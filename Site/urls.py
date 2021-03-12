from django.urls import path
from Site import views as poll_views, views

from .views import IndexView, historicoView, pagenoticiaView, contactView, \
    niverView, principiosView, equipeView, concursoView, gestaoControleView, \
    leisFederaisView, portariasView, resolucoesCmnView, leisMunicipaisView, \
    portariasInstitutoView, balanceteAnualView, balanceteMensalView, crpView, calculoAtuarialView, \
    politicaInvestimentoView, acordoesView, certidoesNegativasView, contratoLicitacoesView, cronogramaPagView, \
    calendario_fiscalView, fiscal_ataView, resolucoes_FiscalView, fiscalRegimentoView, delibeCalendarioView, \
    delibeAtaView, delibeResolucoesView, regimento_DelibeView, calendario_ComiteView, ataComiteView, \
    resolucoes_ComiteView, comiteRegimentoView, composicao_ComiteView, credenciamento_ComiteView, \
    comiteMensalView, relaAnual_ComiteView, comiteAprsView, galeriaFotosView, \
    resultadoPesquisaView, membros_fiscalView, \
    membros_delibeView, membrosComiteView, calculoAtuarialAnualView, audienciaPublicaView, codigoEticaView, \
    educacaoPrevidenciariaView, planoAcaoView, cartilhaPrevidenciariaView, prePosAposentadoriaView, \
    segurancaInformacaoView, constituicaoFederalView, instrucoesNormativasView, orientacoesMpsView, \
    demonstrativoFinanceiroView, acordaosTceView, composicaoCarteiraInvestimentoView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('historico/', historicoView.as_view(), name='historico'),
    path('pagenoticia/', pagenoticiaView.as_view(), name='pagenoticia'),
    path('contact/', contactView.as_view(), name='contact'),
    path('principios/', principiosView.as_view(), name='principios'),
    path('membrosFiscal/', membros_fiscalView.as_view(), name='membrosfiscal'),
    path('membrosDelibe/', membros_delibeView.as_view(), name='membrosdelibe'),
    path('membrosComite/', membrosComiteView.as_view(), name='membroscomite'),
    path('niver/', niverView.as_view(), name='niver'),
    path('equipe/', equipeView.as_view(), name='equipe'),
    path('concurso/', concursoView.as_view(), name='concurso'),
    path('gestao-e-controle-interno/', gestaoControleView.as_view(), name='gestao-e-controle-interno'),

    path('pesquisa-de-satisfacao/', views.pesquisaSatisfacaoView.as_view(), name='pesquisa-de-satisfacao'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<question_id>/vote/', views.vote, name='vote'),







    path('leis-federais/', leisFederaisView.as_view(), name='leis-federais'),
    path('portarias/', portariasView.as_view(), name='portarias'),
    path('resolucoes-cmn/', resolucoesCmnView.as_view(), name='resolucoes-cmn'),
    path('leis-municipais/', leisMunicipaisView.as_view(), name='leis-municipais'),
    path('portarias-instituto/', portariasInstitutoView.as_view(), name='portarias-instituto'),
    path('audiencia-publica/', audienciaPublicaView.as_view(), name='audiencia-publica'),
    path('balancete-anual/', balanceteAnualView.as_view(), name='balancete-anual'),
    path('balancete-mensal/', balanceteMensalView.as_view(), name='balancete-mensal'),
    path('crp/', crpView.as_view(), name='crp'),
    path('calculo-atuarial/', calculoAtuarialView.as_view(), name='calculo-atuarial'),
    path('calculo-atuarial-anual/', calculoAtuarialAnualView.as_view(), name='calculo-atuarial-anual'),
    path('politica-investimento/', politicaInvestimentoView.as_view(), name='politica-investimento'),
    path('acordoes-tce/', acordoesView.as_view(), name='acordoes-tce'),
    path('certidoes-negativas/', certidoesNegativasView.as_view(), name='certidoes-negativas'),
    path('cronograma-de-pagamentos/', cronogramaPagView.as_view(), name='cronograma-de-pagamentos'),
    path('contratos-licitacoes/', contratoLicitacoesView.as_view(), name='contratos-licitacoes'),
    path('calendario-fiscal/', calendario_fiscalView.as_view(), name='calendario-fiscal'),
    path('fiscal-ata/', fiscal_ataView.as_view(), name='fiscal-ata'),
    path('fiscal-resolucoes/', resolucoes_FiscalView.as_view(), name='fiscal-resolucoes'),
    path('fiscal-regimento/', fiscalRegimentoView.as_view(), name='fiscal-regimento'),
    path('calendario-deliberativo/', delibeCalendarioView.as_view(), name='calendario-deliberativo'),
    path('atas-deliberativo/', delibeAtaView.as_view(), name='atas-deliberativo'),
    path('resolucoes-deliberativo/', delibeResolucoesView.as_view(), name='resolucoes-deliberativo'),
    path('regimento-deliberativo/', regimento_DelibeView.as_view(), name='regimento-deliberativo'),
    path('comite-calendario/', calendario_ComiteView.as_view(), name='comite-calendario'),
    path('comite-ata/', ataComiteView.as_view(), name='comite-ata'),
    path('comite-resolucoes/', resolucoes_ComiteView.as_view(), name='comite-resolucoes'),
    path('comite-regimento/', comiteRegimentoView.as_view(), name='comite-regimento'),
    path('comite-composicao/', composicao_ComiteView.as_view(), name='comite-composicao'),

    path('comite-credenciamento/', credenciamento_ComiteView.as_view(), name='comite-credenciamento'),
    path('relatorio-mensal-investimentos/', comiteMensalView.as_view(), name='relatorio-mensal-investimentos'),
    path('relatorio-anual-investimentos/', relaAnual_ComiteView.as_view(), name='relatorio-anual-investimentos'),
    path('apr/', comiteAprsView.as_view(), name='apr'),
    path('galeria-fotos/', galeriaFotosView.as_view(), name='galeria-fotos'),
    path('resultado-pesquisa/', resultadoPesquisaView.as_view(), name='resultado-pesquisa'),

    path('codigo-etica/', codigoEticaView.as_view(), name='codigo-etica'),
    path('educacao-previdenciaria/', educacaoPrevidenciariaView.as_view(), name='educacao-previdenciaria'),
    path('plano-acao/', planoAcaoView.as_view(), name='plano-acao'),
    path('cartilha-previdenciaria/', cartilhaPrevidenciariaView.as_view(), name='cartilha-previdenciaria'),
    path('pre-pos-aposentadoria/', prePosAposentadoriaView.as_view(), name='pre-pos-aposentadoria'),
    path('seguranca-informacao/', segurancaInformacaoView.as_view(), name='seguranca-informacao'),
    path('constituicao-federal/', constituicaoFederalView.as_view(), name='constituicao-federal'),
    path('instrucoes-normativas-mps/', instrucoesNormativasView.as_view(), name='instrucoes-normativas-mps'),
    path('orientacoes-mps/', orientacoesMpsView.as_view(), name='orientacoes-mps'),
    path('demonstrativo-financeiro/', demonstrativoFinanceiroView.as_view(), name='demonstrativo-financeiro'),
    path('acordaos-tce/', acordaosTceView.as_view(), name='acordaos-tce'),
    path('composicao-carteira-investimento/', composicaoCarteiraInvestimentoView.as_view(), name='composicao-carteira'
                                                                                                 '-investimento'),

]
