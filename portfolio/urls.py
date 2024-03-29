from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from me_port.views import HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += i18n_patterns(
    path('', HomeTemplateView.as_view(), name="home")
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)