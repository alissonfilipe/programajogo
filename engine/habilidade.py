# engine/habilidade.py

class Habilidade:
    """
    Representa uma habilidade simples.
    Por enquanto só guarda nome e descricao.
    Futuramente pode ter 'efeito' (callable) ou parametros.
    """
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return f"Habilidade(nome={self.nome!r})"
