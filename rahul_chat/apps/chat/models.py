from django.db import models
from django.contrib.auth.models import User

# chat model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_name') #cascade means if user is deleted, all messages will be deleted
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_name') #related_name is used to get the receiver of the message
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Add this line to track read status

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}: {self.content}"
