import logging

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from .serializers import FeedbackSerializer

logger = logging.getLogger(__name__)


class FeedbackView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer
    parser_classes = (MultiPartParser, JSONParser, )
    template_name = 'contact_us/index.html'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': _('You will be contacted later by the site administration upon your request')},
                        status=status.HTTP_201_CREATED)
