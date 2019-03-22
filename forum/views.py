from django.shortcuts import render

def home(request):
	postes = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo',
'violet']
	cats = ['TECHNO', 'POLITIQUE', 'GAMING', 'DROLE', 'BRICOLAGE', 'DEV']

	return render(request,'forum/home.html', locals())

def postesOfCategorie(request, catID):
	return render('categories.html')

def login(request):
	return render(request,'forum/login.html')

def register(request):
	return render(request,'forum/register.html')

