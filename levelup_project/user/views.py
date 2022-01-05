from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from user.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from user.models import User
from django.utils import timezone

@csrf_exempt
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        return render(request, 'user/user_list.html', {'user_list':user})
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer._errors, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            request.session['user_id'] = User.objects.all().get(user_name=user_name).id
            print(request.session['user_id'])
            return render(request, 'user/success.html')
        except:
            return render(request, 'user/fail.html')

    elif request.method == 'GET':
        return render(request, 'user/login.html')