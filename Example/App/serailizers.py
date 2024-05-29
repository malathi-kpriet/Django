from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    section=serializers.IntegerField()
    roll_no = serializers.IntegerField()
    #id


    class Meta:
        model = Student
        fields = ('__all__')