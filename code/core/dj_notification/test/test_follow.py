from django.test import TestCase
from channels.testing import WebsocketCommunicator
from core.asgi import application  # Replace with your ASGI application
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
import json
import asyncio

User = get_user_model()

class NotificationConsumerTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Generate an access token for the user
        self.token = str(AccessToken.for_user(self.user))

    async def async_test_notification_consumer(self):
        # Create a WebSocket connection with the user's token
        communicator = WebsocketCommunicator(
            application,
            f"ws/notification?token={self.token}"
        )
        
        # Connect to the WebSocket
        connected, _ = await communicator.connect(timeout=30)
        
        self.assertTrue(connected)

        # # Simulate sending a notification to the user's group
        # notification_data = {
        #     'type': 'notification',
        #     'data': {
        #         'message': 'You have a new notification!'
        #     }
        # }
        # await communicator.send_json_to(notification_data)

        # # Receive the notification from the WebSocket
        # response = await communicator.receive_json_from()
        # self.assertEqual(response, {
        #     'message': 'You have a new notification!'
        # })

        # # Disconnect the WebSocket
        # await communicator.disconnect()

    def test_notification_consumer(self):
        # Run the async test code synchronously
        asyncio.run(self.async_test_notification_consumer())