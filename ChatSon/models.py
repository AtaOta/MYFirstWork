from django.db import models
from Account.models import User


# =========================[ User Chat-Message Section ]=======================
class ChatWithFriends(models.Model):
    msg_txt = models.TextField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    # msg_img_or_video = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender.normalprofile.name) + ", Send Message To: " + str(self.receiver.normalprofile.name)

    class Meta:
        ordering = ('timestamp',)

