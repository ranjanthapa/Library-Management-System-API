from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterUser.as_view(), name="register_user"),
    path("user/all/", views.ListOfUser.as_view(), name="list_of_users"),
    path('user/<int:pk>', views.UserById.as_view(), name="user_by_id")

]
