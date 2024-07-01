class Aluno:
    def __init__(self, nome, idade, github, linkedin, mini_bio, foto, serie, cpf, uf, cidade):
        self.nome = nome
        self.idade = idade
        self.github = github
        self.linkedin = linkedin
        self.mini_bio = mini_bio
        self.foto = foto
        self.serie = serie
        self.cpf = cpf
        self.uf = uf
        self.cidade = cidade

class Professor:
    def __init__(self, nome, github, linkedin, bio, foto, email, telefone, idade):
        self.nome = nome
        self.github = github
        self.linkedin = linkedin
        self.bio = bio
        self.foto = foto
        self.email = email
        self.telefone = telefone
        self.idade = idade
