##Настройка django-crispy-forms
pip install django-crispy-forms==2.0

[django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

Уст-ка пакета шаблонов по умолчанию, в самый конец settings.py
так же вместо пакета uni-form может быть bootstrap,или одновременно вместе:

```python
CRISPY_TEMPLATE_PACK = 'uni_form'
```

=====================================================================================

##Настройка django-cleanup

pip install  django-cleanup==7.0.0

[django-cleanup](https://github.com/un1t/django-cleanup) отвечает за удаление ненужных файлов

Для активации билиотеки добавляется в  INSTALED_APP:

```python
'django_cleanup.apps.CleanupConfig' # -добав-ся в INSTALED_APP всегда в самом конце 
```

=====================================================================================


pip install Pillow==9.5.0

=====================================================================================

##Настройка django-ckeditor

pip install django-ckeditor==6.3.2

[django-ckeditor](https://pypi.org/project/django-ckeditor/)

INSTALED_APP добавить:

```python
  'ckeditor',
```

В самом конце settings.py добавить:

```python
#django-ckeditor

CKEDITOR_CONFIGS = {
    'default': {
        'width':'auto',
    },
}

#End django-ckeditor
```

=====================================================================================

##Настройка channels(для очень быстрой работы ассинхронных приложений)

python -m pip install -U channels
#https://channels.readthedocs.io/en/stable/installation.html

settings.py:

```python

'''
ASGI_APPLICATION = "practice_django.routing.application" #1-ая перем название проекта,
                                    #2-ая routing создается одноиме-ый файл routing.py

CHANNEL_LAYERS = {
    "default":{
        "BACKEND":"channels.layers.InMemoryChannelLayer"
    },
}
'''


```

routing.py:

```python

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#import chat.routing #закаментированной т.к. еше не создан чат


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            #chat.routing.websocket_urlpatterns
        )
    ),
})

```

в INSTALED_APP добавим channels:

```python

INSTALLED_APPS = [

     ..................
     
     'django.contrib.sites',
    'django.contrib.staticfiles',
     "debug_toolbar",
      #'channels',

     ................

]

```

======================================================================================

##Настройка django-allauth

pip install django-allauth==0.54.0

[django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

В INSTALLED_APP после messages:

```python

'django.contrib.sites',

```

и чтобы это сработала ,ниже в settings нужно добавить :

```python

SITE_ID=1

```

Затем в INSTALLED_APP добавляем социальные провайдеры, их можно добавлять сколько угодно:

```python

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',


```
Далее запускаются python manage.py migrate и python manage.py collectstatic

Размещаем в settings.py , не важно где:

```python

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]

```


Так же добавляем поле социальные провайдеры, прямо после предыдущей настройки AUTHENTICATION_BACKENDS:

```python

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}


```

urls.py:

```python
 path('accounts/', include('allauth.urls')),
```



=====================================================================================


##Настройка django-debug-toolbar

python -m pip install django-debug-toolbar-3.8.1

[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

Добавить в любое место:

```python

INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
]

```

Добавляем в промежуточный слой:

```python

MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]

```

Настройка отслеживания IP, добавляется в самое начало settings.py:

```python

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

```

Добавляем в urls.py:

```python

from django.urls import include, path

urlpatterns = [
    # ...
    path("__debug__/", include("debug_toolbar.urls")),
]

```
 Или вместо предыдущего примера сделать так(добавиться меню):

```python

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

```

=====================================================================================


##Настройка dotenv

pip install python-dotenv==0.21.1

[dotenv](https://pypi.org/project/python-dotenv/)

Как использовать (переопределим SECRET_KEY в SETTINGS.PY):

1.1.В SETTINS прописывается данный код для сопоставления ключей(SECRET_KEY):
```python

from pathlib import Path
import os
from dotenv import load_dotenv


# Loading ENV 
env_path=Path('.')/'.file.env'

# env_path='.test.env'

load_dotenv(dotenv_path=env_path)
```
1.2. В корневой папке проекта создается файл .file.env 

1.3. в этом файле прописывается SECRET_KEY 

=====================================================================================


pip install django-braces==1.15.0
#https://django-braces.readthedocs.io/en/latest/

pip install mkdocs
#https://www.mkdocs.org/


pip install mkdocs-awesome-pages-plugin
#https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin


pip install mkdocs-material
#https://squidfunk.github.io/mkdocs-material/getting-started/


pip install notebook
#https://jupyter.org/install


================================================================================================

##Настройка django-extensions

pip install django-extensions

[django-extensions](https://django-extensions.readthedocs.io/en/latest/)

в setings.py:

```python

INSTALLED_APPS = (
    ...
    'django_extensions',
)


```


================================================================================================

##Настройка django-taggit

[django-taggit](https://django-taggit.readthedocs.io/en/latest/getting_started.html)

pip install django-taggit

================================================================================================

## Настройка pytest-django

[pytest-django](https://pytest-django.readthedocs.io/en/latest/tutorial.html#step-1-installation)

pip install pytest-django

Для импортировани модуля в терминале прописываем:

set DJANGO_SETTINGS_MODULE=test.settings

После ввода выше перечисленных команда ,в теминале вводим pytest

Далее в файле pytest.ini(который нужно создать в корневой папке practice_django) прописываем:

```python

[pytest]
DJANGO_SETTINGS_MODULE=practice_django.settings
python_files = tests.py test_*.py *_tests.py

```

DJANGO_SETTINGS_MODULE=practice_django.settings-указ-ся путь настройки
python_files = tests.py test_*.py *_tests.py -допустимые имена тестового файла

Далее два пути,если будем тестировать приложение по частям то создаем папку tests в нашем приложении
и в папке tests создаем файл test_models.py и там же обязательно создать файл __init__.py
иначе не будет распозновать пакеты

================================================================================================

## Pylint библиотека настраивающая и корректирующая код ,не запуская его

pip install pylint 