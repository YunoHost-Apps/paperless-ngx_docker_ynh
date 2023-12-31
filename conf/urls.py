"""
    urls.py
    ~~~~~~~

    https://github.com/paperless-ngx/paperless-ngx/blob/main/src/paperless/urls.py
"""


from django.conf import settings
from django.urls import include, path
from django.views.generic import RedirectView


if settings.PATH_URL:
    # settings.PATH_URL is __PATH__
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path('', RedirectView.as_view(url=f'{settings.PATH_URL}/')),
        path(f'{settings.PATH_URL}/', include('paperless.urls')),
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from paperless.urls import urlpatterns  # noqa
