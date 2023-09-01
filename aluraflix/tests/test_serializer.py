from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Lucas Filmes',
            data_lancamento = '2003-07-04'
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_atributos_do_serializer(self):
        '''verifica atributos serizalizzer'''
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudo_dos_campos_serializer(self):
        '''testa os campos do serializer'''
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
    