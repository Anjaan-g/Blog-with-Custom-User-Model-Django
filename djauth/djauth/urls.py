from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from blog.views import (
    blog_post_create_view,
)
from search.views import(
    search_view
)
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('blog-new/',blog_post_create_view),
    path('search/',search_view),

]
if settings.DEBUG:
    #test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
