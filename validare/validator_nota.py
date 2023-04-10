from erori.validation_error import ValidError


class ValidatorNota:
    def __init__(self):
        pass

    def valideaza(self, nota):
        erori = ""
        if nota.get_id_nota() <= 0:
            erori += "id nota invalid\n"
        if nota.get_student() <= 0:
            erori += "id student invalid\n"
        if nota.get_laborator() <= 0:
            erori += "numar problema laborator invalid\n"
        if nota.get_nota() <= 0 or nota.get_nota() > 10:
            erori += "valoare nota invalida\n"
        if len(erori) > 0:
            raise ValidError(erori)