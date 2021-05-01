# Normal In-build Import
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView

# Spacial In-build Import
from Account.models import User, UserOTP
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.core.mail import send_mail
from django.conf import settings
import random

# Created Import
from .models import FollowersFollowing
from .forms import CustomUserCreationForm
from .Acc_MethodDecorator import login_user_only


# class SignUp(CreateView):
#     model = User
#     template_name = 'Account/SignUp.html'
#     form_class = CustomUserCreationForm

def sign_up(request):
    """
    ~~~~~~~~~: By This Part of Code We Handle An User SignUp Section :~~~~~~~~~
    """
    context = {}
    if request.method == 'POST':
        get_otp = request.POST.get('sign_otp')
        if get_otp:
            get_otp_user = request.POST.get('OTP_user')
            user = User.objects.get(id=get_otp_user)
            if int(get_otp) == UserOTP.objects.filter(user=user).last().otp:
                user.is_active = True
                user.save()
                messages.success(request, f"{user.full_name} Your Account has been created Successfully.\nPlease Login\nPlease Check Your Email.")
                return redirect('/Account/Login/')
            else:
                messages.error(request, f'You enter a wrong OTP')
                return render(request, 'Account/SignUp.html', {'otp': True, 'otp_user': user})

        form = CustomUserCreationForm(request.POST)
        # Get the post parameters
        username = request.POST['username']
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        users_data = User.objects.all()
        for data in users_data:
            if data.email == email:
                messages.error(request, 'Please Use Other Email-Id!')
                return redirect('/Account/SignUp/')
            if data.username == username:
                messages.error(request, 'Please User Other User Name!')
                return redirect('/Account/SignUp/')

        if not username.isalnum():
            messages.error(request, 'UserName only contains Character and Numbers ')
            return redirect('/Account/SignUp/')

        if full_name == username:
            messages.error(request, 'User Name and Full Name Should be unique.')
            return redirect('/Account/SignUp/')

        if len(username) > 14 or len(username) < 5:
            messages.error(request, 'Your UserName should be 5 to 14 character')
            return redirect('/Account/SignUp/')

        # Password should be equal to retype password
        if password1 != password2:
            messages.error(request, 'Your 2nd password do not mach')
            return redirect('/Account/SignUp/')
        if len(password1) > 40 or len(password1) < 8:
            messages.error(request, 'Password contains 8 to 40 number, char. and Symbols')
            return redirect('/Account/SignUp/')

        if form.is_valid():
            # get model object data from form here
            user = form.save(commit=False)

            # Cleaned(normalized) data
            password = form.cleaned_data['password1']

            #  User set_password here
            user.set_password(password)
            user.is_active = False
            form.save()
            # OTP Checking
            user_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=user, otp=user_otp)

            # Sending Email For Confirmation
            email_message = f"Hi {full_name}, \n Your OTP is {user_otp}\n Thanks For Creating an Account\n"

            email_subject = 'For Signup click This Below Link'
            email_body = 'Test body'
            # send_mail(
            #     "Welcome To AtaOta.in, Please Verify Your Email",
            #     email_message,
            #     settings.EMAIL_HOST_USER,
            #     [user.email],
            #     fail_silently=False,
            # )

            # OTP Validation
            return render(request, 'Account/SignUp.html', {'otp': True, 'otp_user': user})

        else:
            context['Registration Form'] = form
    else:
        form = CustomUserCreationForm()
    return render(request, 'Account/SignUp.html', {'form': form})  # Account/signUpTest.html


def log_in(request):
    """
    ~~~~~~~~~: A User Can LogIn through this section :~~~~~~~~~
    """

    if request.method == 'POST':
        username = request.POST['Login_username']
        password = request.POST['Login_password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are successfully Logged In")
            return HttpResponseRedirect("/")

        else:
            messages.error(request, 'Invalid Credential! Please Try Again.')
            return redirect('/Account/Login/')
    return render(request, "Account/Login.html")


@login_user_only
def handleLogout(request):
    """
    ~~~~~~~~~: LogOut an User form this website :~~~~~~~~~
    """
    logout(request)
    messages.success(request, "You are success fully logout")
    return redirect("/")


@login_user_only
def password_change(request):
    """     Password Change function Call here      """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated.')
            return redirect('HomePage')
        else:
            messages.error(request, 'Please give valid input!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Account/password_change.html')


# ____________________________________________________________________________________
# =============================[ All User Lists ]=============================
# ____________________________________________________________________________________
@login_user_only
def user_list(request):
    """
    ~~~~~~~~~: Users List View Section :~~~~~~~~~
    """
    users_list = User.objects.all().order_by('-id')

    follow__un_follow = []
    for following in users_list:
        is_following_user = FollowersFollowing.objects.filter(following_user=following,
                                                              followed_by=request.user)
        if is_following_user:
            follow__un_follow.append(following)
    return render(request, 'NormPro/Normalprofile/Normalprofile.html', {
        'UsersList': users_list,
        'following__un_following': follow__un_follow,
    })


@login_user_only
def user_follow_un_follow(request, pk):
    """
    ~~~~~~~~~: To Follow & Un-Follow an User We Use This Code :~~~~~~~~~
    """
    following_user = User.objects.get(pk=pk)
    followed_by = request.user
    follow = FollowersFollowing.objects.filter(following_user=following_user, followed_by=followed_by)
    if follow:
        FollowersFollowing.un_follow(following_user, followed_by)
        return HttpResponse('False')
    else:
        FollowersFollowing.follow(following_user, followed_by)
        return HttpResponse('True')

