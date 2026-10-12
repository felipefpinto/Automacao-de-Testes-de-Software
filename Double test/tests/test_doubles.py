import pytest
from src.usuario import Usuario
from src.usuario_servico import UsuarioServico
from tests.usuario_repositorio_fake import UsuarioRepositorioFake
from tests.usuario_repositorio_spy import UsuarioRepositorioSpy


def criar_usuarios():
   
    return (
        Usuario("Ana Silva", "ana@example.com", "11900000001"),
        Usuario("Bruno Souza", "bruno@example.com", "21900000002"),
    )


def test_fake_armazena_nome_email_e_telefone():
    
    repositorio = UsuarioRepositorioFake()
    servico = UsuarioServico(repositorio)
    ana, bruno = criar_usuarios()

    
    servico.cadastrar(ana)
    servico.cadastrar(bruno)

    
    assert repositorio.buscar_todos() == [ana, bruno]
    print("FAKE: 2 usuarios armazenados com todos os campos corretos.")
    for usuario in repositorio.buscar_todos():
        print(f"  {usuario.nome} | {usuario.email} | {usuario.telefone}")


def test_spy_registra_quantidade_ordem_e_argumentos():
    
    repositorio = UsuarioRepositorioSpy()
    servico = UsuarioServico(repositorio)
    ana, bruno = criar_usuarios()

    
    servico.cadastrar(ana)
    servico.cadastrar(bruno)

    
    assert repositorio.numero_de_insercoes() == 2
    assert repositorio.chamadas[0] is ana
    assert repositorio.chamadas[1] is bruno
    print("SPY: 2 chamadas a inserir; ordem: Ana Silva, Bruno Souza.")


@pytest.mark.parametrize("campo", ["nome", "email", "telefone"])
def test_spy_nao_recebe_usuario_com_campo_vazio(campo):
    repositorio = UsuarioRepositorioSpy()
    servico = UsuarioServico(repositorio)
    dados = dict(nome="Ana Silva", email="ana@example.com", telefone="11900000001")
    dados[campo] = "   "

    with pytest.raises(ValueError, match="obrigatórios"):
        servico.cadastrar(Usuario(**dados))

    assert repositorio.numero_de_insercoes() == 0
    print(f"SPY: {campo} vazio rejeitado; 0 chamadas ao repositorio.")
