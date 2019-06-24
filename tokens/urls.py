from django.urls import path,include

from django.contrib import admin
admin.autodiscover()
from rest_framework import routers
from core.views import UserViewSet
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register('user',UserViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'tokens.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/',jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh',jwt_views.TokenRefreshView.as_view()),
    
]
