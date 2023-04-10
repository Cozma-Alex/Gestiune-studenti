import unittest

from domain.student import Student
from infrastructura.file_repo_student import FileRepoStudenti


class TesteRepoStudent(unittest.TestCase):

    def __goleste_fisier(self, cale_file):
        with open(cale_file, "w") as f:
            pass

    def test_file_repo_test(self):
        cale_test_file = "test_file_studenti.txt"
        self.__goleste_fisier(cale_test_file)
        repo = FileRepoStudenti(cale_test_file)
        assert repo.__len__() == 0
        student = Student(1, 'Andrei', 212)
        repo.adauga_student(student)
        assert repo.__len__() == 1
        repo.sterge_student_dupa_id(1)
        assert repo.__len__() == 0