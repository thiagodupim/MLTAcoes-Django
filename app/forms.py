from django.forms import ModelForm
from app.models import Acoes

class AcoesForm(ModelForm):
    class Meta:
        model = Acoes
        fields = ['codigo', 'descricao', 'data', 'open', 'close', 'high', 'low', 'volume']