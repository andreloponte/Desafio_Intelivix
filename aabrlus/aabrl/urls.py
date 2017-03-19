from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('aabrl.views',
# Home
    url(r'^$', 'index', name='home'),
# Redirecionamento para o site original
    url(r'^(?P<encurt_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
# Criação da ID do encurtamento
    url(r'^makeshort/$', 'url_encolhida', name='urlencolhida'),
    )
