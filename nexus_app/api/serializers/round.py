from rest_framework import serializers
from nexus_app.models import Round

class RoundNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['round_name']

class RoundSerializer(serializers.ModelSerializer):
    test_titles = serializers.SerializerMethodField('test_title_list')

    def test_title_list(self, instance):
        title_list = []
        for test in instance.tests.all():
            title_list.append(test.title)
        return title_list

    class Meta:
        model = Round
        fields = '__all__'