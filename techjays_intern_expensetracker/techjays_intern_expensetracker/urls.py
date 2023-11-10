"""
URL configuration for techjays_intern_expensetracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from .views import PasswordResetView
# from first import views
from expense_tracker import views
# from rest_framework import routers
# router=routers.DefaultRouter()
# router.register(r'lists',views.ExpenseDetailView, 'list')

urlpatterns = [
    path('admin/', admin.site.urls),

    # router url
    # path('api/',include(router.urls)),
    path('account/',include('account.urls')),
    # path('expense_tracker/',include("expense_tracker.urls")),
    # path('api/auth//',include('rest_framework.urls')), #frontend restframework
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('password-reset/<encoded:pk>/<str:token>/',views.ResetPasswordAPI.as_view(),name='password-reset'),
    # path('password-reset/',views.PasswordResetView.as_view(),name='request-password-reset'),
    path('password-reset/', include('django.contrib.auth.urls')),

    # coreapi
    # path('api/',include('core.api.urls')),
]
