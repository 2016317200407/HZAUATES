from rest_framework import serializers
from ATES.models import EvaluationPost,TeacherInformationPost
class EvaluationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationPost
        fields = '__all__'

class TeacherInformationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInformationPost
        fields = '__all__'