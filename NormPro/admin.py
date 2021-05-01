from django.contrib import admin
from .models import NormalPosts, NormalPostComment, LikeDislike


admin.site.register(NormalPosts)
admin.site.register(NormalPostComment)
admin.site.register(LikeDislike)

