from dataclasses import dataclass


@dataclass(frozen=True)
class Usuario:
    nome: str
    email: str
    telefone: str
