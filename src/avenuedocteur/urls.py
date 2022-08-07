"""avenuedocteur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import settings, views
from .views import HomeView, ProView, AboutView, Proclick, Cltclick, ChoixView

urlpatterns = [
                  path('ad-admin/', admin.site.urls, name='administration'),
                  path('', HomeView.as_view(), name='accueil'),
                  path('galerie/', ProView.as_view(), name='galerie'),
                  path('about/', AboutView.as_view(), name='about'),
                  path('choix/', ChoixView.as_view(), name='choix'),
                  # path('register/', IproView.as_view(), name='inscriptiondoc'),
                  # path('signup/', signup, name='Inscription'),
                  path('proclick/', Proclick.as_view(), name='clickpro'),
                  # path('ipro/', IproView.as_view(), name='ipro'),
                  path('ipro/', views.pro_signup_view, name='ipro'),
                  path('prologin/', LoginView.as_view(template_name='prologin.html'), name='prologin'),
                  # path('prosignup/', prosignup, name='inscription'),
                  path('cltclick/', Cltclick.as_view(), name='cltclick'),
                  path('iclt/', views.clt_signup_view, name='iclt'),
                  path('cltlogin/', LoginView.as_view(template_name='cltlogin.html'), name='cltlogin'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# ---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns += [
    path('pro-dashboard/', views.pro_dashboard_view, name='pro-dashboard'),
]

# ---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns += [

    path('clt-dashboard', views.clt_dashboard_view, name='clt-dashboard'),
]
