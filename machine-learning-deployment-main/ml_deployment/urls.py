
# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('birds/', include('birds.urls')),  # Include app URLs under /birds/
    # path('', include('birds.urls')),  # Or use root path if this is your main app
]