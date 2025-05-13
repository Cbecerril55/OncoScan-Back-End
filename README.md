# OncoScan-Back-End

### Descripción del Proyecto

OncoScan-Back-End es una API desarrollada con FastAPI para facilitar el análisis y diagnóstico de cáncer utilizando modelos de inteligencia artificial. El proyecto está diseñado para ser utilizado como herramienta de apoyo para médicos oncólogos en el Hospital Galenia en Cancún, Quintana Roo, permitiendo un análisis rápido y preciso de síntomas y resultados médicos.

### Características Principales

* Registro y gestión de pacientes, diagnósticos y médicos.
* Procesamiento de datos médicos utilizando algoritmos de aprendizaje automático.
* Integración con bases de datos para almacenamiento seguro de datos médicos.
* Pruebas y validación con Postman para simular interacciones del sistema.

### Tecnologías Utilizadas

* **Backend:** FastAPI, Python
* **Base de Datos:** PostgreSQL o SQLite
* **Machine Learning:** scikit-learn, TensorFlow, pandas, numpy
* **Pruebas:** Postman

### Estructura del Proyecto

```
oncoscan-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py           # Archivo principal de la API
│   ├── database.py       # Conexión a la base de datos
│   ├── models.py         # Definición de modelos de datos
│   ├── schemas.py        # Validación y estructura de datos
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── pacientes.py  # Rutas para manejo de pacientes
│   │   ├── diagnosticos.py # Rutas para manejo de diagnósticos
│   │   └── medicos.py    # Rutas para manejo de médicos
│   └── services/
│       ├── __init__.py
│       ├── paciente_service.py
│       ├── diagnostico_service.py
│       └── medico_service.py
│
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación del proyecto
└── .gitignore            # Archivos a ignorar en Git
```

### Instalación y Configuración

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Cbecerril55/OncoScan-Back-End.git
   cd OncoScan-Back-End
   ```
2. Crear y activar el entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```
4. Iniciar el servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

### Uso del Sistema

* **Pacientes:** Crear, listar, actualizar y eliminar pacientes.
* **Diagnósticos:** Crear, listar y actualizar diagnósticos.
* **Médicos:** Crear, listar y actualizar médicos.

### Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio y abre un pull request con tus mejoras.

### Licencia

Este proyecto está bajo la licencia MIT.
