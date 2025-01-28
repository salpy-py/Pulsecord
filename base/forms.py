from django.forms import ModelForm
from .models import Room

# RoomForm: A Django ModelForm for creating and updating Room instances
class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Specifies the model this form is based on (Room model)

        fields = '__all__'
        # Includes all fields from the Room model in the form

        exclude = ['host', 'participants']
        # Excludes the 'host' and 'participants' fields from the form
        # 'host' will be assigned programmatically to the logged-in user
        # 'participants' are managed through other views or actions
