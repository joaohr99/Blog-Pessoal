# mypersonalblog/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- IMPORTAR SETTINGS
from django.conf.urls.static import static  # <-- IMPORTAR STATIC

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# ESTE BLOCO É APENAS PARA AMBIENTE DE DESENVOLVIMENTO!
# Ele ajuda o Django a servir arquivos estáticos e de mídia.
# if settings.DEBUG:
#  urlpatterns += static(settings.STATIC_URL,
#    document_root=settings.STATIC_ROOT)
# Se você tiver arquivos de mídia (uploads de usuários), adicione também:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
