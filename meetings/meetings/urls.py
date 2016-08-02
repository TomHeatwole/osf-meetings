from django.conf.urls import url, include
from api import views as apiViews
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Wire up our API using automatic URL routing.

# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^conferences/',
        include('conferences.urls', namespace='conferences')),
    url(r'^submissions/',
        include('submissions.urls', namespace='submissions')),
    url(r'^checklogin/', apiViews.CheckLoggedInView.as_view(),
        name='checklogin'),
    url(r'^users/me', apiViews.CurrentUserView.as_view(), name='current'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^mail/inbound/', include('mail.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
