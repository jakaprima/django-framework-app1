from rest_framework import serializers
from . import models

#serializers kaya form input
#Serializer memungkinkan data kompleks seperti contoh querysets dan model dikonversi menjadi tipe data asli Python yang kemudian dapat dengan mudah diterjemahkan ke dalam JSON, XML atau jenis konten lainnya. Serializer juga memberikan deserialization, memungkinkan data parsing dikonversi kembali menjadi tipe kompleks, setelah pertama memvalidasi data yang masuk

class HelloSerializer(serializers.Serializer):
	""" serializes adalah nama field untuk testing APIView """
	name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
	""" serializer untuk user profile object kita """
	class Meta:
		model = models.UserProfile
		fields = ('id', 'email', 'name', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		""" membuat dan return user baru """
		user = models.UserProfile(
			email = validated_data['email'],
			name = validated_data['name']
		)

		user.set_password(validated_data['password'])
		user.save()
		return user
	#setelah ini ke view

