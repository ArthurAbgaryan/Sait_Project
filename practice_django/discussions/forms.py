from django.forms import ModelForm
from discussions.models import Discussion

class DiscussionCreateForm(ModelForm):

    class Meta:
        model = Discussion
        fields = ['title','content']

