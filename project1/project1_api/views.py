from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # untuk http response serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from . import serializers
from . import models
from . import permissions

# Create your views here.
class HelloApiView(APIView):
	""" test API View """
	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		""" mengembalikan list dari APIView fitur """
		an_apiview = [
			'gunakan HTTP method sebagai function (get,post,patch,put,delete)',
			'sama dengan traditional django view',
			'memberikan kamu paling kontrol dengan logic',
			'mapped manually ke URLS'
		]

		return Response({'message': 'Halo', 'an_apiview': an_apiview})

	def post(self, request):
		""" buat hello message dengan nama kita """
		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name') #jika valid akan masuk ke data dictionaries ini
			message = 'Hello {0}'.format(name) #
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #standard if bad request

	def put(self, request, pk=None):
		""" handle update object """
		return Response({'method': 'put'})

	def patch(self, request, pk=None):
		""" patch request, hanya update fields yang dilayani dalam request c~ 127.0.0.1/api/profile/1/ """
		return Response({'method': 'patch'})

	def delete(self, request, pk=None):
		""" delete dan object """
		return Response({'method': 'delete'})

#viewset
#setelah routing telah ditentukan dimana controller digunakan untuk request, controller kamu
#bertanggung jawab untuk membuat sense dari request dan produksi output yang sesuai
class HelloViewSet(viewsets.ViewSet):
	""" test api viewset """
	serializer_class = serializers.HelloSerializer

	def list(self, request):
		""" return a hello message """
		a_viewset = [
			'menggunakan actions (list, create, retrieve, update, partial_update)',
			'otomatis map ke URLS menggunakan Routers',
			'melayani lebih fungsional dengan code yang lebih sedikit'
		]

		return Response({'message': 'Hello!', 'a_viewset': a_viewset})

	def create(self, request):
		""" membuat hello message baru """
		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		""" handle getting object dengan ID """
		return Response({'http_method' : 'GET'})

	def update(self, request, pk=None):
		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):
		""" handles updating part dari object """
		return Response({'http_method': 'PATCH'})

	def destroy(self, request, pk=None):
		""" handle removing sebuat object """
		return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
	""" handle create dan update profile """
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,) #tuples
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email', )

class LoginViewSet(viewsets.ViewSet):
	""" cek email dan pasword dan returen auth token """
	serializer_class = AuthTokenSerializer

	def create(self, request):
		""" menggunakan ObtainAuthTOken APIView untuk validasi dan membuat token. """
		return ObtainAuthToken().post(request)
	#lalu buka login dan ambil token taro di Modheader exstension chrome request header Authorization: token b026228ec4e0b54b3c7ec9b8c1505ada7f28fd22 filter urlpattern: *://0.0.0.0/* lalu liat yang kita login ada form buat put