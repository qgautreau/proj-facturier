from django.forms import ModelForm, TextInput
from models import Profile


class UpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "skills": TextInput(attrs={"data-role":"tagsinput"})
        }
