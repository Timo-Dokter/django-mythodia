from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
        path("__reload__/", include("django_browser_reload.urls")),
    ]