from typing import Any
import string
import random

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import valid_email_or_none
from django.conf import settings
from django.http import HttpRequest


def gerar_chave(size=12, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def populate_user(self, request, sociallogin, data):
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        name = data.get('name')
        user = sociallogin.user

        # Gerando nome com strings aleatorias caso não exista email cadastrado Erro
        if email:
            emailtouname = email.split('@')[0] + "_" + email.split('@')[1].split('.')[0]
        else:
            first_name = first_name.lower() if first_name else "semprimeironome"
            emailtouname = f"{first_name}_{gerar_chave()}"

        user_email(user, valid_email_or_none(email) or '')
        name_parts = (name or '').partition(' ')
        user_field(user, 'first_name', first_name or name_parts[0])
        user_field(user, 'last_name', last_name or name_parts[2])
        user_username(user, username or emailtouname)
        return user

