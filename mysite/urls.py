"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home_view, policy_view, affiliate_view




urlpatterns = [ 
  path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
    path('policy', policy_view, name='policy'),
    path("blog/affiliate", affiliate_view, name="affiliate"),
    path("", include("apis.urls", namespace="apis")),
   

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)