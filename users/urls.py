from django.urls import path
from django.utils.functional import lazy
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    path('change-password/',auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url = 'password-changed/',
        ),
        name='password_change'
    ),
    path('change-password/password-changed/',auth_views.PasswordChangeView.as_view(
            template_name='registration/change-done.html',
            success_url = '/',
        ),
        name='change-done'
    ),
]