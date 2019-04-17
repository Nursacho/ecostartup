from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from staff.views import trash_statistics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('staff/', include('staff.urls')),
    path('statistics/', trash_statistics, name='statistics'),
    path('', include('guide.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
