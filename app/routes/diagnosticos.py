from fastapi import APIRouter

router = APIRouter()

@router.get("/diagnosticos/")
def listar_diagnosticos():
    return {"message": "Lista de diagnósticos"}

@router.post("/diagnosticos/")
def crear_diagnostico():
    return {"message": "Diagnóstico creado correctamente"}
