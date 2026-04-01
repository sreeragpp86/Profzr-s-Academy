from .chapters_data import SYLLABUS  # This is the data file you created
from django.shortcuts import render
from .chapters_data import SYLLABUS  # Import the data we just made


def material_list(request, category):
    subject_slug = request.GET.get('subject', 'all')

    # Fetch the chapters for the specific class and subject
    # .get() prevents the app from crashing if a subject isn't found
    chapters = SYLLABUS.get(category, {}).get(subject_slug, [])

    context = {
        'category': category,
        'subject': subject_slug,
        'display_category': category.replace('-', ' ').upper(),
        'display_subject': subject_slug.replace('-', ' ').title(),
        'chapters': chapters,
    }
    return render(request, 'material_list.html', context)


def index(request):
    return render(request, 'index.html')


def sslc_subjects(request):
    return render(request, 'sslc_subjects.html')


def plus_one_subjects(request):
    return render(request, 'plus_one_subjects.html')


def plus_two_subjects(request):
    return render(request, 'plus_two_subjects.html')


def material_list(request, category):
    return render(request, 'material_list.html', {'category': category})


# core/views.py


def material_list(request, category):
    subject_slug = request.GET.get('subject', 'all')

    # Get the list of chapters for this specific category and subject
    chapters = SYLLABUS.get(category, {}).get(subject_slug, [])

    context = {
        'category': category,
        'subject': subject_slug,
        # 'plus-one' -> 'PLUS ONE'
        'display_category': category.replace('-', ' ').upper(),
        # 'computer-science' -> 'Computer Science'
        'display_subject': subject_slug.replace('-', ' ').title(),
        'chapters': chapters,
    }
    return render(request, 'material_list.html', context)
