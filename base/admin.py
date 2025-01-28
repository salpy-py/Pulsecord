from django.contrib import admin
from .models import Room, Topic, Message

# Register your models here.

# Register the Topic model with the Django admin site
admin.site.register(Topic)
# Allows administrators to manage topics directly from the admin interface

# Register the Room model with the Django admin site
admin.site.register(Room)
# Allows administrators to create, update, and delete rooms via the admin interface

# Register the Message model with the Django admin site
admin.site.register(Message)
# Enables administrators to view, manage, and delete messages from the admin interface
