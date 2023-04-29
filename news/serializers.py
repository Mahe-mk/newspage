from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ExtraField, Categories, News, UsersFavoriteCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ExtraFieldSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ExtraField
        fields = ('id', 'user', 'phone_number', 'addresses', 'birthdays')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title', 'category_image')

class NewsSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()
    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'image', 'detail')

class UsersFavoriteCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategoriesSerializer()
    class Meta:
        model = UsersFavoriteCategory
        fields = ('id', 'user', 'category')
