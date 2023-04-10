from domain.student import Student


class ServiceStudenti:
    def __init__(self, validator_student, repo_studenti, repo_file_studenti):
        self.__validator_student = validator_student
        self.__repo_student = repo_studenti
        self.__repo_file_student = repo_file_studenti

    def adauga_student(self, id_student, nume, grupa, date):
        '''
        creeaza un student pe baza id_student int, nume string, grupa int
        valideaza studentul si daca e valid o adauga la repo_studenti
        :param id_student: int
        :param nume: string
        :param grupa: int
        :return: none
        '''
        student = Student(id_student, nume, grupa)
        self.__validator_student.valideaza(student)
        if date == "memorie":
            self.__repo_student.adauga_student(student)
        elif date == "fisier":
            self.__repo_file_student.adauga_student(student)

    def cautare_dupa_id(self, id_student, date):
        '''
        efectueaza cautarea dupa id in repo_student
        :param id_student: int
        :return: student - daca este gasit
                else repoError : student inexistent
        '''
        if date == "memorie":
            student = self.__repo_student.cauta_student_dupa_id(id_student)
        elif date == "fisier":
            student = self.__repo_file_student.cauta_student_dupa_id(id_student)
        return student

    def modifica_student(self, id_student, nume, grupa, date):
        '''
        modifica un student dupa id
        :param id_student: int
        :param nume: string
        :param grupa: int
        :return: dictionarul studenti cu studentul modificat daca exista studentul cu acel id
                else repoError : student inexistent
        '''
        student = Student(id_student, nume, grupa)
        self.__validator_student.valideaza(student)
        if date == "memorie":
            self.__repo_student.modifica_student(student)
        elif date == "fisier":
            self.__repo_file_student.modifica_student(student)
        return student

    def generare_id_studenti(self, x):
        '''
        genereaza x id-uri de studenti unic identificabile
        :param x: int
        :return: lista id_studenti cu x id-uri de studenti unic identificabile
        '''
        id_studenti = self.__repo_student.generare_id_studenti(x)
        return id_studenti

    def generare_nume(self, x):
        '''
        genereaza x nume de studenti
        :param x: int
        :return: lista nume cu x nume
        '''
        nume = self.__repo_student.generare_nume(x)
        return nume

    def generare_grupa(self, x):
        '''
        genereaza x grupe
        :param x: int
        :return: lista grupe cu x grupe
        '''
        grupe = self.__repo_student.generare_grupa(x)
        return grupe

    def get_all_litera(self, l, date):
        '''
        returneaza lista studentilor al caror nume incepe cu litera stocata in variabila l string
        :param l: string
        :return: lista_studenti_valid lista studentilor de tip Student al caror nume incepe cu litera stocata in variabila l string
        '''
        lista_studenti_valid = []
        if date == "memorie":
            lista_studenti = self.__repo_student.get_all()
        elif date == "fisier":
            lista_studenti = self.__repo_file_student.get_all()
        for student in lista_studenti:
            nume = student.get_nume()
            if nume[0] == l:
                lista_studenti_valid.append(student)
        return lista_studenti_valid

    def get_all_studenti(self, date):
        '''
        returneaza lista tuturor studentilor primita din repo_student
        :return: lista de studenti din repo_studenti
        '''
        if date == "memorie":
            return self.__repo_student.get_all()
        elif date == "fisier":
            return self.__repo_file_student.get_all()
