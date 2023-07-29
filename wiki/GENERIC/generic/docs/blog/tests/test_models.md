## Настройка pytest модели

```python
from blog.models import Post
import pytest


'''
Уроки №2 по настройке pytest

'''

'''Если в pytest исключение выскакивают  не в формате python ,то можно прописать 
pytest --tb=native
'''
@pytest.mark.django_db  #допуск к базе данных
def test_title_create(): #даем такое название чтобы pytest смог найти его,название должно
                         # так начинатся как в настройках было указано

    article = Post.objects.create(title='article1')

    '''Далее пишем сам pytest'''
    assert article.title == 'article1'

```