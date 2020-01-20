from django.shortcuts import render, redirect
from IPython import embed
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm

def signup(request):
  if request.user.is_authenticated:
    return redirect('movies:index')
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('movies:index')
  else:
    form = CustomUserCreationForm
  context = {'form':form}
  return render(request, 'accounts/auth_form.html', context)

def login(request):
  if request.user.is_authenticated:
    return redirect('movies:index')

  if request.method =='POST':
    form = AuthenticationForm(request, request.POST)
    # embed()
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect(request.GET.get('next') or 'movies:index')
  else:
    form = AuthenticationForm()
  context = {'form':form}
  return render(request, 'accounts/auth_form.html', context)

def logout(request):
  auth_logout(request)
  # embed()
  return redirect('accounts:login')

@require_POST
def delete(request):
  request.user.delete()
  return redirect('movies:index')

# 회원 정보 수정
@login_required
def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('movies:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context={'form':form}
  return render(request, 'accounts/auth_form.html', context)

# 비밀번호 변경
@login_required
def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      return redirect('movies:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {'form': form}
  return render(request, 'accounts/auth_form.html', context)
