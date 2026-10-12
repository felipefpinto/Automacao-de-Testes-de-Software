from src.usuario import Usuario
from src.usuario_repositorio import UsuarioRepositorio


class UsuarioRepositorioFake(UsuarioRepositorio):


    def __init__(self):
        self._usuarios: list[Usuario] = []

    def inserir(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def buscar_todos(self) -> list[Usuario]:
        return list(self._usuarios)

    def obter_tamanho(self) -> int:
        return len(self._usuarios)
