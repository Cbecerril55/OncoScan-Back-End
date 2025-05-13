from fastapi import APIRouter

router = APIRouter()

@router.get("/medicos/")
def listar_medicos():
    return {"message": "Lista de médicos"}

@router.post("/medicos/")
def crear_medico():
    return {"message": "Médico creado correctamente"}
