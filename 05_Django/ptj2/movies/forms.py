from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='영화제목',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'영화제목',
            }
        )
    )
    description = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class':'description',
                'placeholder':'줄거리',
                'rows':5,
                'cols':30,
            }
        )
    )
    poster = forms.CharField(
    label="이미지",
    widget=forms.Textarea(
        attrs={
            'class':'poster',
            'placeholder':'리미지',
            'rows':1,
            'cols':50,
            }
        )
    )

    class Meta:
        model = Movie
        fields = ('title',)

# class RatingForm(forms.ModelForm):
#     content = forms.CharField(
#         label="이미지",
#         widget=forms.Textarea(
#             attrs={
#                 'class':'poster',
#                 'placeholder':'리미지',
#                 'rows':1,
#                 'cols':50,
#             }
#         )
#     )
#     class Meta:
#         model = Rating
#         fields =
