from django.forms import ModelForm
from .models import list, item

class ItemForm(ModelForm):
    class Meta:
        model = item
        fields = ('name',)

class ListForm(ModelForm):
    class Meta:
        model = list
        fields = ('name',)