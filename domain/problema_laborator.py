class Problema_laborator:
    def __init__(self, numar_laborator_numar_problema, descriere, deadline):
        self.__numar_laborator_numar_problema = numar_laborator_numar_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_numar_problema_lab(self):
        '''
        returneaza numarul de problema de laborator intreg al problemei de laborator Problema_laborator
        :return:
        '''
        return self.__numar_laborator_numar_problema

    def get_descriere(self):
        '''
        returneaza descrierea string al problemei de laborator Problema_laborator
        :return:
        '''
        return self.__descriere

    def get_deadline(self):
        '''
        returneaza deadline-ul intreg al problemei de laborator Problema_laborator
        :return:
        '''
        return self.__deadline

    def __str__(self):
        return f"{self.__numar_laborator_numar_problema},{self.__descriere},{self.__deadline}"
