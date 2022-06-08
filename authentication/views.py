from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.serializers import SignupSerializer


class SignupViewset(ModelViewSet):
    serializer_class = SignupSerializer

    @api_view(
        [
            "POST",
        ]
    )
    def signup_view(self, request):
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "Successfully registered a new user."
            data["email"] = user.email
            data["username"] = user.username
        else:
            data = serializer.errors
        return Response(data)
