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

        fields = ['text']
        #fields-list tells Django what fields to include.

        labels = {'text': ''}
        #The labels dictionary what to label the fields.
        # We'll leave it empty because it looks clean.