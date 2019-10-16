from django.urls import path

from . import views

app_name = 'competition'
urlpatterns = [
  path('inside/', views.inside, name='index'),
  path('signup/', views.signup, name='signup'),
  path('nextlap/', views.NextlapView.as_view(), name='nextlap'),
]