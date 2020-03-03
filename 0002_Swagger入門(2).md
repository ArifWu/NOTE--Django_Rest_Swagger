# Swagger入門(2)_django-rest-swagger

## 1. 安裝django-rest-swagger

- 安裝
```bash
(base) [cabie@centosclean ~]$ pip install django-rest-swagger
```

- 創建project以及APP
```bash
(base) [cabie@centosclean 003_django_rest_swagger]$ django-admin startproject django_swagger



(base) [cabie@centosclean django_swagger]$ python manage.py startapp swagger_test
(base) [cabie@centosclean django_swagger]$ vim django_swagger/settings.py
```




## 2. 更改 settings.py


- 更改settings.py : 加入 'rest_framework_swagger','swagger_test'
- 並另外增加REST_FRAMEWORK的設定
```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_swagger',
    'swagger_test',
]

...
...
...
...

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

```



## 3. 更改 urls.py

```py
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
]

```



## 4. 版本問題的報錯修改

- [https://stackoverflow.com/questions/55929472/django-templatesyntaxerror-staticfiles-is-not-a-registered-tag-library](https://stackoverflow.com/questions/55929472/django-templatesyntaxerror-staticfiles-is-not-a-registered-tag-library)
- [https://blog.csdn.net/soulwyb/article/details/98476461](https://blog.csdn.net/soulwyb/article/details/98476461)


- 修改template
```bash
(base) [cabie@centosclean django_swagger]$ vim /home/cabie/anaconda3/lib/python3.7/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html

```

- 改成```{% load static %}```
```html
{% load i18n %}
{% load static %}
<!DOCTYPE html>

```

- 若沒有修改，會一直報以下錯誤
```bash

(base) [cabie@centosclean django_swagger]$ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

March 03, 2020 - 06:46:07
Django version 3.0.3, using settings 'django_swagger.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
Internal Server Error: /docs/
Traceback (most recent call last):
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/defaulttags.py", line 1021, in find_library
    return parser.libraries[name]
KeyError: 'staticfiles'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/core/handlers/base.py", line 145, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/core/handlers/base.py", line 143, in _get_response
    response = response.render()
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/rest_framework/response.py", line 70, in rendered_content
    ret = renderer.render(self.data, accepted_media_type, context)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/rest_framework_swagger/renderers.py", line 58, in render
    renderer_context
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/loader.py", line 61, in render_to_string
    template = get_template(template_name, using=using)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/loader.py", line 15, in get_template
    return engine.get_template(template_name)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/backends/django.py", line 34, in get_template
    return Template(self.engine.get_template(template_name), self)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/engine.py", line 143, in get_template
    template, origin = self.find_template(template_name)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/engine.py", line 125, in find_template
    template = loader.get_template(name, skip=skip)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/loaders/base.py", line 30, in get_template
    contents, origin, origin.template_name, self.engine,
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/base.py", line 156, in __init__
    self.nodelist = self.compile_nodelist()
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/base.py", line 194, in compile_nodelist
    return parser.parse()
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/base.py", line 477, in parse
    raise self.error(token, e)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/base.py", line 475, in parse
    compiled_result = compile_func(self, token)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/defaulttags.py", line 1078, in load
    lib = find_library(parser, name)
  File "/home/cabie/anaconda3/lib/python3.7/site-packages/django/template/defaulttags.py", line 1025, in find_library
    name, "\n".join(sorted(parser.libraries)),
django.template.exceptions.TemplateSyntaxError: 'staticfiles' is not a registered tag library. Must be one of:
admin_list
admin_modify
admin_urls
cache
i18n
l10n
log
static
tz
[03/Mar/2020 06:46:11] "GET /docs/ HTTP/1.1" 500 160170

```



## 5. 啟動Django

```bash
(base) [cabie@centosclean django_swagger]$ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

March 03, 2020 - 06:53:44
Django version 3.0.3, using settings 'django_swagger.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

```


- [http://192.168.43.156:8000/docs/](http://192.168.43.156:8000/docs/)

![Imgur](https://i.imgur.com/ZNry9hj.png)

沒看到東西，因為目前還沒有寫API程式。


## 6. 創建API程式


為了方便，我們把之前所做過的drf專案直接複製，然後再用以上做法添加swagger。
drf程式碼Github: [https://github.com/cabie8399/NOTE--Python_Bible/tree/master/09_Web%E9%96%8B%E7%99%BC/Django/002_Django_REST_Framework%E5%85%A5%E9%96%80/drf](https://github.com/cabie8399/NOTE--Python_Bible/tree/master/09_Web%E9%96%8B%E7%99%BC/Django/002_Django_REST_Framework%E5%85%A5%E9%96%80/drf)


將之程式碼clone到本機後，我們就按照上述做法做一次。
然後啟動Django，就可看到以下畫面。


![Imgur](https://i.imgur.com/fETxlmo.png)


## 7. 使用 swagger UI

### 執行畫面

畫面非常漂亮，功能也非常完善，

我們可以在上面執行  **GET**  ,  **POST**  ,  **PUT**  ,  **PATCH**  ,  **DELETE**  , 甚至可以直接看到執行結果。
![Imgur](https://i.imgur.com/jpb8p4R.png)


![Imgur](https://i.imgur.com/XQj3Kin.png)


- 即使用POST也非常好用

![Imgur](https://i.imgur.com/rrXNrsf.png)

![Imgur](https://i.imgur.com/wTIhAcs.png)


