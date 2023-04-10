from domain.problema_laborator import Problema_laborator
from infrastructura.repo_problema_lab import RepoProblemaLab


class FileRepoProblemeLab(RepoProblemaLab):

    def __init__(self, calea_catre_fisier):
        RepoProblemaLab.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._problema_lab.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    nr_problema = int(parts[0])
                    descriere = parts[1]
                    deadline = int(parts[2])
                    problema_laborator = Problema_laborator(nr_problema, descriere, deadline)
                    self._problema_lab[nr_problema] = problema_laborator

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for problema in self._problema_lab.values():
                f.write(str(problema) + "\n")

    def adauga_problema_lab(self, problema_laborator):
        self.__read_all_from_file()
        RepoProblemaLab.adauga_problema_lab(self, problema_laborator)
        self.__write_all_to_file()

    def modifica_problema_laborator(self, problema_lab):
        self.__read_all_from_file()
        RepoProblemaLab.modifica_problema_laborator(self, problema_lab)
        self.__write_all_to_file()

    def sterge_laborator_dupa_numar(self, nr_problema):
        self.__read_all_from_file()
        RepoProblemaLab.sterge_laborator_dupa_numar(self, nr_problema)
        self.__write_all_to_file()

    def cauta_laborator_dupa_nr(self, nr_problema):
        self.__read_all_from_file()
        return RepoProblemaLab.cauta_laborator_dupa_nr(self, nr_problema)

    def get_all(self):
        self.__read_all_from_file()
        self.__write_all_to_file()
        return RepoProblemaLab.get_all(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoProblemaLab.__len__(self)