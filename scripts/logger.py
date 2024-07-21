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
    ```python	
    __init__(developer):
    ```
    Inicializa el objeto CustomLogger y configura los loggers según el desarrollador.
    
    ```python	
    get_logger(name):
    ```
        Devuelve el logger solicitado por nombre.

    ```python	
    log_results(estudio, version, modelo, rmse, mse, mae, r2, hiperparams, tiempo_ejecucion):
    ```
        Registra los resultados de una prueba de modelo.
    
    ```python	
    log_visualization(name, path):
    ```
        Registra una visualización generada.
    
    ```python	
    log_optimization(estudio, version, modelo_final, hiperparams, tiempo_ejecucion, resultados):
    ```
        Registra detalles de la optimización del modelo.

    Ejemplo de uso:
    ---------------
    ```python	
    logger = CustomLogger(developer='David')
    app_logger = logger.get_logger('app')
    results_logger = logger.get_logger('results')
    visualizations_logger = logger.get_logger('visualizations')
    optimization_logger = logger.get_logger('optimization')

    app_logger.info('Iniciando la aplicación.')
    ```	
    ## Ejemplo de log de resultados
    ```python
    logger.log_results(
        estudio='House Pricing',
        version='1.0',
        modelo='RandomForest',
        rmse=0.123,
        mse=0.015,
        mae=0.010,
        r2=0.85,
        hiperparams='Optuna v2.0',
        tiempo_ejecucion=123.45
    )
    ```

    ## Ejemplo de log de visualización
    ```python
    logger.log_visualization(
        name='Precio vs Área',
        path='/plots/price_vs_area.png'
    )
    ```

    ## Ejemplo de log de optimización
    ```python
    logger.log_optimization(
        estudio='House Pricing Optimization',
        version='1.0',
        modelo_final='RandomForest',
        hiperparams={'n_estimators': 100, 'max_depth': 10},
        tiempo_ejecucion=123.45,
        resultados={'value_0': 1, 'value_1': 2}
    )
    ```
    """
    
    def __init__(self, developer):
        """
        Inicializa los loggers y configura los handlers y formateadores.
        
        Parámetros:
        -----------
        developer : str
            Nombre del desarrollador que utiliza los logs.
        """
        self.logs_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(self.logs_dir, exist_ok=True)
        self.developer = developer
        
        self.app_logger = self._setup_logger('app_logger', f'{developer}_app.log')
        self.results_logger = self._setup_logger('results_logger', f'{developer}_results.log', level=logging.INFO)
        self.visualizations_logger = self._setup_logger('visualizations_logger', f'{developer}_visualizations.log', level=logging.INFO)
        self.optimization_logger = self._setup_logger('optimization_logger', f'{developer}_optimization.log', level=logging.INFO)
        self.errors_logger = self._setup_logger('errors_logger', f'{developer}_errors.log', level=logging.WARNING)
        self.debug_logger = self._setup_logger('debug_logger', f'{developer}_debug.log', level=logging.DEBUG)

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
        log_file_path = os.path.join(self.logs_dir, log_file)
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

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
        return getattr(self, f"{name}_logger", None)

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
        self.results_logger.info(f"Estudio: {estudio} v{version} | Modelo: {modelo} | RMSE: {rmse} | MSE: {mse} | MAE: {mae} | R2: {r2} | Hiperparams: {hiperparams} | Tiempo de ejecución: {tiempo_ejecucion}")

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
        self.visualizations_logger.info(f"Visualización: {name} | Ubicación: {path}")

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
        self.optimization_logger.info(f"Estudio: {estudio} | Versión: {version} | Modelo Final: {modelo_final} | Hiperparams: {hiperparams} | Tiempo de ejecución: {tiempo_ejecucion} | Resultados: {resultados}")

# Ejemplo de uso:
logger = CustomLogger(developer='David')
app_logger = logger.get_logger('app')
results_logger = logger.get_logger('results')
visualizations_logger = logger.get_logger('visualizations')
optimization_logger = logger.get_logger('optimization')

app_logger.info('Iniciando la aplicación.')

# # Ejemplo de log de resultados
# logger.log_results(
#     estudio='House Pricing',
#     version='1.0',
#     modelo='RandomForest',
#     rmse=0.123,
#     mse=0.015,
#     mae=0.010,
#     r2=0.85,
#     hiperparams='Optuna v2.0',
#     tiempo_ejecucion=123.45
# )

# # Ejemplo de log de visualización
# logger.log_visualization(
#     name='Precio vs Área',
#     path='/plots/price_vs_area.png'
# )

# # Ejemplo de log de optimización
# logger.log_optimization(
#     estudio='House Pricing Optimization',
#     version='1.0',
#     modelo_final='RandomForest',
#     hiperparams={'n_estimators': 100, 'max_depth': 10},
#     tiempo_ejecucion=123.45,
#     resultados={'value_0': 1, 'value_1': 2}
# )
