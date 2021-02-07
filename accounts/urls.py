from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path("userLogin", views.userLogin, name="userLogin"),
    path("signup", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit", views.profile_edit, name="edit_profile"),
    path('logged_out/', views.userLoggedout, name='userLoggedout'),

]
