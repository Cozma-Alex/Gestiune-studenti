from domain.problema_laborator import Problema_laborator


class ServiceProblemaLab:
    def __init__(self, validator_problema_lab, repo_probleme_lab, repo_file_probleme_lab):
        self.__validator_problema_lab = validator_problema_lab
        self.__repo_probleme_lab = repo_probleme_lab
        self.__repo_file_probleme_lab = repo_file_probleme_lab

    def adauga_problema_laborator(self, numar_laborator_numar_problema, descriere, deadline, date):
        '''
        creeaza o problema laborator pe baaza numar_laborator_numar_problema int, descriere string, deadline int
        se valideaza problema de laborator si daca este valida este adaugata in repo_probleme_lab
        :param numar_laborator_numar_problema: int
        :param descriere: string
        :param deadline: int
        :return: none
        '''
        problema_laborator = Problema_laborator(numar_laborator_numar_problema, descriere, deadline)
        self.__validator_problema_lab.valideaza(problema_laborator)
        if date == "memorie":
            self.__repo_probleme_lab.adauga_problema_lab(problema_laborator)
        elif date == "fisier":
            self.__repo_file_probleme_lab.adauga_problema_lab(problema_laborator)

    def cautare_laborator_dupa_numar_problema(self, nr_laborator, date):
        '''
        cauta problema_laborator dupa numarul problemei de laborator(int)
        :param nr_laborator: int
        :return: laboratorul cautat daca exista
                else repoError: problema laborator inexistenta
        '''
        if date == "memorie":
            laborator = self.__repo_probleme_lab.cauta_laborator_dupa_nr(nr_laborator)
        elif date == "fisier":
            laborator = self.__repo_file_probleme_lab.cauta_laborator_dupa_nr(nr_laborator)
        return laborator

    def modifica_problema_laborator(self, numar_problema, descriere, deadline, date):
        '''
        modifica problema de laborator cu numarul problemei transmis prin parametrul numar_problema(int)
        :param numar_problema: int
        :param descriere: string
        :param deadline: int
        :return: dictionarul probleme_lab cu problema modificata daca exista in aplicatie numarul problemei
                else repoError : problema laborator inexistenta
        '''
        problema_laborator = Problema_laborator(numar_problema, descriere, deadline)
        self.__validator_problema_lab.valideaza(problema_laborator)
        if date == "memorie":
            self.__repo_probleme_lab.modifica_problema_laborator(problema_laborator)
        elif date == "fisier":
            self.__repo_file_probleme_lab.modifica_problema_laborator(problema_laborator)
        return problema_laborator

    def generare_numar_probleme(self, x):
        '''
        genereaza x numare de problema unic identificabile
        :param x: int
        :return: lista numar_probleme cu x numere de problema unic identificabile
        '''
        numar_probleme = self.__repo_probleme_lab.generare_nr_probleme(x)
        return numar_probleme

    def generare_descriere(self, x):
        '''
        genereaza x descrieri de problema
        :param x: int
        :return: lista descriere cu x descrieri de problema
        '''
        descriere = self.__repo_probleme_lab.generare_descriere(x)
        return descriere

    def generare_deadline(self, x):
        '''
        genereaza x deadline-uri de problema
        :param x: int
        :return: lista deadline cu x deadline-uri de problema
        '''
        deadline = self.__repo_probleme_lab.generare_deadline(x)
        return deadline

    def get_all_probleme_lab(self, date):
        '''
        returneaza toata lista de probleme primita din repo_probleme_lab
        :return: self.__repo_probleme_lab daca sunt probleme in aplicatie
        '''
        if date == "memorie":
            return self.__repo_probleme_lab.get_all()
        elif date == "fisier":
            return self.__repo_file_probleme_lab.get_all()
