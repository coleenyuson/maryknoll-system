from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^admin-settings', views.settings, name = 'admin-settings'),
    url(r'^registration/', include('registration.urls'), name = 'registration'),
    url(r'^cashier/', include('cashier.urls'), name = 'cashier'),
    url(r'^enrollment/', include('enrollment.urls'), name = 'enrollment'),
    url(r'^administrative/', include('administrative.urls'), name = 'administrative'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
        url(r'^accounts/', include('django.contrib.auth.urls')),
    ]
    
'''This automatically adds:
    ^accounts/login/$ [name='login']
    ^accounts/logout/$ [name='logout']
    ^accounts/password_change/$ [name='password_change']
    ^accounts/password_change/done/$ [name='password_change_done']
    ^accounts/password_reset/$ [name='password_reset']
    ^accounts/password_reset/done/$ [name='password_reset_done']
    ^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
    ^accounts/reset/done/$ [name='password_reset_complete']
    
    
    although they dont have any templates yet, you can add each inside ./auth/templates
'''