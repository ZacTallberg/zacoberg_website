from django import forms
from .models import KittenImage, FlowerImage
from .widgets import FileUploadWithPreview, FileUploadOptimizedForm

class PhotoUploadform(FileUploadOptimizedForm):
    image_upload_field='file'

KittenImageModelForm = forms.modelform_factory (
    KittenImage, 
    form=PhotoUploadform,
    exclude=[]
)

class KittenForm(forms.ModelForm):
    # kitten=forms.ImageField(widget=forms.FileInput(attrs={'id' : 'image'}))

    class Meta:
        model=KittenImage
        fields=[
            'description',
            'file',
        ]