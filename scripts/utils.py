from pathlib import Path
from datetime import datetime
from typing import Any
import sys
import joblib
from scripts.exceptions import ModelSavingError, ModelLoadingError
import traceback

def get_model_class_name(model: Any) -> str:
    """Obtiene el nombre de la clase del modelo."""
    return model.__class__.__name__

def save_model(model, developer_name, version, optuna_study_name, problem_type):
    model_type = type(model).__name__
    directory = Path('models') / model_type
    directory.mkdir(parents=True, exist_ok=True)
    file_name = f"{developer_name}_{model_type}_{version}_{optuna_study_name}_{problem_type}.pkl"
    file_path = directory / file_name
    try:
        joblib.dump(model, file_path)
        print(f"Modelo guardado en {file_path}")
        return [str(file_path)]  # Devolver una lista con el nombre del archivo
    except Exception as e:
        tb = traceback.format_exc()
        raise ModelSavingError(str(e), tb, developer_name, str(file_path))

def load_model(file_path: Path, developer_name: str) -> Any:
    """Carga un modelo desde el archivo especificado."""
    try:
        if not file_path.exists():
            raise FileNotFoundError(f"El archivo {file_path} no existe.")
        model = joblib.load(file_path)
        print(f"Modelo cargado desde {file_path}")
        return model
    except Exception as e:
        tb = sys.exc_info()[2]
        raise ModelLoadingError(e, tb, developer_name, str(file_path))