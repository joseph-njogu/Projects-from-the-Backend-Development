from django.urls import path
# from .views import login, sample_api
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	path('api/login', views.login, name='login'),
	path('api/sample_api', views.sample_api, name='sample_api'),
    path('', TemplateView.as_view(template_name ='login/index.html')),


]