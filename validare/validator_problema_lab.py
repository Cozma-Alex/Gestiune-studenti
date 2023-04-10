from erori.validation_error import ValidError


class ValidatorProblemaLab:
    def __init__(self):
        pass

    def valideaza(self, problema_lab):
        erori = ""
        if problema_lab.get_numar_problema_lab() <= 0:
            erori += "numar problema laborator invalid\n"
        if problema_lab.get_descriere() == "":
            erori += "descriere invalida\n"
        if problema_lab.get_deadline() < 0:
            erori += "deadline invalid\n"
        if len(erori) > 0:
            raise ValidError(erori)
