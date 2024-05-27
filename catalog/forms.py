from django.db.models import BooleanField
from django.forms import ModelForm, forms
from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'current_version':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name_product(self):
        cleaned_data = self.cleaned_data['name_product']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово: {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово: {word}')

        return cleaned_data



class ProductModeratorForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category']


class VersionForm(StyleMixin, ModelForm):

    class Meta:
        model = Version
        fields = '__all__'