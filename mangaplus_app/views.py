import uuid

from django.http import JsonResponse
from django.shortcuts import render

from mangaplus.constants import Language, Viewer, Quality
from mangaplus.shueisha import MangaPlus

device_id = str(uuid.uuid4())
client = MangaPlus(lang=Language.SPANISH, viewer=Viewer.VERTICAL)
client.register(device_id)


def homepage(request):
    content = client.home()

    manga_lang = request.POST.get('manga_lang', 'SPANISH')

    languages = set()
    infos = []

    try:
        home_view = content.get('homeViewV3', {})
        groups = home_view.get('groups', [])

        for group in groups:
            for title_group in group.get('titleGroups', []):
                for title_info in title_group.get('titles', []):
                    language = title_info.get('title', {}).get('language', '')
                    languages.add(language)

        for group in groups:
            filtered_group = {'titleGroups': []}
            for title_group in group.get('titleGroups', []):
                filtered_titles = []
                for title_info in title_group.get('titles', []):
                    language = title_info.get('title', {}).get('language', '')
                    if language == manga_lang:
                        filtered_titles.append(title_info)
                if filtered_titles:
                    filtered_title_group = {'titles': filtered_titles}
                    filtered_group['titleGroups'].append(filtered_title_group)
            if filtered_group['titleGroups']:
                infos.append(filtered_group)

    except Exception as e:
        print(f"Error: {e}")

    return render(request, 'manga/list.html', {'lenguas': languages, 'infos': infos})


def manga_overview(request, title_id):
    title_detail = client.title_detail(title_id)
    overview = title_detail.get('overview', '')
    return JsonResponse({'overview': overview})


def title_detail(request, title_id):
    content = client.title_detail(title_id)

    return render(request, 'manga/title.html', {'chapters': content})


def manga_detail(request, chapter_id):
    content = client.manga_viewer(chapter_id=chapter_id, split=False, quality=Quality.SUPER_HIGH)

    return render(request, 'manga/read.html', {'pages': content})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)


def error_500_view(request):
    return render(request, '500.html', status=500)
