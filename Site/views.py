import form as form
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from Site.forms import PerguntaModelForm
from Site.models import Noticia, Categoria, ArquivoPDF, Historico, Principios, CodigoEtica, EquipeInstituto, \
    EquipeFiscal, EquipeDeliberativo, EquipeComite, Concursos, EducacaoPrevidenciaria, PlanoAcao, GestaoControleInterno, \
    Questionario, Question, Choice


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['noticia'] = Noticia.objects.all()
        context['categoria'] = Categoria.objects.all()
        context['arquivo'] = ArquivoPDF.objects.all()
        context['titulo'] = Historico.objects.all()
        return context



class historicoView(TemplateView):
    template_name = 'historico.html'
    def get_context_data(self, **kwargs):
        context = super(historicoView, self).get_context_data(**kwargs)
        context['titulo'] = Historico.objects.all()
        return context

class equipeView(TemplateView):
    template_name = 'equipe.html'
    def get_context_data(self, **kwargs):
        context = super(equipeView, self).get_context_data(**kwargs)
        context['descricao'] = EquipeInstituto.objects.all()
        return context

class pagenoticiaView(TemplateView):
    template_name = 'pagenoticia.html'
    def get_context_data(self, **kwargs):
        context = super(pagenoticiaView, self).get_context_data(**kwargs)
        context['noticia'] = Noticia.objects.all()
        context['categoria'] = Categoria.objects.all()
        return context

class contactView(TemplateView):
    template_name = 'contact.html'

class codigoEticaView(TemplateView):
    template_name = 'codigoEtica.html'
    def get_context_data(self, **kwargs):
        context = super(codigoEticaView, self).get_context_data(**kwargs)
        context['codigo'] = CodigoEtica.objects.all()
        return context

class educacaoPrevidenciariaView(TemplateView):
    template_name = 'educacaoPrevidenciaria.html'
    def get_context_data(self, **kwargs):
        context = super(educacaoPrevidenciariaView, self).get_context_data(**kwargs)
        context['educacao'] = EducacaoPrevidenciaria.objects.order_by('-titulo').all()
        return context

class planoAcaoView(TemplateView):
    template_name = 'planoAcao.html'
    def get_context_data(self, **kwargs):
        context = super(planoAcaoView, self).get_context_data(**kwargs)
        context['plano'] = PlanoAcao.objects.order_by('-titulo').all()
        return context

class cartilhaPrevidenciariaView(TemplateView):
    template_name = 'cartilhaPrevidenciaria.html'

class prePosAposentadoriaView(TemplateView):
    template_name = 'prePosAposentadoria.html'

class segurancaInformacaoView(TemplateView):
    template_name = 'segurancaInformacao.html'

class constituicaoFederalView(TemplateView):
    template_name = 'constituicaoFederal.html'

class instrucoesNormativasView(TemplateView):
    template_name = 'instrucoesNormativas.html'

class orientacoesMpsView(TemplateView):
    template_name = 'orientacoesMps.html'

class demonstrativoFinanceiroView(TemplateView):
    template_name = 'demostrativoFinanceiro.html'

class acordaosTceView(TemplateView):
    template_name = 'acordaosTce.html'

class composicaoCarteiraInvestimentoView(TemplateView):
    template_name = 'composicaoCarteiraInvestimento.html'

class principiosView(TemplateView):
    template_name = 'principios.html'
    def get_context_data(self, **kwargs):
        context = super(principiosView, self).get_context_data(**kwargs)
        context['principio'] = Principios.objects.all()
        return context

class membros_fiscalView(TemplateView):
    template_name = 'membrosFiscal.html'
    def get_context_data(self, **kwargs):
        context = super(membros_fiscalView, self).get_context_data(**kwargs)
        context['fiscal'] = EquipeFiscal.objects.all()
        return context


class calendario_fiscalView(TemplateView):
    template_name = 'calendarioFiscal.html'

class fiscal_ataView(TemplateView):
    template_name = 'atasFiscal.html'

class resolucoes_FiscalView(TemplateView):
    template_name = 'resolucoesFiscal.html'

class fiscalRegimentoView(TemplateView):
    template_name = 'regimentoFiscal.html'

class membros_delibeView(TemplateView):
    template_name = 'membrosDelibe.html'
    def get_context_data(self, **kwargs):
        context = super(membros_delibeView, self).get_context_data(**kwargs)
        context['delibe'] = EquipeDeliberativo.objects.all()
        return context

class delibeCalendarioView(TemplateView):
    template_name = 'calendarioDelibe.html'

class delibeAtaView(TemplateView):
    template_name = 'ataDelibe.html'

class delibeResolucoesView(TemplateView):
    template_name = 'resolucoesDelibe.html'

class regimento_DelibeView(TemplateView):
    template_name = 'regimentoDelibe.html'

class membrosComiteView(TemplateView):
    template_name = 'membrosComite.html'
    def get_context_data(self, **kwargs):
        context = super(membrosComiteView, self).get_context_data(**kwargs)
        context['comite'] = EquipeComite.objects.all()
        return context

class calendario_ComiteView(TemplateView):
    template_name = 'calendarioComite.html'

class ataComiteView(TemplateView):
    template_name = 'ataComite.html'

class resolucoes_ComiteView(TemplateView):
    template_name = 'resolucoesComite.html'

class comiteRegimentoView(TemplateView):
    template_name = 'regimentoComite.html'

class composicao_ComiteView(TemplateView):
    template_name = 'composicaoComite.html'

class credenciamento_ComiteView(TemplateView):
    template_name = 'credenciamentoComite.html'

class comiteMensalView(TemplateView):
    template_name = 'relatorioMensalInvestimento.html'

class relaAnual_ComiteView(TemplateView):
    template_name = 'relatorioAnualInvestimento.html'

class comiteAprsView(TemplateView):
    template_name = 'apr.html'

class niverView(TemplateView):
    template_name = 'niver.html'

class concursoView(TemplateView):
    template_name = 'concurso.html'
    def get_context_data(self, **kwargs):
        context = super(concursoView, self).get_context_data(**kwargs)
        context['concurso'] = Concursos.objects.order_by('-titulo').all()
        return context

class gestaoControleView(TemplateView):
    template_name = 'gestaoControle.html'
    def get_context_data(self, **kwargs):
        context = super(gestaoControleView, self).get_context_data(**kwargs)
        context['gestao'] = GestaoControleInterno.objects.order_by('-titulo').all()
        return context

class pesquisaSatisfacaoView(generic.ListView):
    template_name = 'pesquisaSatisfacao.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Choice.objects.order_by('id')[:20]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'


def votew(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pesquisaSatisfacao.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def vote(request, question_id):
    escolhas = Choice.objects.get(pk=question_id)
    if str(request.method) == 'POST':
        select_option = request.POST['choice']
        print(request.POST['choice'])
        if select_option == 'Otimo':
            escolhas.choice_text += 1
        elif select_option == 'Bom':
            escolhas.choice_text2 += 1
        elif select_option == 'Regular':
            escolhas.choice_text3 += 1
        elif select_option == 'Ruim':
            escolhas.choice_text4 += 1

        else:
            return HttpResponse(400, 'Formulário Inválido')
        escolhas.save()

    return render(request, 'pesquisaSatisfacao.html')




class leisFederaisView(TemplateView):
    template_name = 'leisFederais.html'

class portariasView(TemplateView):
    template_name = 'portarias.html'

class resolucoesCmnView(TemplateView):
    template_name = 'resolucoesCMN.html'

class leisMunicipaisView(TemplateView):
    template_name = 'leismunicipais.html'

class portariasInstitutoView(TemplateView):
    template_name = 'portariasInstituto.html'

class audienciaPublicaView(TemplateView):
    template_name = 'audienciaPublica.html'

class balanceteAnualView(TemplateView):
    template_name = 'balanceteAnual.html'

class balanceteMensalView(TemplateView):
    template_name = 'balanceteMensal.html'

class crpView(TemplateView):
    template_name = 'crp.html'

class calculoAtuarialView(TemplateView):
    template_name = 'calculoAtuarial.html'

class calculoAtuarialAnualView(TemplateView):
    template_name = 'calculoAtuarialAnual.html'

class politicaInvestimentoView(TemplateView):
    template_name = 'politicaInvestimento.html'

class acordoesView(TemplateView):
    template_name = 'acordoes.html'

class certidoesNegativasView(TemplateView):
    template_name = 'certidoesNegativas.html'

class cronogramaPagView(TemplateView):
    template_name = 'cronogramaPag.html'

class contratoLicitacoesView(TemplateView):
    template_name = 'contratoLicitacoes.html'

class galeriaFotosView(TemplateView):
    template_name = 'galeriaFotos.html'

class resultadoPesquisaView(TemplateView):

    template_name = 'resultadoPesquisa.html'

