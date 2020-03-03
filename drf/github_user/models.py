from django.db import models


# Executing custom SQL directly使用的model
from collections import namedtuple
from django.db import connection




# Create your models here.

# 這裡我們設定Github User的Schema
class Github(models.Model):
    user = models.TextField()
    location = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True) #auto_now=Ture（在每次保存模型時將該字段設置為當前日期）
    created = models.DateTimeField(auto_now_add=True) #auto_now_add（僅設置模型首次創建時的日期）
    
    class Meta:
        db_table = "github_user"
        
        
        
        
#  Performing raw queries        
def fun_raw_sql_query(**kwargs):
    user = kwargs.get('user')
    if user:
        result = Github.objects.raw('SELECT * FROM github_user WHERE user = %s', [user])
    else:
        result = Github.objects.raw('SELECT * FROM github_user')
    return result








# Executing custom SQL directly

def namedtuplefetchall(cursor):
    # Return all rows from a cursor as a namedtuplet
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def fun_sql_cursor_update(**kwargs):
    user = kwargs.get('user')
    #print("=========================================")
    #print("models.py ===>  user")
    #print("=========================================")
    #pk = kwargs.get('pk')

    '''
    Note that if you want to include literal percent signs in the query,
    you have to double them in the case you are passing parameters:
    '''
    with connection.cursor() as cursor:
        #cursor.execute("UPDATE music SET user = %s WHERE id = %s", [user, pk])
        #cursor.execute("SELECT * FROM github_user WHERE id = %s", [pk])
        
        cursor.execute("SELECT * FROM github_user WHERE user = %s", [user])
        # result = cursor.fetchone()
        result = namedtuplefetchall(cursor)
    result = [
        {
            'id': r.id,
            'user': r.user,
            'location': r.location,
            'last_modify_date': r.last_modify_date,
            'created': r.created,
        }
        for r in result
    ]

    return result
