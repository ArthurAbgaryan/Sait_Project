# -*- coding: utf-8 -*-
from blog.models import Post
import pytest

@pytest.mark.django_db
def test_title_create():
    article = Post.objects.create(title='article1',content='Text_article1',slug='article1')

    assert article.title == 'article1'
    assert article.content == 'Text_article1'
    assert article.slug == 'article1'
