from django.contrib import admin
from .models import ConstituicaoFederal, CartilhaPrevidenciaria, PrePosAposentadoria, \
    SegurancaInformacao, LeisFederais, InstrucoesNormativas, OrientacoesMps, PortariasMps, ResolucoesCmn, \
    LeisMunicipais, PortariasInstituto
from .models import Categoria, Noticia, ArquivoPDF, Historico, Principios, CodigoEtica, EquipeInstituto, \
    EquipeDeliberativo, EquipeComite, EquipeFiscal, Concursos, EducacaoPrevidenciaria, PlanoAcao, GestaoControleInterno


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


@admin.register(ConstituicaoFederal)
class ConstituicaoFederalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(CartilhaPrevidenciaria)
class CartilhaPrevidenciariaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(PrePosAposentadoria)
class PrePosAposentadoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(SegurancaInformacao)
class SegurancaInformacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(LeisFederais)
class LeisFederaisAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(InstrucoesNormativas)
class InstrucoesNormativasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(OrientacoesMps)
class OrientacoesMpsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(PortariasMps)
class PortariasMpsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(ResolucoesCmn)
class ResolucoesCmnAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(LeisMunicipais)
class LeisMunicipaisAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')

@admin.register(PortariasInstituto)
class PortariasInstitutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'ativo', 'modificado')
