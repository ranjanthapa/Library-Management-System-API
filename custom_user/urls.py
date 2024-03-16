from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/register", views.RegisterUser.as_view(), name="register_user"),
    path("user/all/", views.ListOfUser.as_view(), name="list_of_users"),
    path('user/<int:pk>', views.UserById.as_view(), name="user_by_id"),

    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
