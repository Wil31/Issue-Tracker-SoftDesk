from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import SignupViewset
from tracker.views import (
    ProjectViewSet,
    ContributorViewSet,
    IssueViewSet,
    CommentViewSet,
)

router = SimpleRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("signup", SignupViewset, basename="signup")

projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register("users", ContributorViewSet, basename="contributor")
projects_router.register("issues", IssueViewSet, basename="issues")

users_router = routers.NestedSimpleRouter(router, "projects", lookup="user")

issues_router = routers.NestedSimpleRouter(projects_router, "issues", lookup="issues")
issues_router.register("comments", CommentViewSet, basename="comments")

# comments_router = routers.NestedSimpleRouter(
#     issues_router, "comments", lookup="comments"
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("api/", include(projects_router.urls)),
    path("api/", include(users_router.urls)),
    path("api/", include(issues_router.urls)),
    # path("api/", include(comments_router.urls)),
]
