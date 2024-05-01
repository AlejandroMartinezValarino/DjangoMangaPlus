from django.http import JsonResponse
from django.shortcuts import render

import secrets

from pymangaplus.client import Client
from pymangaplus.constants import Quality, Language

android_id = secrets.token_bytes(8).hex()
client = Client(Language.SPANISH)
client.register(android_id)


def homepage(request):
    content = client.home()

    manga_lang = request.POST.get('manga_lang', 'SPANISH')

    languages = set()
    infos = []

    try:
        for update in content.get('updates', []):
            for item in update.get('items', []):
                for title in item.get('metadata', {}).get('title', []):
                    language = title.get('language', '')
                    languages.add(language)

        for update in content.get('updates', []):
            filtered_update = {'items': []}
            for item in update.get('items', []):
                filtered_titles = []
                for title in item.get('metadata', {}).get('title', []):
                    language = title.get('language', '')
                    if language == manga_lang:
                        filtered_titles.append(title)
                if filtered_titles:
                    filtered_item = {'metadata': {'title': filtered_titles}}
                    filtered_update['items'].append(filtered_item)
            if filtered_update['items']:
                infos.append(filtered_update)

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
    content = client.manga_viewer(chapter_id, quality=Quality.SUPER_HIGH)

    return render(request, 'manga/read.html', {'pages': content})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)


def error_500_view(request):
    return render(request, '500.html', status=500)
