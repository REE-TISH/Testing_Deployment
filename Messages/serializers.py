from rest_framework import serializers
from .models import ComicGroupMessage,Comments,InboxComments
from rest_framework.response import Response


class ComicGroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicGroupMessage
        fields = '__all__'

class CommentSectionSerializer(serializers.ModelSerializer):
    InBoxComments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comments
        fields = ['id','sender','body','created_at','user_id','InBoxComments']

    def get_InBoxComments(self,obj):
        query_set = obj.CommentsChild.all()
        if not query_set:
            return []
        serializer = InboxCommentsSerializer(query_set,many=True)
        return serializer.data

class InboxCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxComments
        fields = ['id','sender','body','created_at']

