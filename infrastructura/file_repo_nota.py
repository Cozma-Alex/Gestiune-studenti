from domain.nota import Nota
from infrastructura.repo_nota import RepoNote


class FileRepoNote(RepoNote):

    def __init__(self, calea_catre_fisier):
        RepoNote.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._note.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_nota = int(parts[0])
                    id_student = int(parts[1])
                    nr_problema = int(parts[2])
                    valoare = int(parts[3])
                    nota = Nota(id_nota, id_student, nr_problema, valoare)
                    self._note[id_nota] = nota

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for nota in self._note.values():
                f.write(str(nota) + "\n")

    def adauga_nota(self, nota):
        self.__read_all_from_file()
        RepoNote.adauga_nota(self, nota)
        self.__write_all_to_file()

    def sterge_nota(self, id_nota):
        self.__read_all_from_file()
        RepoNote.sterge_nota(self, id_nota)
        self.__write_all_to_file()

    def modifica_nota(self, nota):
        self.__read_all_from_file()
        RepoNote.modifica_nota(self, nota)
        self.__write_all_to_file()

    def cauta_nota_dupa_id(self, id_nota):
        self.__read_all_from_file()
        return RepoNote.cauta_nota_dupa_id(self, id_nota)

    def get_all(self):
        self.__read_all_from_file()
        return RepoNote.get_all(self)

    def get_all_problema(self, nr_problema):
        self.__read_all_from_file()
        self.__write_all_to_file()
        return RepoNote.get_all_problema(self, nr_problema)

    def __len__(self):
        self.__read_all_from_file()
        return RepoNote.__len__(self)