from fastapi import FastAPI
from app.routes import pacientes, diagnosticos, medicos

app = FastAPI()

# Incluir rutas
app.include_router(pacientes.router)
app.include_router(diagnosticos.router)
app.include_router(medicos.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Oncoscan - API para diagnóstico de cáncer"}

@app.get("/status")
def status_check():
    return {"status": "El servidor está funcionando correctamente"}
