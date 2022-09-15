from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_trail.settings import AUTH_USER_MODEL


admin.site.register(get_user_model())

