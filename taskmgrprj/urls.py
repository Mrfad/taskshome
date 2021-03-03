from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Bookstop Tasks | Admin Area'
admin.site.site_title = 'Bookstop Tasks' 
admin.site.index_title= 'Bookstop Tasks'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('tasks.urls')),
    path('', include('suppliers.urls')),
    path('', include('customers.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, Document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)