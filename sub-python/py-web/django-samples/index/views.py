import json

from django.apps import apps
from django.shortcuts import render
from django import urls


def get_all_url(resolver=None, pre='/'):
    if resolver is None:
        resolver = urls.get_resolver()
    for r in resolver.url_patterns:
        if isinstance(r, urls.URLPattern):
            if '<pk>' in str(r.pattern):
                continue
            yield pre + str(r.pattern).replace('^', '').replace('$', ''), r.name
        if isinstance(r, urls.URLResolver):
            yield from get_all_url(r, pre + str(r.pattern))


def index(r):
    all_urls = {url for url, _ in get_all_url()}
    print(all_urls, type(all_urls))
    return render(request=r, template_name='index/index.html', context={
        'apps': dict(apps.all_models),
        'urls': all_urls,
    })
