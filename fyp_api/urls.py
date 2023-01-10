from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('vehicle/',include('vehicle.urls')),
    path('servicing/',include('servicing.urls')),
    path('billbook/',include('billbook.urls')),
    path('workshop/',include('workshop.urls'))

]
