from src.usuario import Usuario
from src.usuario_repositorio import UsuarioRepositorio


class UsuarioRepositorioSpy(UsuarioRepositorio):
    
    def __init__(self):
        self.chamadas: list[Usuario] = []

    def inserir(self, usuario: Usuario) -> None:
        self.chamadas.append(usuario)

    def numero_de_insercoes(self) -> int:
        return len(self.chamadas)
