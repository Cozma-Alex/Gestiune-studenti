from erori.repo_error import RepoError
from erori.validation_error import ValidError


class UI:
    def __init__(self, service_studenti, service_probleme_lab, service_note):
        self.__service_studenti = service_studenti
        self.__service_probleme_lab = service_probleme_lab
        self.__service_note = service_note
        self.__comenzi = {
            "adauga_student": self.__ui_adauga_student,
            "adauga_x_studenti": self.__ui_adauga_x_studenti,
            "sterge_student": self.__ui_sterge_student_dupa_id,
            "print_studenti": self.__ui_print_studenti,
            "print_note": self.__ui_print_note,
            "cauta_student_dupa_id": self.__ui_cautare_studen_dupa_id,
            "modifica_student": self.__ui_modificare_student,
            "adauga_laborator": self.__ui_adauga_laborator,
            "adauga_x_laboratoare": self.__ui_adauga_x_laboratoare,
            "print_laboratoare": self.__ui_print_laboratoare,
            "cauta_laborator_dupa_numar_problema": self.__ui_cautare_laborator_dupa_numar_problema,
            "sterge_laborator" : self.__ui_sterge_laborator_dupa_nr,
            "modifica_laborator": self.__ui_modificare_laborator,
            "adauga_nota": self.__ui_adauga_nota,
            "sterge_nota": self.__ui_sterge_nota,
            "modifica_nota": self.__ui_modifica_nota,
            "cauta_nota_dupa_id": self.__ui_cauta_nota_dupa_id,
            "lista_studenti_alfabetica": self.__ui_lista_studenti_alfabetic,
            "lista_studenti_dupa_nota": self.__ui_lista_studenti_dupa_nota,
            "media_sub_5": self.__ui_lista_studenti_nota_sub_5,
            "media_dupa_litera": self.__ui_media_dupa_litera
        }

    def __ui_adauga_student(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grupa = int(self.__params[2])
        date = self.__params[3]
        self.__service_studenti.adauga_student(id_student, nume, grupa, date)
        print("student adaugat cu succes!")

    def __ui_print_studenti(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        date = self.__params[0]
        studenti = self.__service_studenti.get_all_studenti(date)
        if len(studenti) == 0:
            print("nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)

    def __ui_adauga_x_studenti(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        x = int(self.__params[0])
        date = self.__params[1]
        id_studenti = self.__service_studenti.generare_id_studenti(x)
        nume = self.__service_studenti.generare_nume(x)
        grupa = self.__service_studenti.generare_grupa(x)
        for i in range(0, x):
            self.__service_studenti.adauga_student(id_studenti[i], nume[i], grupa[i], date)
        print("studenti adaugati cu succes!")

    def __ui_cautare_studen_dupa_id(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        date = self.__params[1]
        studentul = self.__service_studenti.cautare_dupa_id(id_student, date)
        print(studentul)

    def __ui_modificare_student(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grupa = int(self.__params[2])
        date = self.__params[3]
        studenti = self.__service_studenti.modifica_student(id_student, nume, grupa, date)
        print("student modificat cu succes!")

    def __ui_sterge_student_dupa_id(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        date = self.__params[1]
        self.__service_note.sterge_student_si_note(id_student, date)
        print("student sters cu succes!")

    def __ui_adauga_x_laboratoare(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        x = int(self.__params[0])
        date = self.__params[1]
        numar_probleme = self.__service_probleme_lab.generare_numar_probleme(x)
        descriere = self.__service_probleme_lab.generare_deslcriere(x)
        deadline = self.__service_probleme_lab.generare_deadline(x)
        for i in range(0, x):
            self.__service_probleme_lab.adauga_problema_laborator(numar_probleme[i], descriere[i], deadline[i], date)
        print("laboratoare adaugate cu succes!")

    def __ui_modificare_laborator(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        nr_problema = int(self.__params[0])
        descriere = self.__params[1]
        deadline = int(self.__params[2])
        date = self.__params[3]
        probleme_laborator = self.__service_probleme_lab.modifica_problema_laborator(nr_problema, descriere, deadline, date)
        print("problema laborator modificata cu succes!")

    def __ui_cautare_laborator_dupa_numar_problema(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        nr_problema = int(self.__params[0])
        date = self.__params[1]
        laboratorul = self.__service_probleme_lab.cautare_laborator_dupa_numar_problema(nr_problema, date)
        print(laboratorul)

    def __ui_sterge_laborator_dupa_nr(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        nr_laborator = int(self.__params[0])
        date = self.__params[1]
        self.__service_note.sterge_laborator_si_note(nr_laborator, date)
        print("laborator sters cu succes!")

    def __ui_adauga_laborator(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        numar_laborator_numar_problema = int(self.__params[0])
        descriere = self.__params[1]
        deadline = int(self.__params[2])
        date = self.__params[3]
        self.__service_probleme_lab.adauga_problema_laborator(numar_laborator_numar_problema, descriere, deadline, date)
        print("problema adaugata cu succes!")

    def __ui_print_laboratoare(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        date = self.__params[0]
        probleme_laborator = self.__service_probleme_lab.get_all_probleme_lab(date)
        if len(probleme_laborator) == 0:
            print("nu exista probleme in aplicatie!")
            return
        for problema_laborator in probleme_laborator:
            print(problema_laborator)

    def __ui_adauga_nota(self):
        if len(self.__params) != 5:
            print("numar parametri invalid!")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        nr_problema = int(self.__params[2])
        valoare = int(self.__params[3])
        date = self.__params[4]
        self.__service_note.adauga_nota(id_nota, id_student, nr_problema, valoare, date)
        print("nota adaugata cu succes!")

    def __ui_print_note(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        date = self.__params[0]
        note = self.__service_note.get_all_note(date)
        if len(note) == 0:
            print("nu exista note in aplicatie!")
            return
        for nota in note:
            print(nota)

    def __ui_sterge_nota(self):
        if len(self.__params) != 2:
            print("numar parametri invalid!")
            return
        id_nota = int(self.__params[0])
        date = self.__params[1]
        self.__service_note.sterge_nota(id_nota, date)
        print("nota stearsa cu succes!")

    def __ui_modifica_nota(self):
        if len(self.__params) != 5:
            print("numar parametrii invalid!")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        nr_problema = int(self.__params[2])
        valoare = int(self.__params[3])
        date = self.__params[4]
        self.__service_note.modifica_nota(id_nota, id_student, nr_problema, valoare, date)
        print("nota modificata cu succes!")

    def __ui_cauta_nota_dupa_id(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_nota = int(self.__params[0])
        date = self.__params[1]
        nota = self.__service_note.cauta_nota_dupa_id(id_nota, date)
        print(nota)

    def __ui_lista_studenti_alfabetic(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        nr_problema = int(self.__params[0])
        date = self.__params[1]
        lista_note = self.__service_note.lista_note_alfabetic(nr_problema, date)
        lista_studenti = self.__service_note.lista_studenti_alfabetic(lista_note, date)
        lista_note_studenti = self.__service_note.lista_note_definitorie_alfabetic(lista_studenti, lista_note)
        for student in lista_note_studenti:
            print(student)

    def __ui_lista_studenti_dupa_nota(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        nr_problema = int(self.__params[0])
        date = self.__params[1]
        modalitate = self.__params[2]
        lista_note = self.__service_note.lista_note_crescator(nr_problema, date, modalitate)
        lista_studenti_note = self.__service_note.lista_definitorie_crescator(lista_note, date)
        for student in lista_studenti_note:
            print(student)

    def __ui_lista_studenti_nota_sub_5(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        date = self.__params[0]
        lista_note = self.__service_note.get_all_note(date)
        lista_studenti = self.__service_studenti.get_all_studenti(date)
        q = 0
        lista_studenti_medie = []
        lista_studenti_medie = self.__service_note.nota_sub_5(lista_note, lista_studenti, lista_studenti_medie, q)
        if len(lista_studenti_medie) == 0:
            print("nu exista studenti cu media mai mica decat 5!")
        for student in lista_studenti_medie:
            print(student)

    def __ui_media_dupa_litera(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        l = self.__params[0]
        date = self.__params[1]
        lista_note = self.__service_note.get_all_note(date)
        lista_studenti = self.__service_studenti.get_all_litera(l, date)
        q = 0
        lista_studenti_medie = []
        lista_studenti_medie = self.__service_note.medie_dupa_litera(lista_note, lista_studenti, lista_studenti_medie, q)
        for student in lista_studenti_medie:
            print(student)

    def run(self):
        while True:
            comanda = input(">>>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parts = comanda.split()
            nume_comanda = parts[0]
            self.__params = parts[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("comanda invalida")


