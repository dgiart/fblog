from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    # title=forms.CharField(max_length=50)
    # slug=forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class':'form-control'})
    # slug.widget.attrs.update({'class':'form-control'})
    class Meta:
        model=Tag
        fields=['title','slug']
        widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'slug':forms.TextInput(attrs={'class':'form-control'}),
        }


    def clean_slug(self):
        new_slug=self.cleaned_data['slug'].lower()
        if new_slug =='create':
            # print ('Slug can not be CREATE')
            raise ValidationError('Slug can not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug MUST BE UNIQUE')
        return new_slug

    # def save(self):
    #     new_tag=Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #         )
    #     return new_tag

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','slug','body','tags']
        widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'slug':forms.TextInput(attrs={'class':'form-control'}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
        'tags':forms.SelectMultiple(attrs={'class':'form-control'})
        }
    def clean_slug(self):
        new_slug=self.cleaned_data['slug'].lower()
        if new_slug =='create':
            # print ('Slug can not be CREATE')
            raise ValidationError('Slug can not be CREATE')

        return new_slug
