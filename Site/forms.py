from django.forms import ModelForm
from .models import Questionario

class PerguntaModelForm(ModelForm):
    class Meta:
        model = Questionario
        fields = ['pergunta', 'ruim', 'regular', 'bom', 'otimo']
