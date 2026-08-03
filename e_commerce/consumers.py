from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope["user"]
        if await self.user.is_authenticated():
            self.group_name=f"user_{self.user.id}"
            await self.channel_layer.group_add(self.channel_name, self.group_name)
            await self.connect()
        else:
            await self.close()

    async def receive(self, text_data):
        data=await json.loads(text_data)
        message=await data.get('message')
        payload={'type':'notification', 'message':message}
        await self.channel_layer.group_send(self.group_name, payload)

    async def notification(self, event):
        message=event['message']
        await self.send(text_data=await json.dumps({'type':'notification', 'message':message}))

    async def disconnect(self, code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)
        