# app/routes/pacientes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/pacientes/")
def listar_pacientes():
    return {"message": "Lista de pacientes"}

@router.post("/pacientes/")
def crear_paciente():
    return {"message": "Paciente creado correctamente"}
