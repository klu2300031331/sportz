from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'venue', 'available_seats', 'description']
        widgets = {
            'date': forms.SelectDateWidget(years=range(2024, 2031)),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def clean_available_seats(self):
        available_seats = self.cleaned_data.get('available_seats')
        if available_seats <= 0:
            raise forms.ValidationError("Available seats must be a positive number.")
        return available_seats
