class Nota:
    def __init__(self, id_nota, id_student, nr_problema_laborator, nota):
        self.__id_nota = id_nota
        self.__id_student = id_student
        self.__nr_problema_laborator = nr_problema_laborator
        self.__nota = nota

    def get_nota(self):
        '''
        returneaza valoarea intreaga a notei Nota
        :return: self.__nota
        '''
        return self.__nota

    def get_id_nota(self):
        '''
        returneaza id-ul intreg al notei Nota
        :return: self.__id_nota
        '''
        return self.__id_nota

    def get_student(self):
        '''
        returneaza id_student al notei Nota
        :return: self.__id_student
        '''
        return self.__id_student

    def get_laborator(self):
        '''
        returneaza laboratorul notei Nota
        :return:self.__nr_problema_laborator
        '''
        return self.__nr_problema_laborator

    def __str__(self):
        return f"{self.__id_nota},{self.__id_student},{self.__nr_problema_laborator},{self.__nota}"

