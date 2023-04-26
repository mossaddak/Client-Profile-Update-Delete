from django.contrib import admin
from django.urls import path, include
from .views import(
    SingUp,
    VerifyOTPview,
    LoginView,
    ProfileView,
    AddClientView,
    #ClientProfileView,
    ClientUserProfileUpdateViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"client-user-profile",ClientUserProfileUpdateViewSet)



urlpatterns = [
    path('account/sing-up/', SingUp.as_view()),
    path('account/verify/', VerifyOTPview.as_view()),
    path('account/login/', LoginView.as_view()),
    path('account/profile/', ProfileView.as_view()),

    path('account/add-client/', AddClientView.as_view()),
]+router.urls
