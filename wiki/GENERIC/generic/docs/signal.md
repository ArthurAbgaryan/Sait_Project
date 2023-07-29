## Вариант прописание сигналов

Расмотрим сигнал pre_save сигнал который дается до сохранения объект,в нашем случае это
будет автозаполнение slug по полю title, в форме добавления статьи

Вариант №1(урок 10)

```python

from django.utils.text import slugify #импорт slugify из самого джанго
#from pytils.translit import slugify #импорт slugify со сторонней библиотеки,
                                        # здесь обрабатывается кирилица

def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)


```
    
Вариант №2 с помощью декоратора (урок 14-15)

```python

from pytils.translit import slugify

@receiver(pre_save,sender=Post) 
def prepopulated_slug(sender,instance,**kwargs):
    instance.slug=slugify(instance.title)

```

В декораторе указывается вид сигнала (pre_save) и модель (Post) с которой будем работать декоратор

instance- это фактический сохраняемый экземпляр класса прописанный в параметрах


Внимание!!! Если поле по которому заполняется slug написана кирилицей и она автоматически
не заполняется , тогда slugify нужно импортировать из pytils

```python

from pytils.translit import slugify

```

или же в случае если не работает библиотека pytils прописать код для 
перевода латиницы на кирилицу самому, и этот код разместить в начало модели

Пример:

```python

from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):

    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))

```