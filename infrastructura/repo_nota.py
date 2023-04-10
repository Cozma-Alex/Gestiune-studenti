from erori.repo_error import RepoError


class RepoNote:
    def __init__(self):
        self._note = {}

    def adauga_nota(self, nota):
        '''
        adauga la dictionarul note nota unic identificabila prin id_nota daca nu apare deja in dictionar
        :param nota: int
        :return: none
        '''
        if nota.get_id_nota() in self._note:
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()] = nota

    def sterge_nota(self, id_nota):
        '''
        sterge din dictionarul note nota cu id_nota unic identificabil daca se regaseste in dictionarul note
        :param id_nota: int
        :return: none
        '''
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
        del(self._note[id_nota])

    def modifica_nota(self, nota):
        '''
        modifica nota din dictionarul note id_note unic identificabil daca apare in dictionar
        :param nota: nota
        :return: none
        '''
        if nota.get_id_nota() not in self._note:
            raise RepoError("nota inexistenta!")
            return
        self._note[nota.get_id_nota()] = nota

    def cauta_nota_dupa_id(self, id_nota):
        '''
        cauta in dictionarul note nota cu id_nota unic identificabil daca apare in dictionar
        :param id_nota: int
        :return: nota cu id-ul unic identificabil id_nota
        '''
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
            return
        return self._note[id_nota]

    def get_all(self):
        '''
        returneaza toate notele cu id unic identificabil care se gasesc in dictionarul note
        :return: lista note cu toate notele cu id unic identificabil din dictionarul note
        '''
        note = []
        for nota_id in self._note:
            note.append(self._note[nota_id])
        return note

    def get_all_problema(self, nr_problema):
        '''
        returneaza toate notele cu id unic identificabil care corespund unui laborator
        :param nr_problema: int
        :return: lista note cu toate notele cu id unic identificabil din dictionarul note care au numarul de problema nr_problema
        '''
        note = []
        for nota_id in self._note:
            if self._note[nota_id].get_laborator() == nr_problema:
                note.append(self._note[nota_id])
        return note

    def __len__(self):
        '''
        returneaza numarul de elemente din dictionarul note
        :return: numarul de elemente din dictionarul note
        '''
        return len(self._note)