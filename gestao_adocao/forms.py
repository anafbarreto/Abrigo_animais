from django import forms
from .models import Adotante, Adocao
from cadastro_animal.models import Animal

class AdotanteForm(forms.ModelForm):
    
    animal_adotado = forms.ModelChoiceField(queryset=Animal.objects.filter(adotado=False), required=False)

    class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'idade', 'telefone', 'email', 'endereco', 'espaco', 'tempo', 'ciente_custos', 'disposicao_fisica_emocional', 'termo_responsabilidade', 'animal_adotado']
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'idade': 'Idade',
            'telefone': 'Telefone',
            'email': 'Email',
            'endereco': 'Endereço',
            'termo_responsabilidade': 'Aceita o Termo de Responsabilidade acima?',
            'espaco': 'Possui espaço adequado para o animal?',
            'tempo': 'Possui tempo disponível para cuidar do animal?',
            'ciente_custos': 'Está ciente dos custos para manter o animal?',
            'disposicao_fisica_emocional': 'Possui disposição física e emocional para cuidar do animal?',
            'animal_adotado': 'Qual animal deseja adotar?'
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     #self.fields['animal_adotado'].queryset = Animal.objects.filter(adotado=False)
    #     self.fields['animal_adotado'].widget.choices = [(animal.id, animal.nome) for animal in self.fields['animal_adotado'].queryset]

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['adotante', 'termo_aceito']
        #fields = ['animais', 'adotante', 'termo_aceito']