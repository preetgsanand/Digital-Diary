from django import forms

from .models import Status

class StatusForm(forms.ModelForm):
	class Meta:
		model = Status
		fields = ["content","username"]

	def clean_content(self):
		content = self.cleaned_data.get("content")
		if len(content) < 5:
			raise forms.ValidationError("Content Too Short...")
		else:
			return content