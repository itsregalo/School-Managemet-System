from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token

from accounts.api.serializers import RegistrationSerializer

@api_view(['POST', ])
def RegistrationApiView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered the user"
            data['email'] = user.email
            data['username'] = user.username
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            token = Token.objects.get(user=user)
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data) 