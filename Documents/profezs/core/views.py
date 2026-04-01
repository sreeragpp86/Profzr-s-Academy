from .chapters_data import SYLLABUS  # This is the data file you created
from django.shortcuts import render
from .chapters_data import SYLLABUS  # Import the data we just made


def material_list(request, category):
    subject_slug = request.GET.get('subject', 'all')
    raw_chapters = SYLLABUS.get(category, {}).get(subject_slug, [])

    clean_chapters = []
    for ch in raw_chapters:
        # This forces the URL to be /media/... and ensures it ends in .pdf
        # It also removes any accidental project names like 'Profzrs' from the path
        url = ch['file_url']
        
        # Ensure it starts with /media/
        if not url.startswith('/media/'):
            # If it starts with media/ (no slash), add the slash
            if url.startswith('media/'):
                url = '/' + url
            # If it doesn't have media at all, add it
            else:
                url = '/media/' + url.lstrip('/')

        # Fix the .htm vs .pdf issue automatically
        if url.endswith('.htm'):
            url = url.replace('.htm', '.pdf')

        clean_chapters.append({
            'id': ch['id'],
            'name': ch['name'],
            'file_url': url
        })

    context = {
        'chapters': subject_chapters,  # This name MUST match the template loop
        'display_subject': subject.replace('_', ' '),
        'display_category': category.upper(),
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
