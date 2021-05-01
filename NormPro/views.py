# Python built in function
import json

# Normal In-build Import
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages

# Spacial In-build Import
from Account.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Created Import
from Account.models import NormalProfile
from .models import NormalPosts, NormalPostComment, LikeDislike

# :~~~~~~~~~~:[This Belows are For Image Processing Purpose ]:~~~~~~~~~~:
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import time, base64

# =================[ This is for decorators ]==================
from Account.Acc_MethodDecorator import login_user_only
decorators = [login_user_only]


# _________________________________________________________________________
#                   This is Profile Section Of An User
# _________________________________________________________________________
@method_decorator(decorators, name='dispatch')
class NormalProfileView(TemplateView):
    model = NormalProfile
    template_name = 'NormPro/Normalprofile/Normalprofile.html'

    def get(self, request, *args, **kwargs):
        """
        According to this function We Fetch data from the data base ordering by reverse Id :~~~~~~~~~
        here (N_post = Normal profile posts) :~~~~~~~~~
        (my_post_lists > refer fetching all post from the data base :~~~~~~~~~
        """
        normal_post_lists = NormalPosts.objects.all().order_by("-id")
        norma_post_likes = []
        for post in normal_post_lists:
            is_liked = LikeDislike.objects.filter(normal_post=post, liked_by=request.user)
            if is_liked:
                norma_post_likes.append(post)
        return render(request, self.template_name, {
            'normal_post_lists': normal_post_lists,
            'norma_post_likes': norma_post_likes,
        })


# User Profile Update Section
@method_decorator(decorators, name='dispatch')
class NormalProfileUpdateView(UpdateView):
    """
    ~~~~~~~~~: This Section is Help Us to Update An User Normal Profile :~~~~~~~~~
    """
    model = NormalProfile
    template_name = 'NormPro/Normalprofile/NormalProfile_Update.html'
    fields = ["name",
              "age",
              "address",
              "status",
              "phone_no",
              "description",
              "gender",
              "profile_pick",
              "profile_Background_pic"]

    def form_valid(self, form):
        self.object = form.save()
        self.object = self.request.user.normalprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"{self.request.user.normalprofile.name} you successfully Update your Profile")
        return f"/profile/NormalProfile/{self.request.user.id}/"


# =============================[ Capture An Image Through WebCam ]=============================
@login_user_only
def change_picture_by_capturing(request):
    if request.method == 'POST':
        image_data = request.POST.get('imageData')  # get image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  # Image data
        myfile = "profile-" + time.strftime("%Y%m%d-%H%M%S") + "." + ext  # filename
        fs = FileSystemStorage()
        # filename = fs.save(myfile, data) This is the basic example how ot save this file
        req_user = NormalProfile.objects.get(user=request.user)
        req_user.profile_pick = fs.save("Profile/images/"+myfile, data)
        req_user.save()
        return HttpResponse("okay")
    return render(request, 'NormPro/CapureImage/CaptureImage_Webcam.html')


# _________________________________________________________________________
#                          User Self post section
# _________________________________________________________________________
# =============================[ Normal Post Create ]=============================
@method_decorator(decorators, name='dispatch')
class NormalPostCreateView(CreateView):
    """
    ~~~~~~~~~: This Bit of Code is Help Us to Create A Normal Post :~~~~~~~~~
    """
    model = NormalPosts
    template_name = 'NormPro/NormalPost_Related/NormalPost_Create.html'
    fields = ['subject', 'post_pick', 'msg']

    def form_valid(self, form):
        self.object = form.save()
        self.object.uploded_by = self.request.user.normalprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"{self.request.user.normalprofile.name} you successfully Create This Post")
        return f"/profile/NormalProfile/{self.request.user.id}/"


@login_user_only
def create_post_by_capturing(request):
    """
    :~~~~~~~~:~~~~~~~:[ Capture An Image Through WebCam ]:~~~~~~~~:~~~~~~~:
    """
    if request.method == "POST":
        image_data = request.POST.get('imageData')  # get image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  # Image data
        myfile = "profile-" + time.strftime("%Y%m%d-%H%M%S") + "." + ext  # filename
        fs = FileSystemStorage()
        location_img = fs.save("UsrPost/post_img/"+myfile, data)
        subject_text = request.POST.get('subject')
        uploded_by = request.user.normalprofile
        normal_post = NormalPosts.objects.create(post_pick=location_img,
                                                 subject=subject_text,
                                                 uploded_by=uploded_by)
        normal_post.save()
    return HttpResponse('Success')


@login_user_only
def normal_post_delete(request, pk):
    """
    ~~~~~~~~~: By this part of Code We Delete A Normal Post :~~~~~~~~~
    """
    if request.method == 'POST':
        """
        ~~~~~~~~~: This Vew Function Delete A particular post according to Post Creator :~~~~~~~~~
        """
        this_post_ = NormalPosts.objects.get(id=pk)
        print(this_post_)
        this_post_.delete()
        return HttpResponse('true')
    return HttpResponse('false')


@method_decorator(decorators, name='dispatch')
class UserNormalPostList(TemplateView):
    """
    ~~~~~~~~~: According to this Class base View we Showing All Users Posts :~~~~~~~~~
    """
    template_name = 'NormPro/Normalprofile/Normalprofile.html'

    def get(self, request, *args, **kwargs):
        """
        According to this function We Fetch data from the data base ordering by reverse Id
        here (N_post = Normal profile posts)
        (my_post_lists > refer fetching all post from the data base
        """
        my_normal_post_lists = NormalPosts.objects.filter(uploded_by=request.user.normalprofile).order_by("-id")
        return render(request, self.template_name, {
            'my_normal_post_lists': my_normal_post_lists,
        })


@login_user_only
def create_normalPost_comment(requests):
    """
    ~~~~~~~~~: Create A Normal Post Comments By this Code_bit :~~~~~~~~~
    """
    if requests.method == 'POST':
        comment = requests.POST.get("NormalComment")
        Comment_by = requests.user.normalprofile
        PostId = requests.POST.get('NormalPostId')
        normalPost = NormalPosts.objects.get(id=PostId)
        Normal_Post_Comment = NormalPostComment(comments=comment, Comment_by=Comment_by, post_is=normalPost)
        Normal_Post_Comment.save()
        return redirect(f"/profile/List_comment/{PostId}")

    return render(requests, 'NormPro/NormalPost_Related/Post_Comment.html')


@login_user_only
def normal_post_comment_list(requests, pk):
    """
    ~~~~~~~~~: This is The List View Of Comments :~~~~~~~~~
    """
    normal_comments = NormalPostComment.objects.filter(post_is=pk).order_by('timeStamp')
    return render(requests, 'NormPro/NormalPost_Related/Post_Comment.html',
                  {'normal_comments': normal_comments})



@login_user_only
def normalpost_like_dislike(requests, pk):
    """
    ~~~~~~~~~: To Like & Dis-Like a Post This Section Play a Important Role :~~~~~~~~~
    """
    normal_post = NormalPosts.objects.get(pk=pk)
    liked_by = requests.user
    like = LikeDislike.objects.filter(normal_post=normal_post, liked_by=liked_by)
    if like:
        LikeDislike.disliked(normal_post, liked_by)
        like_count = normal_post.likedislike.liked_by.count()  # This is Like Counter
        total_likes = like_count
        like_data = [{"liked": "False", "likes": total_likes}]
        return HttpResponse(json.dumps(like_data))
    else:
        LikeDislike.liked(normal_post, liked_by)
        like_count = normal_post.likedislike.liked_by.count()  # This is Like Counter
        total_likes = like_count
        like_data = [{"liked": "True", "likes": total_likes}]
        return HttpResponse(json.dumps(like_data))

