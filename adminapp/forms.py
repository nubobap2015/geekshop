from django import forms

from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductsCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = "__all__"


class ProductCategoryEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = ProductsCategory
        fields = "__all__"