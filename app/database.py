# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Parámetros de conexión a PostgreSQL
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:password@localhost/oncoscan_db")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base de datos
Base = declarative_base()