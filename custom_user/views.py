from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from custom_user.models import User
from .serializer import UserSerializer


class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({"Error": "Invalid data"}, status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({"Success": "User Created"}, status.HTTP_201_CREATED)


class UserLoginView(APIView):
    pass


class ListOfUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserById(RetrieveAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user_obj = self.get_object()
        serialize_data = self.serializer_class(user_obj)
        return Response({"data": serialize_data.data})

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

