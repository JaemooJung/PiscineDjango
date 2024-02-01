from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class VoteModel(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_upvote = models.BooleanField()

class TipModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField(VoteModel)

    def vote(self, user, is_upvote):
        try:
            vote = self.votes.get(author=user)
            if vote.is_upvote == is_upvote:
                vote.delete()
            else:
                vote.is_upvote = is_upvote
                vote.save()
        except VoteModel.DoesNotExist:
            vote = VoteModel(author=user, is_upvote=is_upvote)
            vote.save()
            self.votes.add(vote)
            self.save()

    def get_upvotes(self):
        return self.votes.filter(is_upvote=True).count()
    
    def get_downvotes(self):
        return self.votes.filter(is_upvote=False).count()