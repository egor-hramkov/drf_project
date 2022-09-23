from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    time_created = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()