from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('custom_user.urls')),
    path('library/', include('library.urls')),

]
