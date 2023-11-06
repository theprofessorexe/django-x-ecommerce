from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from PIL import Image
# Create your models here.


class BlogCategory(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    category_slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=300, unique=True)
    blog_slug = models.SlugField(max_length=300, unique=True)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to="Blog")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"


    def __str__(self):
        return self.title

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['blog_image'].label = "Blog Image"
        self.fields['blog_image'].help_text = "Image upload requirements: JPEG, JPG or PNG format, with dimensions of 370 x 266 pixels and a maximum file size of 2MB."

    def clean_blog_image(self):
        image = self.cleaned_data.get('blog_image')

        if image:
            # Check image dimensions
            img = Image.open(image)
            width, height = img.size

            if width != 370 or height != 266:
                raise ValidationError("Please upload an image with dimensions 370x266 pixels.", code="invalid_size")
            

        return image        
            


