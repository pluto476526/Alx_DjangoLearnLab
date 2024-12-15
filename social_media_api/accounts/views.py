from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'New user reqistered'}, status=201)
        return Response(serlializer.errors, status=400)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
        })


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response({'error': 'You cannot follow yourself'}, status=400)

            request.user.following.add(user_to_follow)
            return Response({'message': 'You are now following {user_to-follow}'}, status=200)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


class UnFollowUserView(APIView):
    permission_clases = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({'message': 'You have unfollowed {user_to_unfollow}'}, status=200)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
