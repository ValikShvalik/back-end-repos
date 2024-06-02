from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Account, Respondent, Questioner, Form, Survey, Hobby
from .forms import AccountForm, RespondentForm, QuestionerForm, FormForm, SurveyForm, HobbyForm
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Перенаправление после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправление после успешного входа
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Create your views here.


def account_list(request):
    accounts = Account.objects.all
    return render(request, 'account_list.html', {'accounts': accounts})


def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'account_detail.html', {'account': account})


def account_create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return redirect('account_detail', pk=account.pk)
    else:
        form = AccountForm()
    return render(request, 'account_form.html', {'form': form})


def account_edit(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect('account_detail', pk=account.pk)
    else:
        form = AccountForm(instance=account)
    return render(request, 'account_form.html', {'form': form})


def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        account.delete()
        return redirect('account_list')
    return render(request, 'account_confirm_delete.html', {'account': account})


def survey_list(request):
    surveys = Survey.objects.all()
    data = {'surveys': list(surveys.values())}
    return JsonResponse(data)


def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    data = {
        'id': survey.id,
        'form_id': survey.form.id,
        'respondent_id': survey.respondent.id,
        'result': survey.result,
        'creation_time': survey.creation_time.strftime('%H:%M:%S')
    }
    return JsonResponse(data)
