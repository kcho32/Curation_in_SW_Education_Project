from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Lecture, Category
from .forms import LectureForm
from django.core.exceptions import PermissionDenied


class LectureList(ListView):
    model = Lecture
    paginate_by = 9
    paginate_orphans = 0
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(LectureList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_lecture_count'] = Lecture.objects.filter(category=None).count()
        return context


class LectureDetail(DetailView):
    model = Lecture


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        lecture_list = Lecture.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        lecture_list = Lecture.objects.filter(category=category)
    context = {
        'lecture_list': lecture_list,
        'categories': Category.objects.all(),
        'no_category_lecture_count': Lecture.objects.filter(category=None).count(),
        'category': category,}

    return render(request, 'lecture/lecture_list.html', context)


def lecture_create(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture:index')
    else:
        form = LectureForm()
    context = {'form': form}
    return render(request, 'lecture/lecture_create.html', context)


def lecture_update(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == "POST":
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture:detail', pk=lecture_id)
    else:
        form = LectureForm(instance=lecture)
    context = {'form': form}
    return render(request, 'lecture/lecture_update.html', context)


def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.user.is_staff:
        lecture.delete()
        return redirect('lecture:index')
    else:
        raise PermissionDenied


