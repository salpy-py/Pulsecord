from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Topic Model
class Topic(models.Model):
    name = models.CharField(max_length=200)
    # Represents a topic (category) for rooms
    # 'name' is a string field with a maximum length of 200 characters

    def __str__(self):
        return self.name
        # String representation of the Topic model (returns the name of the topic)

# Room Model
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # ForeignKey to the User model; 'host' refers to the user who created the room
    # on_delete=models.SET_NULL: If the user is deleted, set 'host' to null

    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # ForeignKey to the Topic model; each room is associated with a topic
    # on_delete=models.SET_NULL: If the topic is deleted, set 'topic' to null

    name = models.CharField(max_length=200)
    # Name of the room

    description = models.TextField(null=True, blank=True)
    # Optional field for a room description
    # 'null=True' allows null values in the database
    # 'blank=True' allows the field to be empty in forms

    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    # Many-to-Many relationship with User
    # Tracks users who are participating in the room
    # 'related_name' provides an alternative way to access this relationship from the User model

    updated = models.DateTimeField(auto_now=True)
    # Automatically updates the timestamp whenever the room is modified

    created = models.DateTimeField(auto_now_add=True)
    # Automatically sets the timestamp when the room is created

    class Meta:
        ordering = ["-updated", "-created"]
        # Orders the rooms by most recently updated and then by most recently created

    def __str__(self):
        return self.name
        # String representation of the Room model (returns the name of the room)

# Message Model
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey to the User model; 'user' refers to the message sender
    # on_delete=models.CASCADE: Deletes the message if the associated user is deleted

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # ForeignKey to the Room model; each message belongs to a specific room
    # on_delete=models.CASCADE: Deletes the message if the associated room is deleted

    body = models.TextField()
    # Text field for the message content

    updated = models.DateTimeField(auto_now=True)
    # Automatically updates the timestamp whenever the message is modified

    created = models.DateTimeField(auto_now_add=True)
    # Automatically sets the timestamp when the message is created

    class Meta:
        ordering = ["-updated", "-created"]
        # Orders the messages by most recently updated and then by most recently created

    def __str__(self):
        return self.body[0:50]
        # String representation of the Message model (returns the first 50 characters of the message body)
