from django.urls import path
from .views import HomeView, ServiceView, AboutView, TeamView, ContactView

app_name = 'fiter'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('service/', ServiceView.as_view(), name="service_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('team/', TeamView.as_view(), name='team_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),

]