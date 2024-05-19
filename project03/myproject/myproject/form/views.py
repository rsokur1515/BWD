from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from form.forms import TaskForm
from form.models import Task

def main_page(request):
    template = 'main.html'
    context = {
        'my': {
            'name': 'Сокуров Рустам Астемирович',
            'phone': '89255950551',
            'mail': 'rasokurov@edu.hse.ru',
            'imgurl': 'https://sun9-27.userapi.com/impg/rxzeWj57hir5eFNSpMfZA6jimyLhKUdXRf1CSw/MrPfNFQOxiI.jpg?size=1280x848&quality=95&sign=641c82c821b7d52bf6197d57a72de368&type=album'
        },
        'program': {
            'name': 'Экономика',
            'description': 'Программа «Экономика» НИУ ВШЭ позволяет получить диплом бакалавра в ведущем российском вузе, выпускников которого охотно принимают на работу крупнейшие российские и международные компании, в государственные организации, в исследовательские центры и ведущие университеты. Программа включает в себя глубокое освоение экономической теории, методов математического анализа, статистики, эконометрики, способов обработки информации, программирования и изучение иностранных языков,  а также курсы прикладных финансовых и экономических дисциплин и научно-проектную работу.Во время обучения студенты проходят стажировку в ведущих российских и международных компаниях, получают возможность обучаться в лучших европейских университетах-партнерах ВШЭ. После получения степени бакалавра студент имеет возможность продолжить обучение в магистратуре и докторантуре ведущих мировых университетов.',
            'ruk': {
                'name': 'Кирилл Александрович Букин',
                'mail': 'kabukin@hse.ru',
                'imgurl' :'https://www.hse.ru/pubs/share/thumb/187225977:c2103x2103+50+0:r380x380!.jpg'
            },
            'man': {
                'name': 'Макарова Галина Викторовна',
                'mail': 'gvmakarova@hse.ru',
                'imgurl' :'https://www.hse.ru/pubs/share/thumb/223562260:c527x527+93+0:r380x380!.jpg'
            }
        },
        'pal1': {
            'name': 'Родионов Илья Владимирович',
            'phone': '89031627045',
            'mail': 'ivrodionov@edu.hse.ru',
            'imgurl': 'https://sun9-22.userapi.com/impg/1TLORGT9bS0p46wBmpR-bhYbcdMGuipu-cWJxA/-w40uUjbDzA.jpg?size=2560x1957&quality=96&sign=1cc6eb39f90f269b3c2db736e8bf95ae&type=album'
        },
        'pal2': {
            'name': 'Янковская Анна Михайловна',
            'phone': '88005553535',
            'mail': 'amyankovskaya@edu.hse.ru',
            'imgurl': 'https://sun9-35.userapi.com/impg/6sw0tXdtjgHmYBOhOSgB35UTS21oeRaT1eRbGw/Fo4CJFFxQKs.jpg?size=1440x2160&quality=95&sign=f720de3ad630ebd60fac64d98714e75d&type=album'
        },
    }
    return render(request, template, context)

def form(request):
    template = 'form.html'
    context = {}
    form = TaskForm(request.POST)
    if form.is_valid():
        Task.objects.create(**form.cleaned_data)
        return redirect('form:task_answer')

    context['form'] = form
    return render(request=request, template_name=template, context=context)

def task_answer(request):
    object_list = Task.objects.all().order_by('-id')
    last_object = object_list.values('name', 'surname', 'seat')[0]
    seat = last_object['seat']
    if seat > 36:
        phrase = 'Ваше место - боковое.'
    elif seat % 2:
        phrase = 'Ваше место в купе внизу.'
    else:
        phrase = 'Ваше место в купе наверху.'

    template = 'answer.html'

    context = {}
    context['name'] = last_object['name']
    context['surname'] = last_object['surname']
    context['seat'] = seat
    context['phrase'] = phrase

    return render(request, template, context)


def data(request):
    context = {}
    info = Task.objects.all()
    context['info'] = info
    template = 'data.html'
    return render(request=request, template_name=template, context=context)

def table(request):

    template = 'table.html'

    objects_values = Task.objects.values()
    objects_values_list = (
    Task.objects.values_list().filter(id__gt=4).order_by('-id')
)
    cur_objects = objects_values_list
    statics_val=[
        cur_objects.aggregate(Count("seat")),
        cur_objects.aggregate(Avg("seat")),
        cur_objects.aggregate(Min("seat")),
        cur_objects.aggregate(Max("seat")),
        cur_objects.aggregate(StdDev("seat")),
        cur_objects.aggregate(Sum("seat")),
    ] 

    statics = {'statics_val': statics_val}
    fields = Task._meta.get_fields()
    name_list = []

    for e in fields:
        name_list.append(e.name)

    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "statics": statics,
    }

    return render(request, template, context)