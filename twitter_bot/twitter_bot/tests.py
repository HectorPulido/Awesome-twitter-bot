from django.test import TestCase, Client
from twitter_data.models import Webhook


class WebhookTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_webhook_get(self):
        """
        Tests that a get /webhook/ is type 405
        """
        response = self.client.get("/hook/test/")
        self.assertEqual(response.status_code, 405)

    def test_webhook_post_with_false_slug(self):
        """
        Tests that a post /webhook/<slug> with false data is type 404
        """
        response = self.client.post("/hook/slug/", {"data": "false"})
        self.assertEqual(response.status_code, 404)

    def test_webhook_post_with_true_slug(self):
        """
        Tests that a post /webhook/<slug> with true slug but without data is type 403
        """
        # create the webhook
        Webhook.objects.create(name="slug", enabled=True)
        response = self.client.post("/hook/slug/")
        self.assertEqual(response.status_code, 403)

    def test_webhook_post_with_true_slug_and_data(self):
        """
        Tests that a post /webhook/<slug> with true slug and data is type 200
        """
        Webhook.objects.create(name="slug2", enabled=True, private_key="test")
        response = self.client.post(
            "/hook/slug2/", {"private_key": "test", "text": "Hola mundo"}
        )
        self.assertEqual(response.status_code, 200)
