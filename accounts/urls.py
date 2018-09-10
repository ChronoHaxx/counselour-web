from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
url('^signup/', views.signup, name='signup'),
url('^login/', auth_views.LoginView.as_view(template_name='boards/login.html'), name='login'),
url('^logout/', views.logout_view, name='logout'),

url('^reset/',
    auth_views.PasswordResetView.as_view(
        template_name='boards/password_reset.html',
        email_template_name='boards/password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
url('^reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='boards/password_reset_done.html'),
    name='password_reset_done'),
url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    auth_views.PasswordResetConfirmView.as_view(template_name='boards/password_reset_confirm.html'),
    name='password_reset_confirm'),
url('^reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='boards/password_reset_complete.html'),
    name='password_reset_complete'),

url('^settings/account/', views.UserUpdateView.as_view(), name='my_account'),
url('^settings/password/', auth_views.PasswordChangeView.as_view(template_name='boards/password_change.html'),
    name='password_change'),
url('^settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='boards/password_change_done.html'),
    name='password_change_done'),
url('^profile/',views.UserUpdateView.as_view(), name='my_account'),
    ]
