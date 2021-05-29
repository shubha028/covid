from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/',views.login_page),
    path('registration/',views.registration_page),
    path('appointment/',views.appointment_page),
]