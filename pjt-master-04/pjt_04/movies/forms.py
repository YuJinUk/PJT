from django import forms
from .models import MovieModel

'''
Django Form VS ModelForm
Form: html 렌더링, 유효성 검사  <- 귀찮다/ django야 대신해줘
ModelForm: 어차피 form 객체 DB와 같이 쓸건데, 필드도 model기반으로 만들어줘.

'''

class MovieForms(forms.ModelForm):
    release_date = forms.CharField(
            widget = forms.TextInput(
                attrs={'type' : 'date'}),
            )
    
    # genre = forms.CharField(
    #     widget = forms.Select(
    #         choices=[('공포','공포'), ('로맨스', '로맨스'),('코미디', '코미디')]
    #     )
    # )
    
    genre = forms.ChoiceField(choices=[('공포','공포'), ('로맨스', '로맨스'),('코미디', '코미디')])
    
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'step' : 0.5,
                   'min' : 0,
                   'max' : 5}
        )
    )
    
    class Meta:
        model = MovieModel # 이 모델 기반으로 Form을 만들어줘
        fields = [
            'title',
            'audience',
            'release_date',
            'genre',
            'score',
            'poster_url',
            'description',
            'actor_image',
            ]  # 모든 필드를 다 받을 것