from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.models import Users


# Create your views here.

def home_page_view(request):
    data = Users.objects.all()
    return render(request, 'task.html', {'users': data})


def detail(request):
    if request.POST:
        data = request.POST
        fullname = data.get('fullname')
        image = data.get('image')
        email = data.get('email')
        phone = data.get('phone')
        job = data.get('job')
        salary = data.get('salary')
        position = data.get('position')
        address = data.get('address')
        website = data.get('website')
        social_media = data.get('social_media')

        Users.objects.create(fullname=fullname, image=image, email=email, phone=phone, job=job, position=position,
                             address=address, salary=salary, website=website, social_media=social_media)
        return redirect(reverse('home'))
    return render(request, 'index.html')


def update_data(request, pk):
    if request.POST:
        data = request.POST
        fullname = data.get('fullname')
        image = data.get('image')
        email = data.get('email')
        phone = data.get('phone')
        job = data.get('job')
        salary = data.get('salary')
        position = data.get('position')
        address = data.get('address')
        website = data.get('website')
        social_media = data.get('social_media')

        Users.objects.filter(id=pk).update(fullname=fullname, image=image, email=email, phone=phone, job=job,
                                           position=position,
                                           address=address, salary=salary, website=website, social_media=social_media)
    user = Users.objects.filter(id=pk).first()
    return render(request, 'profile.html', {'user': user})


def delete_date(request, pk):
    data = get_object_or_404(Users, id=pk)
    data.delete()
    return redirect('/')


