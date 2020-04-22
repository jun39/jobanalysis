from django.contrib.auth.forms import AuthenticationForm

# ログインフォームを作成する
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # 入力フォームのクラス属性にform-controlを指定することでブートストラップで操作できるようにしている
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
            # 入力フォームのプレイスフォルダー属性にラベルの名前を入れている
