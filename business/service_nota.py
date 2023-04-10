from domain.nota import Nota


class ServiceNota:
    def __init__(self, validator_nota, repo_note, repo_studenti, repo_probleme_lab, repo_file_note, repo_file_student, repo_file_problema_lab):
        self.__validator_nota = validator_nota
        self.__repo_note = repo_note
        self.__repo_studenti = repo_studenti
        self.__repo_probleme_lab = repo_probleme_lab
        self.__repo_file_note = repo_file_note
        self.__repo_file_student = repo_file_student
        self.__repo_file_probleme_lab = repo_file_problema_lab

    def adauga_nota(self, id_nota, id_student, nr_problema, valoare, date):
        '''
        creeaza o nota pe baza id_nota int si unic identificabila, id_student int, nr_problema int, valoare int
        valideaza nota si daca este valida se va adauga la repo_note
        verifica daca exista un student cu id_student int
        verifica daca exista o problema de laborator cu nr_problema int
        :param id_nota:
        :param id_student:
        :param nr_problema:
        :param valoare:
        :return: none
        '''
        nota = Nota(id_nota, id_student, nr_problema, valoare)
        self.__validator_nota.valideaza(nota)
        if date == "memorie":
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            problema_laborator = self.__repo_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            self.__repo_note.adauga_nota(nota)
        elif date == "fisier":
            student = self.__repo_file_student.cauta_student_dupa_id(id_student)
            problema_laborator = self.__repo_file_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            self.__repo_file_note.adauga_nota(nota)

    def sterge_laborator_si_note(self, nr_laborator, date):
        '''
        sterge un laborator pe baza numarului problemei de laborator
        de asemenea sterge notele de la laboratorul respectiv
        :param nr_laborator:int
        :return: repo-ul de probleme laborator dupa ce a fost efectuata stergerea
        '''
        if date == "memorie":
            problema_laborator = self.__repo_probleme_lab.cauta_laborator_dupa_nr(nr_laborator)
            note = self.__repo_note.get_all()
            note_laborator = [x for x in note if x.get_laborator() == nr_laborator]
            for nota_laborator in note_laborator:
                self.__repo_note.sterge_nota(nota_laborator.get_id_nota())
            self.__repo_probleme_lab.sterge_laborator_dupa_numar(nr_laborator)
        elif date == "fisier":
            problema_laborator = self.__repo_file_probleme_lab.cauta_laborator_dupa_nr(nr_laborator)
            note = self.__repo_file_note.get_all()
            note_laborator = [x for x in note if x.get_laborator() == nr_laborator]
            for nota_laborator in note_laborator:
                self.__repo_file_note.sterge_nota(nota_laborator.get_id_nota())
            self.__repo_file_probleme_lab.sterge_laborator_dupa_numar(nr_laborator)

    def sterge_student_si_note(self, id_student, date):
        '''
        sterge un student pe baza id-ului sau
        de asemenea sterge notele atribuite acestuia
        :param id_student: int
        :return: repo-ul de studenti dupa ce a fost efectuata stergerea
        '''
        if date == "memorie":
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            note = self.__repo_note.get_all()
            note_student = [x for x in note if x.get_student() == id_student]
            for nota_student in note_student:
                self.__repo_note.sterge_nota(nota_student.get_id_nota())
            self.__repo_studenti.sterge_student_dupa_id(id_student)
        elif date == "fisier":
            student = self.__repo_file_student.cauta_student_dupa_id(id_student)
            note = self.__repo_file_note.get_all()
            note_student = [x for x in note if x.get_student() == id_student]
            for nota_student in note_student:
                self.__repo_file_note.sterge_nota(nota_student.get_id_nota())
            self.__repo_file_student.sterge_student_dupa_id(id_student)

    def sterge_nota(self, id_nota, date):
        '''
        sterge nota unui student la un laborator dupa un id_nota
        se verifica existenta notei cu id_nota
        :param id_nota:
        :return: none
        '''
        if date == "memorie":
            self.__repo_note.sterge_nota(id_nota)
        elif date == "fisier":
            self.__repo_file_note.sterge_nota(id_nota)

    def modifica_nota(self, id_nota, id_student, nr_problema, valoare, date):
        '''
        modifica o nota dupa id_nota
        creeaza nota noua
        valideaza datele notei noi
        verifica daca nota cu id_nota exista
        verifica daca studentul cu id_student exista
        verifica daca problema de laborator cu nr_problema exista
        :param id_nota: int
        :param id_student: int
        :param nr_problema: int
        :param valoare: int
        :return: none
        '''
        nota = Nota(id_nota, id_student, nr_problema, valoare)
        self.__validator_nota.valideaza(nota)
        if date == "memorie":
            nota_c = self.__repo_note.cauta_nota_dupa_id(id_nota)
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            probl_laborator = self.__repo_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            self.__repo_note.modifica_nota(nota)
        elif date == "fisier":
            nota_c = self.__repo_file_note.cauta_nota_dupa_id(id_nota)
            student = self.__repo_file_student.cauta_student_dupa_id(id_student)
            probl_laborator = self.__repo_file_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            self.__repo_file_note.modifica_nota(nota)

    def cauta_nota_dupa_id(self, id_nota, date):
        '''
        efectueaza cautarea dupa id a notei in repo_note
        :param id_nota: int
        :return: nota - daca este gasita
                 else repoError : nota inexistenta
        '''
        if date == "memorie":
            nota = self.__repo_note.cauta_nota_dupa_id(id_nota)
        elif date == "fisier":
            nota = self.__repo_file_note.cauta_nota_dupa_id(id_nota)
        return nota

    def lista_studenti_alfabetic(self, note, date, modalitate):
        '''
        cauta studentii care au nota primita la laboratorul note[i].get_laborator() oricare i intre 0 si len(note)-1
        :param note: lista cu note de tip Nota
        :return: lista  cu studentii care au primit nota la laborator
        '''
        lista = []
        if date == "memorie":
            for nota in note:
                id_student = nota.get_student()
                lista.append(self.__repo_studenti.cauta_student_dupa_id(id_student))
            lista = self.sorting(lista, modalitate, self.criteriu_student, self.criteriu_grupa)
        elif date == "fisier":
            for nota in note:
                id_student = nota.get_student()
                lista.append(self.__repo_file_student.cauta_student_dupa_id(id_student))
            lista = self.sorting(lista, modalitate, self.criteriu_student, self.criteriu_grupa)
        return lista

    def criteriu_student(self, e):
        e.get_nume()

    def lista_note_alfabetic(self, nr_problema, date):
        '''
        lista cu notele de la laboratorul cu numarul de problema nr_problema
        :param nr_problema: int
        :return: lista_note - lista cu notele de la laborator, notele de tip Nota
        '''
        if date == "memorie":
            self.__repo_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            lista_note = self.__repo_note.get_all_problema(nr_problema)
        elif date == "fisier":
            self.__repo_file_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            lista_note = self.__repo_file_note.get_all_problema(nr_problema)
        return lista_note

    def shell_sort(self, lista, lungime, key):
        '''
        sorteaza alfabetic dupa nume lista de studenti primita ca parametru
        :param lista: lista de studenti de tip Student
        :return: lista de studenti de tip Student ordonata alfabetic dupa nume
        '''
        interval = lungime // 2
        while interval > 0:
            for i in range(interval, lungime):
                aux = lista[i]
                j = i
                while j >= interval and key(lista[j - interval]) > key(aux):
                    lista[j] = lista[j - interval]
                    j -= interval
                lista[j] = aux
            interval //= 2
        return lista

    def lista_note_definitorie_alfabetic(self, lista_studenti, lista_note):
        '''
        se creeaza lista finala in care apar studentii alaturi de notele lor
        :param lista_studenti: lista de studenti cu studenti de tip Student
        :param lista_note: lista de note cu note de tip Nota
        :return: lista_definitorie cu numele si nota fiecarui elev de la laboratorul lista_note[i].get_laborator() oricare i intre 0 si len(lista_note)-1
        '''
        lista_definitorie = []
        for student in lista_studenti:
            lista = [student.get_nume()]
            for i in range(0, len(lista_note)):
                if lista_note[i].get_student() == student.get_id_student():
                    lista.append(lista_note[i].get_nota())
            lista_definitorie.append(lista)
        return lista_definitorie

    def lista_note_crescator(self, nr_problema, date, modalitate):
        '''
        lista cu notele de la laboratorul cu numarul de problema nr_problema
        :param nr_problema: int
        :return: lista_note - lista cu notele de la laborator, notele de tip Nota sortata crescator in functie de valoarea notei
        '''
        if date == "memorie":
            self.__repo_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            lista_note = self.__repo_note.get_all_problema(nr_problema)
        elif date == "fisier":
            self.__repo_file_probleme_lab.cauta_laborator_dupa_nr(nr_problema)
            lista_note = self.__repo_file_note.get_all_problema(nr_problema)
        lista_note = self.sorting(lista_note, modalitate, self.criteriu_nota, self.criteriu_student)
        return lista_note

    def criteriu_nota(self, e):
        return e.get_nota()

    def criteriu_grupa(self, e):
        return e.get_grupa()

    def bubble_sort(self, lista, key1, key2):
        '''
        sorteaza crescator lista de note de tip Nota in functie de valoarea notei
        :param lista_note: lista cu note de tip Nota
        :return: lista_note cu note de tip Nota ordonata crescator in functie de nota
        '''
        swap = False
        for i in range(0, len(lista)):
            for j in range(0, len(lista) - i - 1):
                if key1(lista[j]) > key1(lista[j+1]):
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    swap = True
                if key1(lista[j]) == key1(lista[j+1]) and key2(lista[j]) > key2(lista[j+1]):
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    swap = True
                if not swap:
                    break
        return lista

    def lista_definitorie_crescator(self, lista_note, date):
        '''
        lista finala cu notele ordonate crescator si studentii carora le apartin notele
        :param lista_note: lista cu note de tip Nota ordonate crescator in functie de valoarea notei
        :return: lista_definitorie - lista in care sunt alaturate numele studentilor si notele acestora
        '''
        lista_definitorie = []
        if date == "memorie":
            for nota in lista_note:
                lista = []
                student = self.__repo_studenti.cauta_student_dupa_id(nota.get_student())
                lista.append(student.get_nume())
                lista.append(nota.get_nota())
                lista_definitorie.append(lista)
        elif date == "fisier":
            for nota in lista_note:
                lista = []
                student = self.__repo_file_student.cauta_student_dupa_id(nota.get_student())
                lista.append(student.get_nume())
                lista.append(nota.get_nota())
                lista_definitorie.append(lista)
        return lista_definitorie

    def nota_sub_5(self, lista_note, lista_studenti, lista_medie_student, q):
        '''
        se creeaza lista lista_medie_student in care sunt stocate mediile studentilor si numele acestora daca au media sub 5
        :param lista_note: lista de note de tip Nota
        :param lista_studenti: lista de studenti de tip Student
        :return: lista_medie_student cu numele studentului si media acestuia

        complexitate:Fie n=len(lista_studenti) si m=len(lista_note) atunci complexitatea este 3n*2m => O(n*m)
        '''
        nr_studenti = len(lista_studenti)
        if q < nr_studenti:
            id_student = lista_studenti[q].get_id_student()
            lista = [0, 0]
            for nota in lista_note:
                if nota.get_student() == id_student:
                    lista[0] += nota.get_nota()
                    lista[1] += 1
            if lista[1] != 0:
                medie = lista[0] / lista[1]
                if medie < 5:
                    lista[0] = lista_studenti[q].get_nume()
                    lista[1] = medie
                    lista_medie_student.append(lista)
            q = q + 1
            self.nota_sub_5(lista_note, lista_studenti, lista_medie_student, q)
        return lista_medie_student

    def medie_dupa_litera(self, lista_note, lista_studenti, lista_medie_student, q):
        '''
        preia numele din lista de studenti si notele acelui student si returneaza o lista in care sunt alaturate numele
        si media la toate laboratorarele ale acestuia
        :param lista_note: lista de note de tip Nota
        :param lista_studenti: lista de studenti de tip Student
        :return: lista lista_medie_student in care sunt alaturate numele studentilor

        complexitate:Fie n=len(lista_studenti) si m=len(lista_note) atunci complexitatea este 2n*2m => O(n*m)
        '''
        nr_studenti = len(lista_studenti)
        if q < nr_studenti:
            id_student = lista_studenti[q].get_id_student()
            lista = [0, 0]
            for nota in lista_note:
                if nota.get_student() == id_student:
                    lista[0] += nota.get_nota()
                    lista[1] += 1
            if lista[1] != 0:
                medie = lista[0] / lista[1]
                lista[0] = lista_studenti[q].get_nume()
                lista[1] = medie
                lista_medie_student.append(lista)
            q = q + 1
            self.medie_dupa_litera(lista_note, lista_studenti, lista_medie_student, q)
        return lista_medie_student

    def get_all_note(self, date):
        '''
        returneaza lista tuturor notelor primita din repo_note
        :return: lista de note din repo_note
        '''
        if date == "memorie":
            return self.__repo_note.get_all()
        elif date == "fisier":
            return self.__repo_file_note.get_all()

    def sorting(self, lista_note, modalitate, key1, key2):
        if modalitate == "bubble":
            return self.bubble_sort(lista_note, key1, key2)
        else:
            return self.shell_sort(lista_note, len(lista_note), key1)