from django import forms
from django.shortcuts import render

class AccessResourses(forms.Form):
	damage = forms.IntegerField(label="Enter the amount of damage to your property from 0-10 (0 being no damage, 10 being fully destroyed)", min_value=0, max_value=10)
# Create your views here.
def index(request):
	return render(request, "form/index.html")

def form(request):
	if request.method == "POST":
		form = AccessResourses(request.POST)
		if form.is_valid():
			damage_mag = form.cleaned_data["damage"]
			# if int(damage_mag) == 0:
			return render(request, "form/response.html", {
				"response": damage_mag
			})
			# elif int(damage_mag) == 1:
			# elif int(damage_mag) == 2:
			# elif int(damage_mag) == 3:
			# elif int(damage_mag) == 4:
			# elif int(damage_mag) == 5:
			# elif int(damage_mag) == 6:
			# elif int(damage_mag) == 7:
			# elif int(damage_mag) == 8:
			# elif int(damage_mag) == 9:
			# elif int(damage_mag) == 10:

		else:
			return render(request, "form/form.html", {
				"form": form
			})


	return render(request, "form/form.html", {
		"form": AccessResourses()
		})



  