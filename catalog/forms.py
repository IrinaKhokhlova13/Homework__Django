from django.db.models import BooleanField
from django.forms import ModelForm, forms
from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['name_product']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise ModelForm.ValidationError(f'Недопустимое слово: {word}')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['description']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise ModelForm.ValidationError(f'Недопустимое слово: {word}')

        return cleaned_data



class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category']


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("is_active_version",)