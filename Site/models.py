from django.db import models
from stdimage.models import StdImageField
from django.utils import timezone
import datetime

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Questionario(models.Model):
    pergunta = models.CharField('Pergunta', max_length=200)
    ruim = models.IntegerField('Ruim', default=0)
    regular = models.IntegerField('Regular', default=0)
    bom = models.IntegerField('Bom', default=0)
    otimo = models.IntegerField('Ótimo', default=0)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    choice_text2 = models.CharField(max_length=200)
    votes2 = models.IntegerField(default=0)
    choice_text3 = models.CharField(max_length=200)
    votes3 = models.IntegerField(default=0)
    choice_text4 = models.CharField(max_length=200)
    votes4 = models.IntegerField(default=0)



    def __str__(self):
        return self.choice_text

# final do questionario

class Categoria(Base):
    categoria = models.CharField('Categoria', max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.categoria

class Noticia(Base):
    titulo = models.CharField('Título', max_length=100)
    imagem = StdImageField('Imagem', upload_to='img_noticia', variations={'thumb': {'width': 359, 'height': 286, 'crop':True}})
    descricao = models.TextField('Descrição', max_length=200)
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Noticias'
    def __str__(self):
        return self.titulo
class ArquivoPDF(Base):
    categoria = models.ForeignKey('Site.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=450)
    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'
        def __str__(self):
            return self.categoria

# página histórico
class Historico(Base):
    titulo = models.CharField('Título', max_length=100)
    imagem = StdImageField('Imagem', blank=True, upload_to='img_historico', variations={'thumb': {'width': 380, 'height': 649, 'crop':True}})
    subtitulo01 = models.CharField('Subtítulo01', max_length=100)
    descricao01 = models.TextField('Subtítulo01 Descrição', max_length=800)
    subtitulo02 = models.CharField('Subtítulo02', max_length=100)
    descricao02 = models.TextField('Subtítulo02 Descrição', max_length=800)
    contador01 = models.CharField('contador01', max_length=50)
    valor01 = models.CharField('valor contador01', max_length=6)
    contador02 = models.CharField('contador02', max_length=50)
    valor02 = models.CharField('valor contador02', max_length=6)
    contador03 = models.CharField('contador03', max_length=50)
    valor03 = models.CharField('valor contador03', max_length=6)
    subtitulo03 = models.CharField('Subtítulo03', blank=True, max_length=100)
    descricao03 = models.TextField('Subtítulo03 Descrição', blank=True, max_length=800)
    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Histórico'
        def __str__(self):
            return self.titulo

# Página princípios

class Principios(Base):
    titulo = models.CharField('Título', max_length=100)
    subtitulo01 = models.CharField('Subtítulo01', max_length=100)
    descricao01 = models.TextField('Subtítulo01 Descrição', max_length=800)
    imagem01 = StdImageField('Imagem01', blank=True, upload_to='img_principio',)
    subtitulo02 = models.CharField('Subtítulo02', max_length=100)
    descricao02 = models.TextField('Subtítulo02 Descrição', max_length=800)
    imagem02 = StdImageField('Imagem02', blank=True, upload_to='img_principio',)
    subtitulo03 = models.CharField('Subtítulo03', max_length=100)
    descricao03 = models.TextField('Subtítulo03 Descrição', max_length=800)
    imagem03 = StdImageField('Imagem03', blank=True, upload_to='img_principio',)
    class Meta:
        verbose_name = 'Princípio'
        verbose_name_plural = 'Princípio'
        def __str__(self):
            return self.principio

class CodigoEtica(Base):
    categoria = models.ForeignKey('Site.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    descricao = models.TextField('Descrição', max_length=800)
    titulo = models.CharField('Título', max_length=100)
    class Meta:
        verbose_name = 'Código de Ética'
        verbose_name_plural = 'Código de Ética'
        def __str__(self):
            return self.codigoEtica

class EquipeInstituto(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    atuacao = models.CharField('Atuação', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    imagem = StdImageField('Imagem', blank=True, upload_to='EquipeInstituto')
    face = models.CharField('Facebook', max_length=100)
    gmais = models.CharField('Google+', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)
    class Meta:
        verbose_name = 'Equipe Instituto'
        verbose_name_plural = 'Equipe Instituto'
        def __str__(self):
            return self.EquipeInstituto

class EquipeFiscal(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    atuacao = models.CharField('Atuação', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    imagem = StdImageField('Imagem', blank=True, upload_to='EquipeFiscal')
    face = models.CharField('Facebook', max_length=100)
    gmais = models.CharField('Google+', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)
    class Meta:
        verbose_name = 'Equipe Conselho Fiscal'
        verbose_name_plural = 'Equipe Conselho Fiscal'
        def __str__(self):
            return self.EquipeFiscal

class EquipeDeliberativo(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    atuacao = models.CharField('Atuação', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    imagem = StdImageField('Imagem', blank=True, upload_to='EquipeDeliberativo')
    face = models.CharField('Facebook', max_length=100)
    gmais = models.CharField('Google+', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)
    class Meta:
        verbose_name = 'Equipe Conselho Deliberativo'
        verbose_name_plural = 'Equipe Conselho Deliberativo'
        def __str__(self):
            return self.EquipeDeliberativo

class EquipeComite(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    atuacao = models.CharField('Atuação', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    imagem = StdImageField('Imagem', blank=True, upload_to='EquipeComite')
    face = models.CharField('Facebook', max_length=100)
    gmais = models.CharField('Google+', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)
    class Meta:
        verbose_name = 'Equipe Comitê de Investimento'
        verbose_name_plural = 'Equipe Comitê de Investimento'
        def __str__(self):
            return self.EquipeInstituto

class Concursos(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    imagem = StdImageField('Imagem', blank=True, upload_to='Concursos')
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Concurso'
        verbose_name_plural = 'Concursos'
        def __str__(self):
            return self.Concursos

class EducacaoPrevidenciaria(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Educação Previdênciaria'
        verbose_name_plural = 'Educação Previdênciaria'
        def __str__(self):
            return self.EducacaoPrevidenciaria

class PlanoAcao(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Plano de Ação'
        verbose_name_plural = 'Plano de Ação'
        def __str__(self):
            return self.PlanoAcao

class GestaoControleInterno(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Gestão e Controle Interno'
        verbose_name_plural = 'Gestão e Controle Interno'
        def __str__(self):
            return self.GestaoControleInterno

class ConstituicaoFederal(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Constituição Federal'
        verbose_name_plural = 'Constituição Federal'
        def __str__(self):
            return self.ConstituicaoFederal

class CartilhaPrevidenciaria(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Cartilha Previdenciária'
        verbose_name_plural = 'Cartilha Previdenciária'
        def __str__(self):
            return self.CartilhaPrevidenciaria

class PrePosAposentadoria(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Pré Pós Aposentadoria'
        verbose_name_plural = 'Pré Pós Aposentadoria'
        def __str__(self):
            return self.PrePosAposentadoria

class SegurancaInformacao(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Segurança da Informação'
        verbose_name_plural = 'Segurança da Informação'
        def __str__(self):
            return self.SegurancaInformacao

class LeisFederais(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Leis Federais'
        verbose_name_plural = 'Leis Federais'
        def __str__(self):
            return self.LeisFederais

class InstrucoesNormativas(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Instruções Normativas'
        verbose_name_plural = 'Instruções Normativas'
        def __str__(self):
            return self.InstrucoesNormativas

class OrientacoesMps(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Orientações Mps'
        verbose_name_plural = 'Orientações Mps'
        def __str__(self):
            return self.OrientacoesMps

class PortariasMps(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Portarias Mps'
        verbose_name_plural = 'Portarias Mps'
        def __str__(self):
            return self.PortariasMps

class ResolucoesCmn(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Resoluções Cmn'
        verbose_name_plural = 'Resoluções Cmn'
        def __str__(self):
            return self.ResolucoesCmn

class LeisMunicipais(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Leis Municipais'
        verbose_name_plural = 'Leis Municipais'
        def __str__(self):
            return self.LeisMunicipais

class PortariasInstituto(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=800)
    arquivo = models.FileField('Arquivo', upload_to='PDFfiles')
    class Meta:
        verbose_name = 'Portarias Instituto'
        verbose_name_plural = 'Portarias Instituto'
        def __str__(self):
            return self.PortariasInstituto
