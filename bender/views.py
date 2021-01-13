from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from .forms import *
import random
from django.contrib import messages
def home(request):
    bender = UserInfo.objects.all().order_by('-id')
    context  = {
        'bender': bender
    }
    template_name = 'home.html'
    return render(request, template_name, context)

def bender_selection(request):
    context = {}
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        context['form'] = form
        full_name = request.POST['full_name'] 
        image = request.FILES['image'] 
        if form.is_valid():
            if UserInfo.objects.filter(full_name=full_name).exists():
                messages.error(request, f'{full_name} already exists')
                return redirect('/bender-selection')
                print(f'{full_name} already exists')
            else:
                results = ['Earth', 'Fire', 'Air', 'Water']
                bender = random.choice(results)
                UserInfo.objects.create(full_name=full_name, bender=bender, image=image)
                if bender == 'Earth':
                    video = Video.objects.get(id = 2)
                    context['video'] = video
                    benders = f'an {bender}'
                elif bender == 'Air':
                    video = Video.objects.get(id = 1)
                    context['video'] = video
                    benders = f'an {bender}'
                elif bender == 'Water':
                    video = Video.objects.get(id = 4)
                    context['video'] = video
                    benders = f'a {bender}' 
                elif bender == 'Fire':
                    video = Video.objects.get(id = 3)
                    context['video'] = video
                    benders = f'a {bender}' 
                context['message'] = f'{full_name}, Your bender is selected,  you are {benders} bender'
                # messages.success(request,)
                print(f'Your bender is selected,  you are {benders} bender')
                
    else:
        form =  UserForm()
        context['form'] = form
    template_name = 'bender.html'
    return render(request, template_name, context)


def search(request):
    q = request.GET.get('q')
    bender = UserInfo.objects.filter(
        Q(full_name__icontains=q) |
        Q(bender__icontains=q) |
        Q(id__icontains=q)
        ).distinct()
    try:
        context = {
            'bender': bender,
            't': f'search results for {q}'
            }
        template_name = 'all.html'
    except:
        return redirect('/')
    return render(request, template_name, context)