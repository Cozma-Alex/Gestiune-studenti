class Student:
    def __init__(self, id_student, nume, grupa):
        self.__id_student = id_student
        self.__nume = nume
        self.__grupa = grupa

    def get_id_student(self):
        '''
        returneaza id-ul intreg al studentului Student
        :return:self.__id_student
        '''
        return self.__id_student

    def get_nume(self):
        '''
        returneaza numele string al studentului Student
        :return: self.__nume
        '''
        return self.__nume

    def get_grupa(self):
        '''
        returneaza grupa intreaga a studentului Student
        :return: self.__grupa
        '''
        return self.__grupa

    def __str__(self):
        return f"{self.__id_student},{self.__nume},{self.get_grupa()}"

    def __repr__(self):
        return repr((self.__id_student, self.__nume, self.__grupa))