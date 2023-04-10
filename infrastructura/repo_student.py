import random

from erori.repo_error import RepoError


class RepoStudenti:
    def __init__(self):
        self._studenti = {}
        self._id_student_generare = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self._nume_generare = ["Flavius", "Emilian", "Luciana", "Dorian", "Teodora", "Simion", "Emanuela", "Grigore", "Silvia", "Lavinia", "Costache", "Sandra", "Mirela", "Rahela", "Cristiana", "Loredana"]
        self._grupa_generare = [641, 103, 648, 325, 621, 123, 221, 400, 399, 135, 366, 547, 556, 698, 515, 452]

    def adauga_student(self, student):
        '''
        adauga la dictionarul studenti studentul unic identificabil prin id student daca nu apare deja in dictionar
        :param student: student
        :return: none
        '''
        if student.get_id_student() in self._studenti:
            raise RepoError("student existent!")
        self._studenti[student.get_id_student()] = student

    def sterge_student_dupa_id(self, id_student):
        '''
        sterge din dictionarul studenti studentul unic identificabil prin id_student daca acesta apare in dictionar
        :param id_student: int
        :return: none
        '''
        if id_student not in self._studenti:
            raise RepoError("student inexistent!")
        del self._studenti[id_student]

    def cauta_student_dupa_id(self, id_student):
        '''
        cauta in dictionarul studenti studentul unic identificabil prin id_student daca acesta apare in dictionar
        :param id_student: int
        :return: studentul cu id-ul unic identificabil id_student
        '''
        if id_student not in self._studenti:
            raise RepoError("student inexistent!")
        return self._studenti[id_student]

    def modifica_student(self, student):
        '''
        modifica studentul din dictionarul studenti cu un id unic identificabil daca acesta apare in dictionar
        :param student: student
        :return: dictionarul studenti
        '''
        if student.get_id_student() not in self._studenti:
            raise RepoError("student inexistent!")
        self._studenti[student.get_id_student()] = student
        return self._studenti

    def generare_id_studenti(self, x):
        '''
        genereaza x id-uri studenti unic identificabile
        :param x: int
        :return: lista id_studenti cu x id-uri unic identificabile
        '''
        id_studenti = random.sample(self._id_student_generare, x)
        return id_studenti

    def generare_nume(self, x):
        '''
        genereaza x nume de studenti
        :param x: int
        :return: lista nume cu x nume de studenti
        '''
        nume = random.sample(self._nume_generare, x)
        return nume

    def generare_grupa(self, x):
        '''
        genereaza x grupe de studenti
        :param x: int
        :return: lista grupa cu x grupe
        '''
        grupa = random.sample(self._grupa_generare, x)
        return grupa

    def get_all(self):
        '''
        returneaza toti studentii cu id unic identifiabil din dictionarul studenti
        :return: lista studenti cu toti studentii cu id unic identifiabil din dictionarul studenti
        '''
        studenti = []
        for id_student in self._studenti:
            studenti.append(self._studenti[id_student])
        return studenti

    def __len__(self):
        '''
        returneaza numarul de elemente din dictionarul studenti
        :return: lungimea dictionarului studenti
        '''
        return len(self._studenti)
