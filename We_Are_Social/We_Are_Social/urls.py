"""We_Are_Social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from home import views as home_views
from accounts import views as accounts_views
from products import  views as product_views
from magazines import views as magazine_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_views.get_index, name='index'),
# Faltpages
    url(r'^pages/',include('django.contrib.flatpages.urls')),

# Email Auth
    url(r'^register/$',accounts_views.register, name='register'),
    url(r'^profile/$',accounts_views.profile, name='profile'),
    url(r'^login/$',accounts_views.login, name='login'),
    url(r'^logout/$',accounts_views.logout, name='logout'),


# Paypal Urls
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
    url(r'^magazines/$', magazine_views.all_magazines),
]
