from locust import HttpUser, task, between

class SimpleLoadTestUser(HttpUser):
    host = "http://localhost:8000" 
    wait_time = between(1, 2)

    @task(1)
    def test_list_items(self):

    @task(2)
    def test_create_item(self):