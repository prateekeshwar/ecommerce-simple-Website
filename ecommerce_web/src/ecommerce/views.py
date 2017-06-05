from django.shortcuts import render,get_object_or_404
from .forms import UserForm,UserProfileForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Category
from .forms import CategoryForm
import googlemaps
import requests
# Create your views here.

def home(request):
    queryset_list=Category.objects.all()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context={
        'title':'Category',
        'category_list':queryset,
    }    
   
    return render(request, "home.html", context)


def add_category(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    form=CategoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(reverse('ecommerce:home'))
    else:
        messages.error(request,"Not Successfully Created")
        context={
            "form":form,
        }
    return render(request, "add_category.html", context)

def contactus(request):
	form=UserProfileForm
	address = "Saket Metro Station, South Delhi, India"
	api_key = "AIzaSyCADt6sAhZUkrmSOehKePE5tcarm-_aeYI"
	api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
	api_response_dict = api_response.json()
	if api_response_dict['status'] == 'OK':
	    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        print 'Latitude:', latitude
        print 'Longitude:', longitude
        x = 'Latitude:', latitude
        y = 'Longitude:', longitude
	context = {
		"form": form,
		"x":x,
		"y":y,
	}
	return render(request, "contactus.html", context)

def signup(request):
    signed = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            signed = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,'signup.html',{'user_form': user_form,'signed': signed} )
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Yinc Mall account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})

    
    
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/logout/')
    
    
