from .views import registration_view, update_account_view, account_properties_view, ObtainAuthTokenView, SpellViewSet, \
    SpellDetailsViewSet
from django.urls import path
from knox import views as knox_views

app_name = "api"

urlpatterns = [
    path('api/register/',registration_view,name='register'),
    path('api/properties/',account_properties_view,name='properties'),
    path('api/properties/update/',update_account_view,name='update'),
    path('api/login/',ObtainAuthTokenView.as_view(),name='login'),
    path('api/spell/', SpellViewSet.as_view(), name='spell'),
    path('api/spell/<int:id>/', SpellDetailsViewSet.as_view(), name='detail'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),

]