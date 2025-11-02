from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        id = self.room_name.split('_')[1]  # Assuming room_name is in the format 'chat_<id>'
        self.group = await self.get_comic_group(id)  # Fetch the ComicGroup instance

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        # Save the message ONCE here
        message_id = await self.save_message(
            self.group,
            data['sender'],
            data['body'],
            data.get('avatar', None)
        )
        data['id'] = message_id

        # Broadcast without saving again
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': json.dumps(data)
            }
        )

    async def chat_message(self, event):
        # Just send the message to the client — no saving here
        await self.send(text_data=event['message'])

    @database_sync_to_async
    def get_comic_group(self, id):
        from ComicData.models import ComicGroup  # ✅ Lazy import
        return ComicGroup.objects.get(id=id)

    @database_sync_to_async
    def save_message(self, group, sender, body, avatar):
        from Messages.models import ComicGroupMessage  # ✅ Lazy import
        message = ComicGroupMessage.objects.create(
            comic_group=group,
            sender=sender,
            body=body,
            avatar=avatar
        )
        return message.id
