import sys
import os
import logging
from datetime import datetime
import traceback

def error_message_detail(error, tb):
    """Construye un mensaje de error detallado."""
    if tb is None:
        return f"Error: {str(error)}"
    file_name = tb.tb_frame.f_code.co_filename
    func_name = tb.tb_frame.f_code.co_name
    return f"Error en el script [{file_name}] en la función [{func_name}] línea [{tb.tb_lineno}] con mensaje: {str(error)}"

class CustomMLException(Exception):
    """Clase base para excepciones personalizadas relacionadas con Machine Learning."""

    def __init__(self, error, tb, developer_name, invalid_data=None):
        self.error = error
        self.tb = tb
        self.developer_name = developer_name
        self.invalid_data = invalid_data
        self.traceback_str = ''.join(traceback.format_tb(tb))
        self.log_exception()

    def log_exception(self):
        """Registra la excepción en un archivo de log."""
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%d-%m-%Y')}_{self.developer_name}_Exceptions.log")
        logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
        logging.error(self.__str__())
        logging.error(f"Traceback completo:\n{self.traceback_str}")
        logging.shutdown()

    def __str__(self):
        return f"{error_message_detail(self.error, self.tb)}\nTraceback completo:\n{self.traceback_str}"



class DataValidationError(CustomMLException):
    """Excepción para errores de validación de datos."""

    def __init__(self, error, tb, developer_name, invalid_data):
        super().__init__(error, tb, developer_name)
        self.invalid_data = invalid_data

    def __str__(self):
        base_message = super().__str__()
        return f"{base_message}\nDatos no válidos: {self.invalid_data}"

class ModelTrainingError(CustomMLException):
    """Excepción para errores durante el entrenamiento del modelo."""

    def __init__(self, error, tb, developer_name, model_params):
        super().__init__(error, tb, developer_name)
        self.model_params = model_params

    def __str__(self):
        base_message = super().__str__()
        return f"{base_message}\nParámetros del modelo: {self.model_params}"

class PredictionError(CustomMLException):
    """Excepción para errores durante la predicción."""

    def __init__(self, error, tb, developer_name, input_data):
        super().__init__(error, tb, developer_name)
        self.input_data = input_data

    def __str__(self):
        base_message = super().__str__()
        return f"{base_message}\nDatos de entrada: {self.input_data}"

class ModelSavingError(CustomMLException):
    def __init__(self, error, tb, developer_name, file_path):
        super().__init__(error, tb, developer_name)
        self.file_path = file_path

    def __str__(self):
        base_message = super().__str__()
        return f"{base_message}\nRuta del archivo: {self.file_path}"

class ModelLoadingError(CustomMLException):
    """Excepción para errores al cargar el modelo."""

    def __init__(self, error, tb, developer_name, file_path):
        super().__init__(error, tb, developer_name)
        self.file_path = file_path

    def __str__(self):
        base_message = super().__str__()
        return f"{base_message}\nRuta del archivo: {self.file_path}"

# Ejemplo de uso
if __name__ == "__main__":
    developer_name = "David"
    try:
        # Simulamos un error
        raise ValueError("Error en la validación de datos")
    except Exception as e:
        # Capturamos la excepción y obtenemos el traceback
        tb = sys.exc_info()[2]
        # Creamos nuestra excepción personalizada
        custom_exception = DataValidationError(str(e), tb, developer_name, {"precio": -1000})
        print(f"DataValidationError capturada: {custom_exception}")
