from pydantic import BaseModel


# Dados que CHEGAM ao criar uma tarefa (o cliente só informa título e descrição)
class TarefaCreate(BaseModel):
    titulo: str
    descricao: str = ""


# Dados que CHEGAM ao atualizar uma tarefa (inclui o "concluida")
class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str
    concluida: bool


# Formato da RESPOSTA que a API devolve
class TarefaResposta(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool

    class Config:
        from_attributes = True  # permite criar o schema a partir do objeto do banco
