from rest_framework import serializers

class MeetInfoSerializer(serializers.Serializer):

    def sendMessage(self,data):
        print("Hello")

