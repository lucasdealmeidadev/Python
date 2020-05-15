from random import randint;

class Autor():
    def __init__(self, id, nome):
        self.id    = id;
        self.nome  = nome;
    
    #GET
    def getId(self):
        return self.id;
    
    def getNome(self):
        return self.nome;
    
    #SET
    def setId(self, id):
        self.id = id;
    
    def setNome(self, nome):
        self.nome = nome;
    
class Livro():
    def __init__(self, autor, id, nome):
        self.autor = Autor(randint(0,9), autor);
        self.id    = id;
        self.nome  = nome;

    #GET LIVRO
    def getId(self):
        return self.id;

    def getNome(self):
        return self.nome;

    #SET LIVRO
    def setId(self, id):
        self.id = id;

    def setNome(self, nome):
        self.nome = nome;

    #GET AUTOR
    def getIdAutor(self):
        return self.autor.getId();
    
    def getAutor(self):
        return self.autor.getNome();

    #SET AUTOR
    def setIdAutor(self, id):
        self.autor.setId(id);
    
    def setAutor(self, autor):
        self.autor.setNome(autor);