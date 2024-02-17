from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  
  @property
  def reputation(self):
    from .tip import TipModel
    tips = TipModel.objects.filter(author=self)
    return sum([tip.get_upvotes() * 5 - tip.get_downvotes() * 2 for tip in tips])

  def can_downvote(self):
    return self.is_staff or self.reputation >= 15
  
  def can_delete_tips(self):
    return self.is_staff or self.reputation >= 30