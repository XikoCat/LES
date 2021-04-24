from django.shortcuts import render

def login_page(request):
    #app_html = 
    #request.user
	return render(request, "utilizadores/login.html", None)
