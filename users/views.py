from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UpdateUserform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User


def register(request):
    if request.method != 'POST':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    return render(request, "register.html", {'form': form})


@login_required
def profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserform(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "اطلاعات شما بروزرسانی شد")
            return redirect('home')
        return render(request, 'profile.html', {'user_form': user_form})
