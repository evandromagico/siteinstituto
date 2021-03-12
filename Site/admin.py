from django.contrib import admin
from .models import Question, Choice
from .models import Categoria, Noticia, ArquivoPDF, Historico, Principios, CodigoEtica, EquipeInstituto, \
    EquipeDeliberativo, EquipeComite, EquipeFiscal, Concursos, EducacaoPrevidenciaria, PlanoAcao, GestaoControleInterno, \
    Questionario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'modificado', 'ativo')

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'criados', 'modificado', 'ativo')

@admin.register(ArquivoPDF)
class ArquivoPDFAdmin(admin.ModelAdmin):
     list_display = ('categoria', 'arquivo', 'criados', 'modificado', 'ativo')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criados', 'modificado', 'ativo')

@admin.register(Principios)
class PrincipiosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criados', 'modificado', 'ativo')

@admin.register(CodigoEtica)
class CodigoEticaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'arquivo', 'modificado', 'ativo')

@admin.register(EquipeInstituto)
class EquipeInstitutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'atuacao', 'email', 'telefone', 'ativo', 'modificado')

@admin.register(EquipeFiscal)
class EquipeFiscalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'atuacao', 'email', 'telefone', 'ativo', 'modificado')

@admin.register(EquipeDeliberativo)
class EquipeDeliberativoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'atuacao', 'email', 'telefone', 'ativo', 'modificado')

@admin.register(EquipeComite)
class EquipeComiteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'atuacao', 'email', 'telefone', 'ativo', 'modificado')

@admin.register(Concursos)
class ConcursosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'imagem', 'ativo', 'modificado')

@admin.register(EducacaoPrevidenciaria)
class EducacaoPrevidenciariaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(PlanoAcao)
class PlanoAcaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(GestaoControleInterno)
class GestaoControleInternoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'ruim', 'regular', 'bom', 'otimo')



admin.site.register(Question)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes', 'choice_text2', 'votes2', 'choice_text3', 'votes3', 'choice_text4', 'votes4')