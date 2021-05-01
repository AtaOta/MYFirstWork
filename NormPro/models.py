from django.db import models
from Account.models import User, NormalProfile
from django.utils.timezone import now


# =========================[ User Posts Section ]=======================
class NormalPosts(models.Model):
    """
    Normal post Creating model.
    """
    post_pick = models.ImageField(upload_to='UsrPost/post_img', null=True)
    subject = models.CharField(max_length=75)
    msg = models.TextField(null=True, blank=True)
    creat_date = models.DateTimeField(auto_now_add=True)
    uploded_by = models.ForeignKey(to=NormalProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.subject + " | Post Create By: " + str(self.uploded_by)

    def delete(self, *args, **kwargs):
        """
        Deleting previous post image file
        """
        self.post_pick.delete()
        super().delete(*args, **kwargs)

    @property
    def get_comments_total(self):
        all_comment = NormalPostComment.objects.filter(post_is=self.id)
        total_comment = all_comment.count()
        return total_comment


class NormalPostComment(models.Model):
    """
    Normal Post Comment and reply Model
    """
    sr_no = models.AutoField(primary_key=True)
    comments = models.TextField()
    Comment_by = models.ForeignKey(to=NormalProfile, on_delete=models.CASCADE, related_name='Comment_by')
    post_is = models.ForeignKey(to=NormalPosts, on_delete=models.CASCADE, related_name='post_is')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.comments[0:20]) + "....By " + str(self.Comment_by.name) + "...Post Is: " + str(self.post_is)


class LikeDislike(models.Model):
    """
    Normal Post Like and Dislike Model
    """
    liked_by = models.ManyToManyField(User, related_name='NormalPost_Like_by')
    normal_post = models.OneToOneField(to=NormalPosts, on_delete=models.CASCADE)

    # This is for liking purpose
    @classmethod
    def liked(cls, normal_post, liked_by_user):
        obj, create = cls.objects.get_or_create(normal_post=normal_post)
        obj.liked_by.add(liked_by_user)

    # This is for dis-liking purpose
    @classmethod
    def disliked(cls, normal_post, liked_by_user):
        obj, create = cls.objects.get_or_create(normal_post=normal_post)
        obj.liked_by.remove(liked_by_user)
   
    @property
    def get_total_like(self):
        likes = self.liked_by
        total_likes = likes.count()
        return total_likes

    def __str__(self):
        return str(self.normal_post)+" upload by: "+str(self.normal_post.uploded_by)

