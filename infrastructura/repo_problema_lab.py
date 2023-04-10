import random

from erori.repo_error import RepoError


class RepoProblemaLab:
    def __init__(self):
        self._problema_lab = {}
        self.__nr_problema_generare = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.__descriere_generare = ["WNFFt", "ZFnlU", "rjBmb", "lUgOp", "uwYxK", "QzgOF", "HRggw", "fmvHo", "HQiKK", "huZOn", "EuSkA", "YIEDW", "KrztQ", "DKvSH", "HvkOo", "SPLQL"]
        self.__deadline_generare = [27,  4,  9, 10, 16, 32, 36, 40, 35, 23, 12, 34, 26,  6, 31, 19]

    def adauga_problema_lab(self, problema_laborator):
        '''
        adauga la dictionarul problema_lab problema de laborator unic identificabila prin numar de problema daca nu se regaseste in dictionar
        :param problema_laborator: Problema_laborator
        :return: none
        '''
        if problema_laborator.get_numar_problema_lab() in self._problema_lab:
            raise RepoError("problema laborator existenta!")
        self._problema_lab[problema_laborator.get_numar_problema_lab()] = problema_laborator

    def cauta_laborator_dupa_nr(self, nr_problema):
        '''
        cauta in dictionarul probleme_lab problema de laborator unic identificabila prin numarul de problema daca se regaseste in dictionarul probleme_lab
        :param nr_problema: int
        :return: studentul cu nr_problema unic identificabil daca se regaseste in dictionarul probleme_lab
                 in caz contrar raise repoError
        '''
        if nr_problema not in self._problema_lab:
            raise RepoError("problema laborator inexistenta!")
        return self._problema_lab[nr_problema]

    def sterge_laborator_dupa_numar(self, nr_problema):
        '''
        sterge din dictionarul problema_lab problema de laborator cu numar problema unic identificabil
        :param nr_problema: int
        :return: none
        '''
        if nr_problema not in self._problema_lab:
            raise RepoError("problema laborator inexistenta!")
        del self._problema_lab[nr_problema]

    def modifica_problema_laborator(self, problema_lab):
        '''
        modifica problema de laborator din dictionarul problema_lab cu numar de problema unic identificabil daca se gaseste in dictionar
        :param problema_lab: Problema_laborator
        :return: dictionarul problema_lab
        '''
        if problema_lab.get_numar_problema_lab() not in self._problema_lab:
            raise RepoError("problema laborator inexistenta!")
        self._problema_lab[problema_lab.get_numar_problema_lab()] = problema_lab
        return self._problema_lab

    def generare_nr_probleme(self, x):
        '''
        genereaza x intreg numere de problema unic identificabile
        :param x: int
        :return: lista numar_probleme
        '''
        numar_probleme = random.sample(self.__nr_problema_generare, x)
        return numar_probleme

    def generare_descriere(self, x):
        '''
        genereaza x intreg descrieri de problema
        :param x: int
        :return: lista descriere
        '''
        descriere = random.sample(self.__descriere_generare, x)
        return descriere

    def generare_deadline(self, x):
        '''
        genereaza x intreg deadline-uri de probleme
        :param x: int
        :return: lista deadline
        '''
        deadline = random.sample(self.__deadline_generare, x)
        return deadline

    def get_all(self):
        '''
        returneaza toate problemele cu numar de problema unic identificabila din dictionarul problema_lab
        :return: lista probleme_laborator cu toate problemele de laborator cu numar de problema unic identificabila
        '''
        probleme_laborator = []
        for numar_problema_lab in self._problema_lab:
            probleme_laborator.append(self._problema_lab[numar_problema_lab])
        return probleme_laborator

    def __len__(self):
        '''
        returneaza numarul de elemente din dictionarul probleme_lab
        :return: numarul de elemente din dictionarul probleme_lab
        '''
        return len(self._problema_lab)
