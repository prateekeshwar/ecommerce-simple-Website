from django.conf.urls import url

from ecommerce import views

urlpatterns = [
    url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^contactus/', 'ecommerce.views.contactus', name='contactus'),
     url(r'^add_category/', 'ecommerce.views.add_category', name='add_category'),
    url(r'^signup/', 'ecommerce.views.signup', name='signup'),
    url(r'^login/', 'ecommerce.views.user_login', name='login'),
    url(r'^logout/', 'ecommerce.views.user_logout', name='logout'),
    ]