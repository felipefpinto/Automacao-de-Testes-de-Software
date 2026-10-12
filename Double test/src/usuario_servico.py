from src.usuario import Usuario
from src.usuario_repositorio import UsuarioRepositorio


class UsuarioServico:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def cadastrar(self, usuario: Usuario) -> None:
        
        if not all(campo.strip() for campo in (
            usuario.nome, usuario.email, usuario.telefone
        )):
            raise ValueError("Nome, e-mail e telefone são obrigatórios.")
        self.repositorio.inserir(usuario)
