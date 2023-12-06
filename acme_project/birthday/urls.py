from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'birthday'

urlpatterns = [
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('login_only/', views.simple_view),
    path(
        'create/',
        login_required(views.BirthdayCreateView.as_view()),
        name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path(
        '<int:pk>/edit/',
        login_required(views.BirthdayUpdateView.as_view),
        name='edit'),
    path(
        '<int:pk>/delete/',
        login_required(views.BirthdayDeleteView.as_view()),
        name='delete')
]
