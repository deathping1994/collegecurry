from django import forms

CATEGORIES_CHOICES = (
    ("0", "Select the category"),
    ("Academics", "Academics"),
    ("Sports", "Sports"),
)

class ReviewForm(forms.Form):
    authorName = forms.CharField(label="Author Name", max_length=50)
    authorEmail = forms.EmailField(label="Author Email", max_length=50)
    authorYear = forms.IntegerField(label="Author Year")
    category = forms.ChoiceField(choices=CATEGORIES_CHOICES)
    authorCourse = forms.CharField(label="Author Course", max_length=100)
    marks = forms.FloatField(label = "Marks")
    review = forms.CharField(widget=forms.Textarea)
