import logging
import os
from datetime import datetime

class CustomLogger:
    """
    Clase para configurar y gestionar múltiples loggers personalizados para diferentes propósitos.

    Atributos:
    ----------
    logs_dir : str
        Directorio donde se almacenan los archivos de log.
    
    developer : str
        Nombre del desarrollador que utiliza los logs.
    
    Métodos:
    --------
    __init__(developer):
        Inicializa el objeto CustomLogger y configura los loggers según el desarrollador.
    
    get_logger(name):
        Devuelve el logger solicitado por nombre.

    log_results(estudio, version, modelo, rmse, mse, mae, r2, hiperparams, tiempo_ejecucion):
        Registra los resultados de una prueba de modelo.
    
    log_visualization(name, path):
        Registra una visualización generada.
    
    log_optimization(estudio, version, modelo_final, hiperparams, tiempo_ejecucion, resultados):
        Registra detalles de la optimización del modelo.

    Ejemplo de uso:
    ---------------
    logger = CustomLogger(developer='David')
    app_logger = logger.get_logger('app')
    results_logger = logger.get_logger('results')
    visualizations_logger = logger.get_logger('visualizations')
    optimization_logger = logger.get_logger('optimization')

    app_logger.info('Iniciando la aplicación.')
    """	
    _instance = None
    _loggers = {}

    def __new__(cls, developer):
        if cls._instance is None:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, developer):
        """
        Inicializa los loggers y configura los handlers y formateadores.
        
        Parámetros:
        -----------
        developer : str
            Nombre del desarrollador que utiliza los logs.
        """
        if self._initialized:
            return
        self._initialized = True

        self.logs_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
        os.makedirs(self.logs_dir, exist_ok=True)
        self.developer = developer

        # Configurar todos los loggers necesarios
        self._setup_logger('app_logger', f'{developer}_app.log')
        self._setup_logger('results_logger', f'{developer}_results.log', level=logging.INFO)
        self._setup_logger('visualizations_logger', f'{developer}_visualizations.log', level=logging.INFO)
        self._setup_logger('optimization_logger', f'{developer}_optimization.log', level=logging.INFO)
        self._setup_logger('errors_logger', f'{developer}_errors.log', level=logging.WARNING)
        self._setup_logger('debug_logger', f'{developer}_debug.log', level=logging.DEBUG)

    def _setup_logger(self, logger_name, log_file, level=logging.DEBUG):
        """
        Configura un logger con el nombre y archivo de log especificados.
        
        Parámetros:
        -----------
        logger_name : str
            Nombre del logger.
        
        log_file : str
            Nombre del archivo de log.
        
        level : int
            Nivel de logging.
        
        Devuelve:
        ---------
        logger : logging.Logger
            Logger configurado.
        """
        if logger_name in self._loggers:
            return self._loggers[logger_name]

        log_file_path = os.path.join(self.logs_dir, log_file)
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        if not logger.handlers:  # Solo configura si no hay handlers
            file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
            file_handler.setLevel(level)
            file_format = logging.Formatter('[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_format)
            logger.addHandler(file_handler)
            
            if logger_name == 'app_logger':
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.WARNING)
                console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
                console_handler.setFormatter(console_format)
                logger.addHandler(console_handler)

            logger.propagate = False
        
        self._loggers[logger_name] = logger
        return logger

    def get_logger(self, name):
        """
        Devuelve el logger solicitado por nombre.
        
        Parámetros:
        -----------
        name : str
            Nombre del logger.
        
        Devuelve:
        ---------
        logger : logging.Logger
            Logger solicitado.
        """
        logger_name = f"{name}_logger"
        return self._loggers.get(logger_name, None)

    def log_results(self, estudio, version, modelo, rmse, mse, mae, r2, hiperparams, tiempo_ejecucion):
        """
        Registra los resultados de una prueba de modelo.
        
        Parámetros:
        -----------
        estudio : str
            Nombre del estudio.
        
        version : str
            Versión del estudio.
        
        modelo : str
            Nombre del modelo utilizado.
        
        rmse : float
            Error cuadrático medio de la raíz.
        
        mse : float
            Error cuadrático medio.
        
        mae : float
            Error absoluto medio.
        
        r2 : float
            Coeficiente de determinación.
        
        hiperparams : str
            Hiperparámetros utilizados y versión de Optuna. 
        
        tiempo_ejecucion (segundos) : float
            Tiempo de ejecución del modelo.
        """
        if 'results_logger' not in self._loggers:
            raise AttributeError("Este método solo puede ser llamado por el results_logger")
        
        self._loggers['results_logger'].info(f"Estudio: {estudio} v{version} | Modelo: {modelo} | RMSE: {rmse} | MSE: {mse} | MAE: {mae} | R2: {r2} | Hiperparams: {hiperparams} | Tiempo de ejecución: {tiempo_ejecucion}")

    def log_visualization(self, name, path):
        """
        Registra una visualización generada.
        
        Parámetros:
        -----------
        name : str
            Nombre de la visualización.
        
        path : str
            Ruta de almacenamiento de la visualización.
        """
        self._loggers['visualizations_logger'].info(f"Visualización: {name} | Ubicación: {path}")

    def log_optimization(self, estudio, version, modelo_final, hiperparams, tiempo_ejecucion, resultados):
        """
        Registra detalles de la optimización del modelo.
        
        Parámetros:
        -----------
        estudio : str
            Nombre del estudio.
        
        version : str
            Versión del estudio.
        
        modelo_final : str
            Modelo final utilizado.
        
        hiperparams : dict
            Hiperparámetros del modelo final.
        
        tiempo_ejecucion : float
            Tiempo de ejecución del modelo.
        
        resultados : dict
            Resultados del modelo.
        """
        self._loggers['optimization_logger'].info(f"Estudio: {estudio} | Versión: {version} | Modelo Final: {modelo_final} | Hiperparams: {hiperparams} | Tiempo de ejecución: {tiempo_ejecucion} | Resultados: {resultados}")
