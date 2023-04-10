import unittest

from domain.problema_laborator import Problema_laborator
from infrastructura.file_repo_problema_lab import FileRepoProblemeLab


class TesteRepoProblemeLab(unittest.TestCase):

    def goleste_fisier(self, cale_file):
        with open(cale_file, "w") as f:
            pass

    def test_file_repo_test(self):
        cale_test_file = "test_file_probleme_lab.txt"
        self.goleste_fisier(cale_test_file)
        repo = FileRepoProblemeLab(cale_test_file)
        assert repo.__len__() == 0
        problema_lab = Problema_laborator(1, 'TDD', 10)
        repo.adauga_problema_lab(problema_lab)
        assert repo.__len__() == 1