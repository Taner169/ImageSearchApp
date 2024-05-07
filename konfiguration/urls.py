from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Function to serve as your home view
def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Welcome</title>
            </head>
            <body>
                <p>Welcome to the homepage!</p>
                <a href="/bilder/list-images/">List Images</a><br>
                <a href="/bilder/search/">Search Images</a>
            </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bilder/', include('bilder.urls')),
    path('', home, name='home'),
]

# Append static and media files handling in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
