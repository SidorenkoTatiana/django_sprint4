from django import forms
from .models import Post, Category, Location, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'location', 'category', 'is_published', 'image']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
