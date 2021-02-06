from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index, name = 'index'),
    path('accounts/',include('accounts.urls')),
    path('Transaction/<str:tel>',views.user_transactions),
    path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
