from domain.student import Student
from infrastructura.repo_student import RepoStudenti


class FileRepoStudenti(RepoStudenti):

    def __init__(self, calea_catre_fisier):
        RepoStudenti.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_student = int(parts[0])
                    nume = parts[1]
                    grupa = int(parts[2])
                    student = Student(id_student, nume, grupa)
                    self._studenti[id_student] = student

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for student in self._studenti.values():
                f.write(str(student) + "\n")

    def adauga_student(self, student):
        self.__read_all_from_file()
        RepoStudenti.adauga_student(self, student)
        self.__write_all_to_file()

    def modifica_student(self, student):
        self.__read_all_from_file()
        RepoStudenti.modifica_student(self, student)
        self.__write_all_to_file()

    def sterge_student_dupa_id(self, id_student):
        self.__read_all_from_file()
        RepoStudenti.sterge_student_dupa_id(self, id_student)
        self.__write_all_to_file()

    def cauta_student_dupa_id(self, id_student):
        self.__read_all_from_file()
        return RepoStudenti.cauta_student_dupa_id(self, id_student)

    def get_all(self):
        self.__read_all_from_file()
        self.__write_all_to_file()
        return RepoStudenti.get_all(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoStudenti.__len__(self)
