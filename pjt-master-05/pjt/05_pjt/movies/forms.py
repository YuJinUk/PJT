from django import forms
from .models import MovieModel

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'
        
    # 유효성 검사
    def clean_title(self):
        title = self.cleaned_data['title']
        lst = ['*']
        for i in lst:
            if i in title:
                return
        else:
            return title
    
    def clean_description(self):
        description = self.cleaned_data['description']
        return description