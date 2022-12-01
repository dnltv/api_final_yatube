from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault, ModelSerializer, ValidationError, SlugRelatedField

from posts.models import Comment, Post, Follow, Group
from rest_framework.validators import UniqueTogetherValidator


User = get_user_model()


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username',
                            read_only=True, default=CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Нельзя подписаться на одного автора дважды.'
            )
        ]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise ValidationError('Нельзя подписаться на себя.')
        return data
