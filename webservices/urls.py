from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from dogapp import views
# Import views from the dogapp for REST and SOAP endpoints
from dogapp.views import (
    dog_service,
    rest_get_dog,
    DogList,
    DogDetail,
    BreedList,
    BreedDetail
)

# JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# GraphQL view
from graphene_django.views import GraphQLView
from dogapp.schema import schema

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # SOAP Service for Dogs
    path('soap/dogservice/', dog_service),

    # REST API for Dogs
    #path('api/dogs/', DogList.as_view(), name='dog-list'),
    #path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    # Dog Endpoints
    path('api/dogs/', views.DogList.as_view(), name='dog-list'),  # GET (list), POST
    path('api/dogs/<int:pk>/', views.DogDetail.as_view(), name='dog-detail'),  # GET, PUT, DELETE

    # Breed Endpoints
    path('api/breeds/', views.BreedList.as_view(), name='breed-list'),  # GET (list), POST
    path('api/breeds/<int:pk>/', views.BreedDetail.as_view(), name='breed-detail'),  # GET, PUT, DELETE

    # REST API for Breeds
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),

    # GraphQL endpoint
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Account login/logout
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
