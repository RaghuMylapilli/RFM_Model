"""finalyear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rfm_model.views import *
from register import views as v

app_name = 'rfm_model'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePageViews.as_view(),name='homepage'),
    path('register/',v.register,name='register' ),
    path('customersupport/',homepage.customersupportViews,name='customersupport'),
    path('',include("django.contrib.auth.urls")),
    path('logout/',homepage.logoutPageViews,name='logout'),
    path('viewpage/', viewPage.as_view(), name="viewpage"),
    path('analysis/', homepage.analysis, name="analysis"),

]
