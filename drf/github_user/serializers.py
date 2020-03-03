from rest_framework import serializers
from github_user.models import Github

class GithubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Github
        #fields = '__all__' #或用此句代表全部fields都要
        fields = ("id","user","location","last_modify_date","created")