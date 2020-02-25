from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateProfile
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloAPIView(APIView):
    """API VIEW class"""
    serializer_class = HelloSerializer
    fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

    def get(self, request):
        return Response({'fruit': HelloAPIView.fruit})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            fruit_name = serializer.validated_data.get('fruit_name')
            HelloAPIView.fruit.append(fruit_name)
            message = f'Fruit : {fruit_name}'
            return Response({
                'fruit': HelloAPIView.fruit
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """updating object"""
        return Response({
            'message': 'PUT Method'
        })

    def patch(self, request, pk=None):
        return Response({
            'message': "Partial update (PATCH) request"
        })

    def delete(self, request, pk=None):
        return Response({
            'message': 'Delete objects'
        })


class HelloViewSet(viewsets.ViewSet):
    """test viewset"""
    serializer_class = HelloSerializer
    fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

    def list(self, request):
        return Response({
            'fruit': HelloViewSet.fruit
        })

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('fruit_name')
            return Response(f'fruit {name}')
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):
        return Response({'message': 'Retrive'})


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES






