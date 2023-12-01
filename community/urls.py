from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup
from .views import new_comment

app_name = 'community'


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),

    # mypage관련 url
    path('mypage/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('mypage/<int:pk>/modKeyword/', views.modKeyWord, name='modKeyword'),
    path('keywords/', views.get_keywords),
    path('saveKeywords/<int:pk>/', views.save_keywords, name='save_keywords'),
    path('mypage/<int:pk>/modMajor/', views.modMajor, name='modMajor'),
    path('saveMajors/<int:pk>/', views.save_majors, name='save_majors'),

    path('team/<int:pk>/', views.TeamList.as_view(), name='team'), #post_detail -> team_list // http://127.0.0.1:8000/community/team/11753/
    # path('recommend/<int:pk>/', views.recommend, name='recommend'),
    path('recommend/<int:pk>/', views.Recommend.as_view(), name='recommend'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='community/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('team_post/', views.TeamPostForm.as_view(template_name='community/team_post_form.html'), name="TeamPostForm"),
    path('team/<int:pk>/new_comment/', views.new_comment, name='new_comment'),

]