from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        #페이지 접근하려는 pk를 확인해서 request한 user와 다르면 접근 금지
        return func(request, *args, **kwargs)
    return decorated

