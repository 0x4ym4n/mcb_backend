"""ADGM_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from base.api.company import send_email, search_company, get_company_data
from base.api.hackathon import truststamp_token, register_person, get_image_it2, perform_login
from base.api.utils import getSDKToken
from baseproject import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(r'company/search_company/', search_company),
                  path(r'company/get_company_data/', get_company_data),
                  path(r'company/send_email/', send_email),
                  path(r'uqudo/generate_token/', getSDKToken),
                  path(r'hackathon/register', register_person),
                  path(r'hackathon/token', truststamp_token),
                  path(r'hackathon/generate_it2', get_image_it2),
                  path(r'hackathon/perform_login', perform_login),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
