import unittest

from business.service_nota import ServiceNota
from business.service_problema_lab import ServiceProblemaLab
from business.service_student import ServiceStudenti
from domain.nota import Nota
from domain.problema_laborator import Problema_laborator
from domain.student import Student
from erori.repo_error import RepoError
from erori.validation_error import ValidError
from infrastructura.file_repo_nota import FileRepoNote
from infrastructura.file_repo_problema_lab import FileRepoProblemeLab
from infrastructura.file_repo_student import FileRepoStudenti
from infrastructura.repo_nota import RepoNote
from infrastructura.repo_problema_lab import RepoProblemaLab
from infrastructura.repo_student import RepoStudenti
from validare.validator_nota import ValidatorNota
from validare.validator_problema_lab import ValidatorProblemaLab
from validare.validator_student import ValidatorStudent


class Teste(unittest.TestCase):

    def test_define(self):
        self.__repo_note = RepoNote()
        self.__repo_studenti = RepoStudenti()
        self.__repo_probleme_lab = RepoProblemaLab()
        self.__repo_file_note = FileRepoNote(self.__repo_note)
        self.__repo_file_studenti = FileRepoStudenti(self.__repo_studenti)
        self.__repo_file_problema_lab = FileRepoProblemeLab(self.__repo_probleme_lab)
        self.__validator_nota = ValidatorNota()
        self.__validator_student = ValidatorStudent()
        self.__validator_problema_lab = ValidatorProblemaLab()
        self.__service_note = ServiceNota(self.__validator_nota, self.__repo_note, self.__repo_studenti, self.__repo_probleme_lab, self.__repo_file_note, self.__repo_file_studenti, self.__repo_file_problema_lab)
        self.__service_studenti = ServiceStudenti(self.__validator_student, self.__repo_studenti, self.__repo_file_studenti)
        self.__service_probleme_lab = ServiceProblemaLab(self.__validator_problema_lab, self.__repo_probleme_lab, self.__repo_file_problema_lab)

    def test_stergere_student(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_note.sterge_student_si_note(1, "memorie")
        self.assertTrue("student inexistent!" in str(context.exception))

    def test_adaugare_student(self):
        self.test_define()
        self.__service_studenti.adauga_student(1, 'Andrei', 212, "memorie")
        with self.assertRaises(RepoError) as context:
            self.__service_studenti.adauga_student(1, 'Elena', 314, "memorie")
        self.assertTrue("student existent" in str(context.exception))
        self.__service_note.sterge_student_si_note(1, "memorie")

    def test_cautare_student(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_studenti.cautare_dupa_id(2, "memorie")
        self.assertTrue("student inexistent!" in str(context.exception))

    def test_modifica_student(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_studenti.modifica_student(20, 'Traian', 912, "memorie")
        self.assertTrue("student inexistent!" in str(context.exception))

    def test_student_true(self):
        self.test_define()
        self.__service_studenti.adauga_student(1, 'Andrei', 212, "memorie")
        self.__service_studenti.adauga_student(2, 'Elena', 1234, "memorie")
        assert self.__repo_studenti.__len__() == 2
        assert self.__service_studenti.modifica_student(2, 'Florina', 917, "memorie")
        assert self.__service_studenti.cautare_dupa_id(1, "memorie")
        assert self.__service_studenti.cautare_dupa_id(2, "memorie")
        self.__service_note.sterge_student_si_note(1, "memorie")
        self.__service_note.sterge_student_si_note(2, "memorie")
        assert self.__repo_studenti.__len__() == 0

    def test_student_valid(self):
        self.test_define()
        student = Student(1, 'Andre', 212)
        self.__validator_student.valideaza(student)
        student_gresit = Student(-2, '', 0)
        try:
            self.__validator_student.valideaza(student_gresit)
            assert False
        except ValidError as ve:
            assert (str(ve) == "id invalid!\ngrupa invalida!\nnume invalid!\n")

    def test_adaugare_lab(self):
        self.test_define()
        self.__service_probleme_lab.adauga_problema_laborator(1, 'TDD', 12, "memorie")
        with self.assertRaises(RepoError) as context:
            self.__service_probleme_lab.adauga_problema_laborator(1, 'Functionalitati', 21, "memorie")
        self.assertTrue("problema laborator existenta!" in str(context.exception))
        self.__service_note.sterge_laborator_si_note(1, "memorie")

    def test_sterge_lab(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_note.sterge_laborator_si_note(2, "memorie")
        self.assertTrue("problema laborator inexistenta!")

    def test_cauta_lab(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_probleme_lab.cautare_laborator_dupa_numar_problema(2, "memorie")
        self.assertTrue("problema laborator inexistenta!" in str(context.exception))

    def test_modifica_lab(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_probleme_lab.modifica_problema_laborator(17, "Functionalitati", 12, "memorie")
        self.assertTrue("problema laborator inexistenta!" in str(context.exception))

    def test_problema_lab_true(self):
        self.test_define()
        self.__service_probleme_lab.adauga_problema_laborator(1, "TDD", 12, "memorie")
        assert self.__repo_probleme_lab.__len__() == 1
        assert self.__service_probleme_lab.cautare_laborator_dupa_numar_problema(1, "memorie")
        assert self.__service_probleme_lab.modifica_problema_laborator(1, "Functionalitati", 10, "memorie")
        self.__service_note.sterge_laborator_si_note(1, "memorie")
        assert self.__repo_probleme_lab.__len__() == 0

    def test_problema_lab_valid(self):
        self.test_define()
        problema_lab = Problema_laborator(1, 'TDD', 12)
        self.__validator_problema_lab.valideaza(problema_lab)
        problema_lab_gresita = Problema_laborator(-8, '', -2)
        try:
            self.__validator_problema_lab.valideaza(problema_lab_gresita)
            assert False
        except ValidError as ve:
            assert str(ve) == "numar problema laborator invalid\ndescriere invalida\ndeadline invalid\n"

    def test_adaugare_nota(self):
        self.test_define()
        self.__service_studenti.adauga_student(1, 'Andrei', 212, "memorie")
        self.__service_probleme_lab.adauga_problema_laborator(1, 'TDD', 10, "memorie")
        self.__service_note.adauga_nota(1, 1, 1, 1, "memorie")
        with self.assertRaises(RepoError) as context:
            self.__service_note.adauga_nota(2, 2, 2, 2, "memorie")
        self.assertTrue("student inexistent!" in str(context.exception))
        with self.assertRaises(RepoError) as context:
            self.__service_note.adauga_nota(2, 1, 2, 2, "memorie")
        self.assertTrue("problema laborator inexistenta!" in str(context.exception))
        with self.assertRaises(RepoError) as context:
            self.__service_note.adauga_nota(1, 1, 1, 1, "memorie")
        self.assertTrue("nota existenta!" in str(context.exception))
        self.__service_note.sterge_laborator_si_note(1, "memorie")
        self.__service_note.sterge_student_si_note(1, "memorie")

    def test_sterge_nota(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_note.sterge_nota(1, "memorie")
        self.assertTrue("nota inexistenta!" in str(context.exception))

    def test_modifica_nota(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_note.modifica_nota(1, 1, 1, 1, "memorie")
        self.assertTrue("nota inexistenta!" in str(context.exception))
        self.__service_studenti.adauga_student(1, 'Andrei', 212, "memorie")
        self.__service_probleme_lab.adauga_problema_laborator(1, 'TDD', 10, "memorie")
        self.__service_note.adauga_nota(1, 1, 1, 1, "memorie")
        self.__service_note.modifica_nota(1,1,1,8,"memorie")
        with self.assertRaises(RepoError) as context:
            self.__service_note.modifica_nota(1, 2, 1, 1, "memorie")
        self.assertTrue("student inexistent!" in str(context.exception))
        with self.assertRaises(RepoError) as context:
            self.__service_note.modifica_nota(1, 1, 2, 1, "memorie")
        self.assertTrue("problema laborator inexistenta!" in str(context.exception))
        self.__service_note.sterge_student_si_note(1, "memorie")
        self.__service_note.sterge_laborator_si_note(1, "memorie")

    def test_cauta_nota(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_note.cauta_nota_dupa_id(1, "memorie")
        self.assertTrue("nota inexistenta!" in str(context.exception))

    def test_nota_valid(self):
        self.test_define()
        nota = Nota(1, 1, 1, 1)
        self.__validator_nota.valideaza(nota)
        nota_gresita = Nota(-1, -2, -7, -0)
        try:
            self.__validator_nota.valideaza(nota_gresita)
            assert False
        except ValidError as ve:
            assert str(ve) == "id nota invalid\nid student invalid\nnumar problema laborator invalid\nvaloare nota invalida\n"
        nota_gresita_2 = Nota(-1, -2, -4, 11)
        try:
            self.__validator_nota.valideaza(nota_gresita_2)
            assert False
        except ValidError as ve:
            assert str(ve) == "id nota invalid\nid student invalid\nnumar problema laborator invalid\nvaloare nota invalida\n"

    def test_liste(self):
        self.test_define()
        with self.assertRaises(RepoError) as context:
            self.__service_note.lista_note_alfabetic(1, "memorie")
        self.assertTrue("problema laborator inexistenta!" in str(context.exception))
        with self.assertRaises(RepoError) as context:
            self.__service_note.lista_note_crescator(1, "memorie","bubble")
        self.assertTrue("problema laborator inexistenta!" in str(context.exception))
        lista_medie_student = []
        lista_medie_student = self.__service_note.nota_sub_5([], [], lista_medie_student, 0)
        assert len(lista_medie_student) == 0
        self.__service_studenti.adauga_student(1, 'Andrei', 212, "memorie")
        self.__service_probleme_lab.adauga_problema_laborator(1, 'TDD', 10, "memorie")
        self.__service_note.adauga_nota(1, 1, 1, 1, "memorie")
        lista_note_alfabetic = self.__service_note.lista_note_alfabetic(1, "memorie")
        assert len(lista_note_alfabetic) == 1
        lista_studenti_alfabetic = self.__service_note.lista_studenti_alfabetic(lista_note_alfabetic, "memorie", "bubble")
        assert len(lista_studenti_alfabetic) == 1
        lista_note_studenti_alfabetic = self.__service_note.lista_note_definitorie_alfabetic(lista_studenti_alfabetic, lista_note_alfabetic)
        assert len(lista_note_studenti_alfabetic) == 1
        lista_note_crescator = self.__service_note.lista_note_crescator(1, "memorie", "bubble")
        lista_studenti_crescator = self.__service_note.lista_definitorie_crescator(lista_note_crescator, "memorie")
        assert len(lista_note_crescator) == 1
        assert len(lista_studenti_crescator) == 1
        lista_note = self.__service_note.get_all_note("memorie")
        lista_studenti = self.__service_studenti.get_all_studenti("memorie")
        lista_medie_student = self.__service_note.nota_sub_5(lista_note, lista_studenti, lista_medie_student, 0)
        assert len(lista_medie_student) == 1
        self.__service_note.sterge_laborator_si_note(1, "memorie")
        self.__service_note.sterge_student_si_note(1, "memorie")
