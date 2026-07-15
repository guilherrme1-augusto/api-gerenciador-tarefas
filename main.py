from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

# Cria as tabelas no banco (faz o CREATE TABLE automaticamente)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gerenciador de Tarefas")


@app.get("/")
def home():
    return {"mensagem": "API de Gerenciador de Tarefas"}


# CREATE - cria uma tarefa nova
@app.post("/tarefas", response_model=schemas.TarefaResposta, status_code=201)
def criar_tarefa(dados: schemas.TarefaCreate, db: Session = Depends(get_db)):
    nova = models.Tarefa(titulo=dados.titulo, descricao=dados.descricao)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


# READ - lista todas as tarefas
@app.get("/tarefas", response_model=list[schemas.TarefaResposta])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(models.Tarefa).all()


# READ - busca uma tarefa pelo id
@app.get("/tarefas/{id}", response_model=schemas.TarefaResposta)
def buscar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


# UPDATE - atualiza uma tarefa (ex: marcar como concluída)
@app.put("/tarefas/{id}", response_model=schemas.TarefaResposta)
def atualizar_tarefa(id: int, dados: schemas.TarefaUpdate, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa.titulo = dados.titulo
    tarefa.descricao = dados.descricao
    tarefa.concluida = dados.concluida
    db.commit()
    db.refresh(tarefa)
    return tarefa


# DELETE - apaga uma tarefa
@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
    return {"mensagem": f"Tarefa {id} apagada com sucesso"}
