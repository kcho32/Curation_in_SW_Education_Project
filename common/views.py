from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from typing import Any, Dict
from .forms import UserForm, StaffForm
from .models import CustomUser as User
from .models import CustomerMessage, NewsAgreedCustomer
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from lecture.models import Lecture, Category
from functools import reduce
from operator import and_
import ast
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def signup(request):
    if request.method == 'POST':  # request 들어온 것이 post방식이면
        if request.POST['teacher_code'] in ['A0001', 'A0002']:
            form = StaffForm(request.POST)
        else:
            form = UserForm(request.POST)  # form에 UserForm post version으로 저장한다
        if form.is_valid():  # form이 valid하면
            form.save()
            return redirect('../login')
    else:
        form = UserForm()  # 계정 생성 화면 리턴
    return render(request, './common/signup.html', {'form': form})


def find_id(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            context = {'username': user.username}
            return render(request, './common/find_id.html', context)
        except ObjectDoesNotExist:
            context = {'username': "None"}
            return render(request, './common/find_id.html', context)

    else:
        return render(request, './common/find_id.html')


def find_pw(request):
    if request.method == "POST":
        try:
            user = User.objects.get(
                username=request.POST['username'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            return redirect('common:verify', pk=user.pk)
        except ObjectDoesNotExist:
            context = {'error_message': '입력하신 정보를 확인해주세요'}
            return render(request, './common/verify.html', context)
    else:
        return render(request, './common/find_pw.html')


def verify(request, pk):
    if request.method == 'POST':
        return redirect('common:reset_pw', pk)
    else:
        user = User.objects.get(pk=pk)
        question = user.self_prove
        answer = user.self_prove_answer
        context = {
            'question': question,
            'answer': answer,
            'pk': pk
        }
        return render(request, './common/verify.html', context)


def reset_pw(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 == password2:
            user.set_password(password1)
            user.save()
            return redirect('common:login')
        else:
            return render(request, '/', context)

    else:
        user = User.objects.get(pk=pk)
        username = user.username
        email = user.email
        context = {
            'username': username,
            'email': email,
            'pk': pk
        }
        return render(request, './common/reset_pw.html', context)


def searched_lecture(request):
    if request.method == 'POST':
        categories = Category.objects.all()
        term_list = request.POST['term_list']
        sub_term = request.POST['sub_term']
        if len(term_list) < 1:
            term_list = []
        else:
            term_list = ast.literal_eval(term_list)
        term_list.append(sub_term)
        term_list = list(set(term_list))  # 중복 단어 삭제
        lecture_list = reduce(and_, (Lecture.objects.filter(class_name__icontains=term)
                                     | Lecture.objects.filter(subject__icontains=term)
                                     | Lecture.objects.filter(level__icontains=term)
                                     | Lecture.objects.filter(content__icontains=term) for term in term_list))
        context = {'lecture_list': lecture_list, 'term_list': term_list, 'categories': categories}
        return render(request, './common/searched_lecture.html', context)
    else:
        categories = Category.objects.all()
        term_list = [request.GET['searching']]
        print(term_list, type(term_list))
        lecture_list = reduce(and_, (Lecture.objects.filter(class_name__icontains=term)
                                     | Lecture.objects.filter(subject__icontains=term)
                                     | Lecture.objects.filter(level__icontains=term)
                                     | Lecture.objects.filter(content__icontains=term) for term in term_list))
        context = {'lecture_list': lecture_list, 'term_list': term_list, 'categories': categories}
        return render(request, './common/searched_lecture.html', context)


def customer_message(request):
    message = CustomerMessage(
        name=request.POST['name'],
        email=request.POST['email'],
        subject=request.POST['subject'],
        message=request.POST['message']
    )
    message.save()
    return redirect('/#contact')


def subscribe(request):
    if request.method == "POST":
        subscribe_email = NewsAgreedCustomer(
            email=request.POST['email']
        )
        subscribe_email.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
