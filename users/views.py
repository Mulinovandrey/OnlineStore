from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import NewUserForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:index')
    form = NewUserForm()
    context = {"form": form}
    return render(request, 'users/register.html', context)

@login_required #декоратор необходимый для разграничения доступа (при условии что пользователь не аутентифицирован, при обращении по адресу /users/profile/ будет возникать ошибка 404)
def profile(request):
    if request.method == "POST":
        image = request.FILES['upload_profile_images']
        contact_number = request.POST.get("contact_number")
        profile_user = Profile(image=image, contact_number=contact_number)
        profile_user.save()
    return render(request, 'users/profile.html')

def seller_profile(request, id):
    seller = User.objects.get(id=id)

    context = {'seller': seller}
    return render(request, 'users/sellerprofile.html', context)