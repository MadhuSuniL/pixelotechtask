from django.contrib import admin
from django.urls import path , include
from task_app.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('user/', include('otp_auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
