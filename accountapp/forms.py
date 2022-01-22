from django.contrib.auth.forms import UserCreationForm

#form을 상속받음, 가입하고 ID를 못 바꾸게 하기 위함
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #disabled가 True로 바꿔줌으로 커스터마이징이 됨
        self.fields['username'].disabled = True