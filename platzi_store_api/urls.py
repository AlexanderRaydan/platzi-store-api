from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

#views
from products.views import funtion_test , ProductsViewSet 
from rest_framework import routers


route = routers.DefaultRouter()
route.register('products' , ProductsViewSet)
#route.register('test' , funtion_test )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include(route.urls)),
    path('api/test/<str:id>' , funtion_test , name = 'test')

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
