from django import forms
from .models import Order, Feedback

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["quantity"].widget.attrs.update({'placeholder': 'Quantity'})


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
    
  