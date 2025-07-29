# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.db.models import Q

# def home(request):
#     users = User.objects.all()
#     return render(request, 'home/index.html', {'users': users})

# def search(request):
#     query = request.GET.get('query')
#     users = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)) 
    
#     return render(request, 'home/search.html', {
#         'users': users,
#         'query': query
#     })