# Normal In-build Import
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Spacial In-build Import
from Account.models import User
from Account.models import FollowersFollowing
from django.contrib.auth.decorators import login_required

# Build-In Import
from .models import ChatWithFriends

# =================[ This is for decorators ]==================
from Account.Acc_MethodDecorator import login_user_only
decorators = [login_user_only]


@login_user_only
def following_list(request):
    """
    ~~~~~~~~~: This Section Import HowMany Followers and Following Of an User :~~~~~~~~~
    """
    all_following_users = FollowersFollowing.objects.filter(followed_by=request.user)
    return render(request, 'NormPro/Normalprofile/Normalprofile.html',
     {'followings': all_following_users})


@login_user_only
def followers_list(request):
    """
    ~~~~~~~~~: This Section Import HowMany Followers Of an User :~~~~~~~~~
    """
    main_user = request.user
    all_user_list = User.objects.all().order_by('-id')

    this_is_list_of_Followers = []
    for followers in all_user_list:
        is_following_user = FollowersFollowing.objects.filter(following_user=main_user,
                                                              followed_by=followers)
        if is_following_user:
            this_is_list_of_Followers.append(followers)
    return render(request, 'NormPro/Normalprofile/Normalprofile.html', {'followers': this_is_list_of_Followers})


@login_user_only
def chat_list(request):
    main_user = request.user
    all_user_list = User.objects.all().order_by('-id')
    all_following_users = FollowersFollowing.objects.filter(followed_by=request.user)

    this_is_list_of_Followers = []
    this_is_list_of_Following = []
    for followers in all_user_list:
        is_following_user = FollowersFollowing.objects.filter(following_user=main_user,
                                                              followed_by=followers)
        if is_following_user:
            this_is_list_of_Followers.append(followers)

    for following in all_following_users:
        this_is_list_of_Following.append(following.following_user)

    # Joining All User logic
    rest_list = [y for x in [this_is_list_of_Followers, this_is_list_of_Following] for y in x]

    # Remove Duplicate Logic
    chat_list = list(dict.fromkeys(rest_list))

    return render(request, 'ChatSon/ChatList.html', {'ChatList': chat_list})


# ____________________________________________________________________________________
# =============================[ Chat section ]=============================
# ____________________________________________________________________________________
@login_user_only
def chat_son_chat(requests, pk):
    """
    ~~~~~~~~~: This Code Bit is UseCase in Case of Chatting With Other User :~~~~~~~~~
    """
    requested_receiver = User.objects.get(pk=pk)
    requested_sender = requests.user
    all_receiver_message_text = ChatWithFriends.objects.filter(sender=requested_sender, receiver=requested_receiver)
    all_sender_message_text = ChatWithFriends.objects.filter(sender=requested_receiver, receiver=requested_sender)
    all_text_messages = all_receiver_message_text | all_sender_message_text
    recent_text_messages = all_text_messages.distinct().order_by('timestamp')
    if requests.method == "POST":
        text_message = requests.POST['message_text']
        chat_message = ChatWithFriends(msg_txt=text_message, receiver=requested_receiver, sender=requested_sender)
        chat_message.save()
        return HttpResponseRedirect(f"/chatting/create_chat/{pk}")
    return render(requests, 'ChatSon/chatSon.html',
                  {'Detail_Of_User': requested_receiver,
                     'all_messages': recent_text_messages
                   })


@login_user_only
def chat_msg_list(requests, pk):
    requested_receiver = User.objects.get(pk=pk)
    requested_sender = requests.user
    all_receiver_message_text = ChatWithFriends.objects.filter(sender=requested_sender, receiver=requested_receiver)
    all_sender_message_text = ChatWithFriends.objects.filter(sender=requested_receiver, receiver=requested_sender)
    all_text_messages = all_receiver_message_text | all_sender_message_text
    recent_text_messages = all_text_messages.distinct().order_by('timestamp')
    return render(requests, 'ChatSon/ChatMsgList.html',
                  {
                     'all_messages': recent_text_messages,
                      'receiverID': requested_receiver.id,
                  })
