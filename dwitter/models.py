from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
    "self",
    related_name="followed_by",
    symmetrical=False,
    blank=True
)

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver
# ... in methods like post_save i define the reciever that is the func in the bottom of
#  reciever decorator and the i specify the sender in same method
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
        # Remove: post_save.connect(create_profile, sender=User)
#name of model is single and capital letter in first letter on it
class Dweet(models.Model):
    user = models.ForeignKey(
    User, related_name="dweets", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (
        f"{self.user} "
        f"({self.created_at:%Y-%m-%d %H:%M}): "
        f"{self.body[:30]}..."
        )