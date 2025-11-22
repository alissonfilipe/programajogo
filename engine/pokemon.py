# engine/pokemon.py
from typing import List
from engine.habilidade import Habilidade

class Pokemon:
    def __init__(self,
                 nome: str,
                 hp: int,
                 forca: int,
                 resistencia: int,
                 atk_especial: int,
                 def_especial: int,
                 velocidade: int,
                 agilidade: int,
                 tipos: List[str],
                 habilidades: List[Habilidade]):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.forca = forca
        self.resistencia = resistencia
        self.atk_especial = atk_especial
        self.def_especial = def_especial
        self.velocidade = velocidade
        self.agilidade = agilidade
        self.tipos = tipos
        self.habilidades = habilidades

    def esta_vivo(self) -> bool:
        return self.hp > 0

    def atacar(self, alvo: "Pokemon") -> int:
        """
        Dano simples: forca - resistencia.
        Garante minimo 1 de dano.
        Retorna o dano causado.
        """
        dano = self.forca - alvo.resistencia
        if dano < 1:
            dano = 1
        alvo.hp -= dano
        return dano

    @classmethod
    def from_dict(cls, data: dict) -> "Pokemon":
        # converte lista de habilidades (dicts) em objetos Habilidade
        habs = []
        for h in data.get("habilidades", []):
            # h pode ser string ou dict; tratar ambos
            if isinstance(h, dict):
                nome = h.get("nome") or h.get("descricao") or "habilidade"
                descricao = h.get("descricao", "")
            else:
                nome = str(h)
                descricao = ""
            habs.append(Habilidade(nome, descricao))

        return cls(
            nome=data.get("nome", "SemNome"),
            hp=int(data.get("hp", 1)),
            forca=int(data.get("forca", 1)),
            resistencia=int(data.get("resistencia", 0)),
            atk_especial=int(data.get("atk_especial", 0)),
            def_especial=int(data.get("def_especial", 0)),
            velocidade=int(data.get("velocidade", 0)),
            agilidade=int(data.get("agilidade", 0)),
            tipos=data.get("tipos", []),
            habilidades=habs
        )

    def __repr__(self):
        return f"<Pokemon {self.nome} HP={self.hp}/{self.hp_max}>"
