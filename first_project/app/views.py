from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f"Текущее время: {current_time} <br> <a href={reverse('home')}>На главную</a>"
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    workdir = []
    for root, dirs, files in os.walk("."):
        for dir in dirs:
            dir_1 = ('Каталог:' + os.path.join(root, dir))
            workdir.append(dir_1 + f'<br>')
        for filename in files:
            file = ('Файл:' + os.path.join(root, filename))
            workdir.append(file + f'<br>')
    workdirs = f"{workdir}<br><a href={reverse('home')}> На главную</a>"
    return HttpResponse(workdirs)
