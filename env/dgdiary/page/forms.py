from django import forms

from .models import Page

class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = ["highlight","content","photo"]
		widgets = {
			'highlight' : forms.TextInput(attrs={'placeholder':'Highlight of the day...'}),
			'content' : forms.Textarea(attrs={'placeholder':'Tell me more about it...'}),
		}

	def clean_title(self):
		title = self.cleaned_data.get("highlight")
		if len(title) < 5:
			raise forms.ValidationError("Title is too short...")
		else:
			return title

	def clean_content(self):
		content = self.cleaned_data.get("content")
		if len(content) < 50:
			raise forms.ValidationError("So thats all that happened today?")
		else:
			return content