from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "API de Gerenciador de Tarefas"}


def test_criar_tarefa():
    resposta = client.post(
        "/tarefas",
        json={"titulo": "Estudar Python", "descricao": "Revisar POO"},
    )
    assert resposta.status_code == 201
    dados = resposta.json()
    assert dados["titulo"] == "Estudar Python"
    assert dados["concluida"] is False


def test_listar_tarefas():
    resposta = client.get("/tarefas")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)


def test_buscar_tarefa_inexistente():
    resposta = client.get("/tarefas/99999")
    assert resposta.status_code == 404


def test_atualizar_tarefa():
    # primeiro cria uma tarefa
    criada = client.post(
        "/tarefas",
        json={"titulo": "Tarefa para concluir", "descricao": ""},
    ).json()
    id_tarefa = criada["id"]

    # depois marca como concluída
    resposta = client.put(
        f"/tarefas/{id_tarefa}",
        json={"titulo": "Tarefa para concluir", "descricao": "", "concluida": True},
    )
    assert resposta.status_code == 200
    assert resposta.json()["concluida"] is True


def test_deletar_tarefa():
    criada = client.post(
        "/tarefas",
        json={"titulo": "Tarefa para apagar", "descricao": ""},
    ).json()
    id_tarefa = criada["id"]

    resposta = client.delete(f"/tarefas/{id_tarefa}")
    assert resposta.status_code == 200

    # confirma que sumiu
    busca = client.get(f"/tarefas/{id_tarefa}")
    assert busca.status_code == 404
