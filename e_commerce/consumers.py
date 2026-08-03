from channels.generic.websocket import AsyncWebsocketConsumer
import json
from core.models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope["user"]
        if await self.user.is_authenticated():
            self.group_name="users"
            await self.channel_layer.group_add(self.channel_name, self.group_name)
            await self.connect()
        else:
            await self.close()

    async def receive(self, text_data):
        notification_data=await Notification.objects.alast()
        if notification_data:
            title=notification_data.title
            content=notification_data.content
            await self.channel_layer.group_send(self.group_name, {'type':'notification', 'title':title, 'content':content})

    async def notification_message(self, event):
        title=event['title']
        content=event['content']
        await self.send(text_data=json.dumps({'type':'notification', 'title':title, 'content':content}))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        