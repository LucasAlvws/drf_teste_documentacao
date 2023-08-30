from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def test_falha(self):
        self.fail('teste_falhou')