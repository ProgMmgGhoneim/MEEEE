from django.urls import path

from .views import  (
    PostList ,
    PostDetail ,
    PostCreate ,
    PostUpdate ,
    PostDelete ,
    ctegoryCreate,
    CommentCreate ,
    CommentUpdate ,
    CommentDelete)

urlpatterns = [
    path('', PostList , name='post_list'),
    path('category_create', ctegoryCreate , name='category_create'),
    path('create', PostCreate , name='post_create'),
    path('<int:pk>/', PostDetail.as_view() , name='post_detail'),
    path('<int:pk>/comment_update', CommentUpdate.as_view() , name='comment_update'),
    path('<int:pk>/comment_delet', CommentDelete.as_view() , name='comment_delete'),
    path('<int:pk>/update', PostUpdate , name='post_update'),
    path('<int:pk>/delete', PostDelete , name='post_delete'),



]
