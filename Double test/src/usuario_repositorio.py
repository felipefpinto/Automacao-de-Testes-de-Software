from abc import ABC, abstractmethod
from src.usuario import Usuario


class UsuarioRepositorio(ABC):
    @abstractmethod
    def inserir(self, usuario: Usuario) -> None:
        pass
