import unittest

from domain.nota import Nota
from infrastructura.file_repo_nota import FileRepoNote


class TesteRepoNote(unittest.TestCase):

    def __goleste_fisier(self, cale_fisier):
        with open(cale_fisier, "w") as f:
            pass

    def test_file_repo_test(self):
        cale_test_file = "test_file_note.txt"
        self.__goleste_fisier(cale_test_file)
        repo = FileRepoNote(cale_test_file)
        assert repo.__len__() == 0
        nota = Nota(1, 1, 1, 1)
        repo.adauga_nota(nota)
        assert repo.__len__() == 1