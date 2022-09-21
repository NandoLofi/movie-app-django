from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("search/", views.search, name="search"),
    path("show/<int:id>/", views.showdetail, name="showdetail"),
    path("show/<int:show_id>/comments/", views.comments, name="comments"),
]