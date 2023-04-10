from validare.validator_student import ValidatorStudent
from validare.validator_problema_lab import ValidatorProblemaLab
from validare.validator_nota import ValidatorNota
from business.service_nota import ServiceNota
from business.service_problema_lab import ServiceProblemaLab
from business.service_student import ServiceStudenti
from infrastructura.repo_nota import RepoNote
from infrastructura.repo_problema_lab import RepoProblemaLab
from infrastructura.repo_student import RepoStudenti
from prezentare.consola import UI
from infrastructura.file_repo_student import FileRepoStudenti
from infrastructura.file_repo_nota import FileRepoNote
from infrastructura.file_repo_problema_lab import FileRepoProblemeLab

if __name__ == '__main__':
    validator_student = ValidatorStudent()
    validator_problema_lab = ValidatorProblemaLab()
    validator_nota = ValidatorNota()
    repo_studenti = RepoStudenti()
    repo_probleme_lab = RepoProblemaLab()
    repo_note = RepoNote()
    fisier_studenti = "studenti.txt"
    repo_file_studenti = FileRepoStudenti(fisier_studenti)
    fisier_note = "note.txt"
    repo_file_note = FileRepoNote(fisier_note)
    fisier_probleme = "probleme_lab.txt"
    repo_file_probleme_lab = FileRepoProblemeLab(fisier_probleme)
    service_note = ServiceNota(validator_nota, repo_note, repo_studenti, repo_probleme_lab, repo_file_note, repo_file_studenti, repo_file_probleme_lab)
    service_studenti = ServiceStudenti(validator_student, repo_studenti, repo_file_studenti)
    service_probleme_lab = ServiceProblemaLab(validator_problema_lab, repo_probleme_lab, repo_file_probleme_lab)
    consola = UI(service_studenti, service_probleme_lab, service_note)
    consola.run()
