from django import forms
#First we import this forms module, which is needed when working with and creating forms.

from .models import Topic, Entry
#We'll also need to import our models we want to work with. 

class TopicForm(forms.ModelForm):
    #Here, we create our first form using ModelForm.
    class Meta:
        #The simplest version of a ModelForm consists of a nested Meta class like this.
        
        model = Topic
        #model tells Django what model to base the form on.

        fields = ['text', 'public']
        #fields-list tells Django what fields to include.

        labels = {'text': '', 'public': 'Public'}
        #The labels dictionary what to label the fields.
        # We'll leave it empty because it looks clean.


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        #The new thing in this ModelForm is the widgets attribute.
        # A widget is basically an HTML form element, 
        #  such as a single-line text box, a multi-line textarea or a drop down list.
        #   By including this widgets attribute, we can override Django's default widget choices.
        #    We tell Django to use a forms.Textarea element, 
        #     and customize its attrbibutes and set the width to 80 columns instead of 40 which is default.
        #      This gives the user more room to enter meaningful entries.