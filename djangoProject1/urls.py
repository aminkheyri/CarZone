from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('cars/', include('cars.urls', namespace='cars')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('socialaccount/', include('allauth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)