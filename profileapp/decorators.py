from django.http import HttpResponseForbidden

from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        #pk에서 profile의 주인을 받아와서 확인
        if not profile.user == request.user:
            return HttpResponseForbidden()
        #request한 user와 다르면 접근 금지
        return func(request, *args, **kwargs)
    return decorated