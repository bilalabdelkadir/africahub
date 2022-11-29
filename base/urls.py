from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="home"),
    path('blog/', views.BlogList, name="blog"),
    path('article/<slug:slug>/', views.article, name="article"),

    path('register/', views.RegisterUser, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUSer, name='logout'),

    path('create-article/', views.CreateArticle, name='create-article'),
    path('update-article/<slug:slug>/', views.UpdateArticle, name='update-article'),
    path('delete-article/<str:pk>', views.DeleteArticle, name='delete-article'),
]
