from django.contrib import admin

from modules.example.models.FakeModel import FakeModel

admin.site.register(FakeModel)