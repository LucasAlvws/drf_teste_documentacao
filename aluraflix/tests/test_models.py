from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Lucas Filmes',
            data_lancamento = '2003-07-04'
        )

    def test_verifica_atributos_do_programa(self):
        '''teste verifica atributos do programa'''
        self.assertEqual(self.programa.titulo,'Lucas Filmes')
        self.assertEqual(self.programa.tipo,'F')
        self.assertEqual(self.programa.data_lancamento,'2003-07-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)

    