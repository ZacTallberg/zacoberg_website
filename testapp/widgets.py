import base64
from django import forms
from django.core.files.base import ContentFile

class FileUploadWithPreview(forms.widgets.ClearableFileInput):
    template_name = "widgets/file_upload.html"


class FileUploadOptimizedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FileUploadOptimizedForm, self).__init__(*args, **kwargs)
        self.hidden_image_field_name = "{}_image_data".format(self.image_upload_field)
        self.fields[self.hidden_image_field_name] = forms.CharField(widget=forms.HiddenInput, required=False)
        self.fields[self.image_upload_field].widget = FileUploadWithPreview()
        self.fields[self.image_upload_field].required = False

    def clean(self, *args, **kwargs):
        data = super(FileUploadOptimizedForm, self).clean(*args, **kwargs)
        image_data = data.get(self.hidden_image_field_name)

        if image_data:
            format, image_string = image_data.split(";base64,")
            extension = format.split("/")[-1]
            file = ContentFile(base64.b64decode(image_string), name="temp." + extension)
            file_name = "image." + extension
            image_field = getattr(self.instance, self.image_upload_field)
            image_field.save(file_name, file)

            data[self.image_upload_field] = image_field
            data[self.hidden_image_field_name] = ""

        return data