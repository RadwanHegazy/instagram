from channels.generic.websocket import WebsocketConsumer
from chat.models import Chat, Message
from asgiref.sync import async_to_sync
import json
from chat.apis.serializers import GetMessageSerializer

class ChatConsumer (WebsocketConsumer) :

    def connect(self):

        chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.sender = self.scope['user']

        try : 
            self.chat_model = Chat.objects.get(id=chat_id)

            if self.sender not in self.chat_model.users.all() : 
                self.close()
                return
            
        except Chat.DoesNotExist:
            self.close()
            return
        
        self.GROUP = f'chat_{self.chat_model.id}'
        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.GROUP,
            self.channel_name
        )


    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP,
            self.channel_name
        )


    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        content = data.get('content', '')
        image = data.get('image', None)

        message = Message.objects.create(
            sender=self.sender,
            chat=self.chat_model,
            content=content
        )

        message.save()

        msg_serialiser = GetMessageSerializer(message)

        async_to_sync(self.channel_layer.group_send)(
            self.GROUP,
            {
                'type' : 'send_msg',
                'data' : msg_serialiser.data
            }
        )

    def send_msg(self ,event) : 
        message = event['data']
        self.send(text_data=json.dumps(message))


