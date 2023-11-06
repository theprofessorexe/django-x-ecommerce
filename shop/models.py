from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from PIL import Image


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)
    category_slug = models.SlugField(max_length=200, unique=True)
    category_description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to="Category")


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'  # You can specify specific fields if needed

    # You can define custom labels or help text for fields
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        # Add a custom label or help text for the category_image field
        self.fields['category_image'].label = 'Category Image'
        self.fields['category_image'].help_text = "Image upload requirements: JPEG, JPG or PNG format, with dimensions of 270 x 270 pixels and a maximum file size of 2MB."

        # You can customize labels and help text for other fields as well
    def clean_category_image(self):
        image = self.cleaned_data.get('category_image')

        if image:
            # Check image dimensions
            img = Image.open(image)
            width, height = img.size

            if width != 270 or height != 270:
                raise ValidationError("Please upload an image with dimensions 270x270 pixels.", code="invalid_size")

        return image

    


class Product(models.Model):
    DROPDOWN = [
        ('kg', 'Kilogram'),
        ('lbs', 'Lbs'),
        ('piece', 'Piece'),
    ]

    product_name = models.CharField(max_length=200, unique=True)
    product_slug = models.SlugField(max_length=200, unique=True)
    product_price = models.PositiveIntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = models.TextField(blank=True, default=None)
    stock_quantity = models.PositiveBigIntegerField()
    product_image = models.ImageField(upload_to="Products")
    stock_unit = models.CharField(max_length=50, choices=DROPDOWN, default='piece')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # You can specify specific fields if needed

    # You can define custom labels or help text for fields
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Add a custom label or help text for the category_image field
        self.fields['product_image'].label = 'Product Image'
        self.fields['product_image'].help_text = "Image upload requirements: JPEG, JPG or PNG format, with dimensions of 270 x 270 pixels and a maximum file size of 2MB."

        # You can customize labels and help text for other fields as well
    def clean_product_image(self):
        image = self.cleaned_data.get('product_image')

        if image:
            # Check image dimensions
            img = Image.open(image)
            width, height = img.size

            if width != 270 or height != 270:
                raise ValidationError("Please upload an image with dimensions 270x270 pixels.", code="invalid_size")

        return image
