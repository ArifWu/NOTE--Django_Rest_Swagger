from django.shortcuts import render

from github_user.models import Github
from github_user.serializers import GithubSerializer

from rest_framework import viewsets


# Performing raw SQL queries時，用到的model
from github_user.models import Github
from github_user.models import fun_raw_sql_query,fun_sql_cursor_update
from github_user.serializers import GithubSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status


# Create your views here.
# 只要這樣寫就擁有 CRUD 的全部功能
class GithubViewset(viewsets.ModelViewSet):
    queryset = Github.objects.all()
    serializer_class = GithubSerializer
    
    
    
    
    # /api/github_user/raw_sql_query/
    @action(detail=False,methods=['get'],url_path='raw_sql_query')
    def raw_sql_query(self, request):
        user = request.query_params.get('user', None)
        user_info = fun_raw_sql_query(user=user)
        serializer = GithubSerializer(user_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
    
    
    # /api/github_user/sql_cursor/
    @action(detail=False,methods=['post'],url_path='sql_cursor')
    def sql_cursor(self, request):
        user = request.data.get('user')
        
        #print("=========================================")
        #print("views.py:   "+str(user))
        #print("=========================================")

        user2 = fun_sql_cursor_update(user=user)
        return Response(user2, status=status.HTTP_200_OK)

        
        #if user:
        #    user = fun_sql_cursor_update(user=user)
        #    return Response(user, status=status.HTTP_200_OK)
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    