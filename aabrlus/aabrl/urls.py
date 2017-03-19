from django.conf.urls import patterns, include, url
from django.views.generic import list, detail
from aabrl.models import Urls
 
urlpatterns = patterns('aabrl.views',
# Home
    url(r'^$', 'index', name='home'),
# Redirecionamento para o site original
    url(r'^(?P<encurt_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
# Criação da ID do encurtamento
    url(r'^makeshort/$', 'url_encolhida', name='urlencolhida'),
# Criação da lista com os posts
    url(r'', 'url_list', name='listaurls'),
    )
