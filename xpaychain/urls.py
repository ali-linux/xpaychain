from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('kalla_table.urls')),
    path('',include('home.urls')),
    path('accounts/',include('accounts.urls')),
    path('Transaction/<str:tel>',views.user_transactions),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
