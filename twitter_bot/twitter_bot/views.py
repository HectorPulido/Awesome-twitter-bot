from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from twitter_data.twitter_bot import TwitterBot
from twitter_data.models import Webhook


class WebhookViewSet(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        name = self.kwargs.get("name")
        wh = Webhook.objects.filter(name=name, enabled=True)
        if not wh.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        wh = wh.first()

        private_key = request.data.get("private_key")

        if private_key == wh.private_key:
            if settings.CONSUMER_KEY == "foo":
                return Response(status=status.HTTP_200_OK)

            bot = TwitterBot(
                settings.CONSUMER_KEY,
                settings.CONSUMER_SECRET,
                settings.ACCESS_TOKEN,
                settings.ACCESS_TOKEN_SECRET,
                0,
            )

            bot.sent_twit(request.data.get("text"))
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)
