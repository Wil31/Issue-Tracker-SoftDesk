"""issuetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import SignupViewset
from tracker.views import ProjectViewset, ContributorViewSet

router = SimpleRouter()
router.register('projects', ProjectViewset, basename='projects')
router.register('signup', SignupViewset, basename='signup')

projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register(r'users', ContributorViewSet)

users_router = routers.NestedSimpleRouter(router, "projects", lookup="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(users_router.urls)),
]
