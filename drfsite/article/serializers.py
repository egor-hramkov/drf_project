from rest_framework import serializers

from article.models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = "__all__"


class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     time_created = serializers.DateTimeField(read_only=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance
