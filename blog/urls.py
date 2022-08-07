from django.urls import path

from .views import PostListView,PostDetailView,category,search
urlpatterns = [
    path('search/', search, name="search"),
    path('',PostListView.as_view() , name ='frontpage'),
    path('category/<slug:slug>' ,category, name='category' ),
    path('<slug>/',PostDetailView.as_view() , name='post_detail')
]
 
  