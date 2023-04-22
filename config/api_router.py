from django.conf import settings
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from vet_sys.users.api.views import UserViewSet, FacebookLogin, GoogleLogin
from vet_sys.pacientes.api.views import EspeciesViewSet, RacasViewSet, PortesViewSet, PacientesViewSet
from vet_sys.clientes.api.views import ClientesViewSet
from vet_sys.funcionarios.api.views import AdministrativosViewSet, VeterinariosViewSet
from dj_rest_auth.views import LoginView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Vet Sys API",
      default_version='v1',
      description="API desenvolvida para Vet Sys – Sistema de Gerenciamento de Clínicas Veterinárias",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ollyverottoboni@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router.register("users", UserViewSet)
router.register("especies", EspeciesViewSet)
router.register("racas", RacasViewSet)
router.register("portes", PortesViewSet)
router.register("pacientes", PacientesViewSet)
router.register("clientes", ClientesViewSet)
router.register("funcionarios", AdministrativosViewSet)
router.register("veterinarios", VeterinariosViewSet)


app_name = "api"

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


   re_path('rest-auth/', include('dj_rest_auth.urls')),
   re_path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
   re_path('rest-auth/login/', LoginView.as_view()),
   re_path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
   re_path('rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]

urlpatterns += router.urls
