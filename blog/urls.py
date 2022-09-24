""" Sets the URLS for the views created in Views.py matching to templates """

from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.AllPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_full'),
]
