from channels.generic.websocket import WebsocketConsumer


class ChatConsumer (WebsocketConsumer) :

    def connect(self):
        chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass

