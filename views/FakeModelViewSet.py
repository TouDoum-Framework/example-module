from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions
from rest_framework import serializers

from modules.example.models.FakeModel import FakeModel


class FakeModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FakeModel
        fields = ["url", "title", "body"]


class FakeModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FakeModel to be viewed or edited.
    """
    queryset = FakeModel.objects.all()
    serializer_class = FakeModelSerializer
    permission_classes = [permissions.IsAuthenticated]