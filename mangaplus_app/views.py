from django.shortcuts import render

import secrets

from pymangaplus.client import Client
from pymangaplus.constants import Quality, Language

android_id = secrets.token_bytes(8).hex()
client = Client(Language.SPANISH)
client.register(android_id)


def homepage(request):
    content = client.free_titles()

    manga_id = request.POST.get('manga_id')

    info = client.title_detail(manga_id) if manga_id else None

    return render(request, 'manga/list.html', {'mangas': content, 'info': info})


def title_detail(request, title_id):
    content = client.title_detail(title_id)

    return render(request, 'manga/title.html', {'chapters': content})


def manga_detail(request, chapter_id):
    content = client.manga_viewer(chapter_id, quality=Quality.SUPER_HIGH)

    return render(request, 'manga/read.html', {'pages': content})
