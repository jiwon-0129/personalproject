from django.db.models import query, Count, Avg
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *
import geocoder
from django.views.generic import FormView
from mad.forms import PostSearchForm
from django.db.models import Q
# Create your views here.
def showmap(request):
    restaurants=Restaurant.objects.all()
    coordinate= geocoder.ip('me').latlng

    if Filter.objects.count()==0:
        Filter.objects.create()
    option=get_object_or_404(Filter)

    if request.method=='POST':
        form=FilterForm(request.POST, instance=option)
        if form.is_valid():
            option=form.save(commit=False)
            option.save()
            return redirect(showmap)
    else:
        form=FilterForm()

    if option.family == False:
        restaurants=restaurants.exclude(choice='family')
    if option.friends == False:
        restaurants=restaurants.exclude(choice='friends')
    if option.lovers == False:
        restaurants=restaurants.exclude(choice='lovers')
    if option.self == False:
        restaurants=restaurants.exclude(choice='self')
    if option.senior == False:
        restaurants=restaurants.exclude(choice='senior')
    return render(request, 'map.html', {'restaurants':restaurants, 'form':form, 'coordinate':coordinate})

def family(request):
    restaurants=Restaurant.objects.all()
    if Filter.objects.count()==0:
        Filter.objects.create()
    option=get_object_or_404(Filter)
    restaurants=restaurants.exclude(choice='friends')
    restaurants=restaurants.exclude(choice='lovers')
    restaurants=restaurants.exclude(choice='senior')
    restaurants=restaurants.exclude(choice='self')
    return render(request,'family.html', {'restaurants':restaurants})

def friends(request):
    restaurants=Restaurant.objects.all()
    if Filter.objects.count()==0:
        Filter.objects.create()
    option=get_object_or_404(Filter)
    restaurants=restaurants.exclude(choice='family')
    restaurants=restaurants.exclude(choice='lovers')
    restaurants=restaurants.exclude(choice='senior')
    restaurants=restaurants.exclude(choice='self')
    return render(request,'friend.html', {'restaurants':restaurants})

def lovers(request):
    restaurants=Restaurant.objects.all()
    if Filter.objects.count()==0:
        Filter.objects.create()
    option=get_object_or_404(Filter)
    restaurants=restaurants.exclude(choice='friends')
    restaurants=restaurants.exclude(choice='family')
    restaurants=restaurants.exclude(choice='senior')
    restaurants=restaurants.exclude(choice='self')
    return render(request,'lovers.html', {'restaurants':restaurants})

def self(request):
    restaurants=Restaurant.objects.all()
    if Filter.objects.count()==0:
        Filter.objects.create()
    option=get_object_or_404(Filter)
    restaurants=restaurants.exclude(choice='friends')
    restaurants=restaurants.exclude(choice='lovers')
    restaurants=restaurants.exclude(choice='senior')
    restaurants=restaurants.exclude(choice='family')
    return render(request,'self.html', {'restaurants':restaurants})

def senior(request):
    restaurants=Restaurant.objects.all()
    if Filter.objects.count()==0:
        Filter.objects.create()
    option=get_object_or_404(Filter)
    restaurants=restaurants.exclude(choice='friends')
    restaurants=restaurants.exclude(choice='lovers')
    restaurants=restaurants.exclude(choice='family')
    restaurants=restaurants.exclude(choice='self')
    return render(request,'senior.html', {'restaurants':restaurants})

def new(request):
    if request.method=='POST':
        form=RestaurantForm(request.POST)

        if form.is_valid():
            res_field=form.cleaned_data.get('res_field')
    else:
        form = RestaurantForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    tags = request.POST.get('tags', '').split(',')
    form=RestaurantForm(request.POST, request.FILES)
    if form.is_valid():
        new_restaurant=form.save(commit=False)
        new_restaurant.save()
        return redirect('detail', new_restaurant.id)
    return redirect('showmap')


def detail(request, restaurants_id):
    restaurants_detail=get_object_or_404(Restaurant, pk=restaurants_id)
    return render(request, 'detail.html', {'restaurants': restaurants_detail})

def add_comment_to_post(request, restaurants_id):
    restaurants = get_object_or_404(Restaurant, pk=restaurants_id)
    if request.method=="POST":
        form=CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=restaurants
            comment.save()
            return redirect('detail', restaurants_id)

    else:
        form=CommentForm()
    return render(request, 'add_comment_to_post.html', {'form':form})


def update_comment(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', restaurants_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'review_update.html', {'form': form})

def del_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', restaurants_id=comment.post.id)

class TaggedObjectLV(ListView):
    template_name='taggit/taggit_post_list.html'
    model=Restaurant

    def get_queryset(self):
        return Restaurant.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tagname']=self.kwargs['tag']
        return context

