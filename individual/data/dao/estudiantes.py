from ..schemas import EsquemaEstudiante

from ..models import Estudiante
from ..database import SessionLocal

db = SessionLocal()


def registrar_estudiante(estudiante: EsquemaEstudiante):
    db_estudiante = Estudiante(
        simulacion_id=estudiante.simulacion_id,
        horas_cumplidas=estudiante.horas_cumplidas,
        duracion_pasantia=estudiante.duracion_pasantia,
        tramites_realizados=estudiante.tramites_realizados,
        tiempo_promedio_por_tramite=estudiante.tiempo_promedio_por_tramite,
    )
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)

    return db_estudiante


def actualizar_estudiante(estudiante_id: int, estudiante: EsquemaEstudiante):
    db_estudiante = db.query(Estudiante).filter(
        Estudiante.id == estudiante_id).first()
    if db_estudiante:
        db_estudiante.horas_cumplidas = estudiante.horas_cumplidas
        db_estudiante.duracion_pasantia = estudiante.duracion_pasantia
        db_estudiante.tramites_realizados = estudiante.tramites_realizados
        db_estudiante.tiempo_promedio_por_tramite = estudiante.tiempo_promedio_por_tramite
        db.commit()
        db.refresh(db_estudiante)

        return db_estudiante

    return None