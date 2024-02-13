
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class WallpaperConsumer(WebsocketConsumer):
    def connect(self):
        # Chamado quando o websocket é mão de obra
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"wallpaper_{self.room_name}"

        # Junte-se ao grupo
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps(
            'type:connection_established',
            'message:connected'
        ))

    def disconnect(self, close_code):
        # Chamado quando o WebSocket é fechado por algum motivo
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # Chamado quando recebe uma mensagem do WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envia a mensagem para o grupo
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'wallpaper_update',
                'message': message
            }
        )

    # Recebe a mensagem do grupo
    def wallpaper_update(self, event):
        message = event['message']

        # Envia a mensagem para o WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
