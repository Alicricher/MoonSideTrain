import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app
from storage import load_tasks


class TaskAPITests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.file_patch = patch(
            "storage.TASKS_FILE", Path(self.directory.name) / "tasks.json"
        )
        self.file_patch.start()
        self.addCleanup(self.file_patch.stop)
        self.client = TestClient(app)
        self.addCleanup(self.client.close)

    def test_create_list_complete_and_reload(self):
        self.assertEqual(self.client.get("/tasks").json(), [])
        response = self.client.post("/tasks", json={"title": "  Учить Python  "})
        self.assertEqual(response.status_code, 201)
        task = response.json()
        self.assertEqual(task, {"id": 1, "title": "Учить Python", "status": "TODO"})
        self.assertEqual(self.client.get("/tasks").json(), [task])
        response = self.client.patch("/tasks/1/complete")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "DONE")
        self.assertEqual(load_tasks(), [response.json()])
        with TestClient(app) as new_client:
            self.assertEqual(new_client.get("/tasks").json(), load_tasks())
        self.assertEqual(self.client.patch("/tasks/1/complete").status_code, 200)

    def test_invalid_requests_do_not_create_tasks(self):
        for body in ({}, {"title": ""}, {"title": "   "}, {"title": 12},
                     {"title": "a" * 201}):
            with self.subTest(body=body):
                self.assertEqual(self.client.post("/tasks", json=body).status_code, 422)
        self.assertEqual(self.client.patch("/tasks/999/complete").status_code, 404)
        self.assertEqual(self.client.patch("/tasks/abc/complete").status_code, 422)
        self.assertEqual(self.client.get("/tasks").json(), [])

    def test_concurrent_creates_preserve_all_tasks(self):
        def create(index):
            return self.client.post("/tasks", json={"title": f"Task {index}"})

        with ThreadPoolExecutor(max_workers=4) as executor:
            responses = list(executor.map(create, range(12)))
        self.assertTrue(all(response.status_code == 201 for response in responses))
        tasks = self.client.get("/tasks").json()
        self.assertEqual(len(tasks), 12)
        self.assertEqual(len({task["id"] for task in tasks}), 12)

    def test_docs_and_openapi(self):
        self.assertEqual(self.client.get("/docs").status_code, 200)
        schema = self.client.get("/openapi.json").json()
        self.assertIn("post", schema["paths"]["/tasks"])
        self.assertIn("patch", schema["paths"]["/tasks/{task_id}/complete"])


if __name__ == "__main__":
    unittest.main()
