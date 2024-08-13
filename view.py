from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AvatarUpdateForm

@login_required
def update_avatar(request):
    if request.method == 'POST':
        form = AvatarUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправлення на сторінку профілю після успішного оновлення
    else:
        form = AvatarUpdateForm(instance=request.user.profile)
    
    return render(request, 'users/update_avatar.html', {'form': form})
