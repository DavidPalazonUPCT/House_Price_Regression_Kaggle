# House Price Regression Kaggle

## Descripción del Proyecto

Este proyecto está diseñado para aquellos con experiencia en R o Python y conceptos básicos de machine learning. Es perfecto para estudiantes de ciencia de datos que han completado un curso en línea de machine learning y buscan expandir su conjunto de habilidades antes de intentar una competencia destacada.

url del proyecto en kaggle 

https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

### Introducción

Cuando un comprador de vivienda describe su casa soñada, probablemente no mencione la altura del sótano o la proximidad a una vía férrea. Sin embargo, este dataset de competencia demuestra que mucho más influye en las negociaciones de precios que solo el número de dormitorios o una cerca blanca.

Con 79 variables explicativas que describen casi todos los aspectos de las viviendas residenciales en Ames, Iowa, este reto te invita a predecir el precio final de cada casa.

### Habilidades Prácticas

- Ingeniería creativa de características
- Técnicas avanzadas de regresión como random forest y gradient boosting

## Descripción del Dataset

### Descripción de Archivos

- `train.csv` - El conjunto de datos de entrenamiento
- `test.csv` - El conjunto de datos de prueba
- `data_description.txt` - Descripción completa de cada columna, preparada originalmente por Dean De Cock pero editada ligeramente para coincidir con los nombres de las columnas utilizados aquí.
- `sample_submission.csv` - Una presentación de referencia basada en una regresión lineal sobre el año y mes de venta, superficie del lote y número de dormitorios

### Campos de Datos

Aquí hay una versión breve de lo que encontrarás en el archivo de descripción de datos:

- `SalePrice` - El precio de venta de la propiedad en dólares. Esta es la variable objetivo que intentas predecir.
- `MSSubClass` - Clase del edificio
- `MSZoning` - Clasificación general de zonificación
- `LotFrontage` - Pies lineales de calle conectados a la propiedad
- `LotArea` - Tamaño del lote en pies cuadrados
- `Street` - Tipo de acceso a la carretera
- `Alley` - Tipo de acceso al callejón
- `LotShape` - Forma general de la propiedad
- `LandContour` - Planitud de la propiedad
- `Utilities` - Tipo de servicios disponibles
- `LotConfig` - Configuración del lote
- `LandSlope` - Pendiente de la propiedad
- `Neighborhood` - Ubicaciones físicas dentro de los límites de la ciudad de Ames
- `Condition1` - Proximidad a carretera principal o ferrocarril
- `Condition2` - Proximidad a carretera principal o ferrocarril (si hay un segundo presente)
- `BldgType` - Tipo de vivienda
- `HouseStyle` - Estilo de vivienda
- `OverallQual` - Calidad general del material y acabado
- `OverallCond` - Clasificación del estado general
- `YearBuilt` - Fecha de construcción original
- `YearRemodAdd` - Fecha de remodelación
- `RoofStyle` - Tipo de techo
- `RoofMatl` - Material del techo
- `Exterior1st` - Recubrimiento exterior de la casa
- `Exterior2nd` - Recubrimiento exterior de la casa (si hay más de un material)
- `MasVnrType` - Tipo de revestimiento de mampostería
- `MasVnrArea` - Área de revestimiento de mampostería en pies cuadrados
- `ExterQual` - Calidad del material exterior
- `ExterCond` - Condición actual del material en el exterior
- `Foundation` - Tipo de cimiento
- `BsmtQual` - Altura del sótano
- `BsmtCond` - Condición general del sótano
- `BsmtExposure` - Paredes de sótano con salida al jardín o nivel del suelo
- `BsmtFinType1` - Calidad del área terminada del sótano
- `BsmtFinSF1` - Tipo 1 de pies cuadrados terminados
- `BsmtFinType2` - Calidad de la segunda área terminada (si está presente)
- `BsmtFinSF2` - Tipo 2 de pies cuadrados terminados
- `BsmtUnfSF` - Pies cuadrados sin terminar del sótano
- `TotalBsmtSF` - Total de pies cuadrados del sótano
- `Heating` - Tipo de calefacción
- `HeatingQC` - Calidad y condición de la calefacción
- `CentralAir` - Aire acondicionado central
- `Electrical` - Sistema eléctrico
- `1stFlrSF` - Pies cuadrados del primer piso
- `2ndFlrSF` - Pies cuadrados del segundo piso
- `LowQualFinSF` - Pies cuadrados de baja calidad terminados (todos los pisos)
- `GrLivArea` - Área de vivienda sobre el nivel del suelo en pies cuadrados
- `BsmtFullBath` - Baños completos en el sótano
- `BsmtHalfBath` - Medios baños en el sótano
- `FullBath` - Baños completos sobre el nivel del suelo
- `HalfBath` - Medios baños sobre el nivel del suelo
- `Bedroom` - Número de dormitorios sobre el nivel del sótano
- `Kitchen` - Número de cocinas
- `KitchenQual` - Calidad de la cocina
- `TotRmsAbvGrd` - Total de habitaciones sobre el nivel del suelo (no incluye baños)
- `Functional` - Clasificación de funcionalidad del hogar
- `Fireplaces` - Número de chimeneas
- `FireplaceQu` - Calidad de la chimenea
- `GarageType` - Ubicación del garaje
- `GarageYrBlt` - Año en que se construyó el garaje
- `GarageFinish` - Acabado interior del garaje
- `GarageCars` - Tamaño del garaje en capacidad de coches
- `GarageArea` - Tamaño del garaje en pies cuadrados
- `GarageQual` - Calidad del garaje
- `GarageCond` - Condición del garaje
- `PavedDrive` - Entrada pavimentada
- `WoodDeckSF` - Área de la terraza de madera en pies cuadrados
- `OpenPorchSF` - Área de porche abierto en pies cuadrados
- `EnclosedPorch` - Área de porche cerrado en pies cuadrados
- `3SsnPorch` - Área de porche de tres estaciones en pies cuadrados
- `ScreenPorch` - Área de porche con mosquitero en pies cuadrados
- `PoolArea` - Área de la piscina en pies cuadrados
- `PoolQC` - Calidad de la piscina
- `Fence` - Calidad de la cerca
- `MiscFeature` - Característica miscelánea no cubierta en otras categorías
- `MiscVal` - Valor de característica miscelánea
- `MoSold` - Mes de venta
- `YrSold` - Año de venta
- `SaleType` - Tipo de venta
- `SaleCondition` - Condición de la venta

## Sugerencias de Contribución
Para contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (```git checkout -b feature/nueva-funcionalidad```).
3. Realiza tus cambios y haz commit (```git commit -am 'Añadir nueva funcionalidad'```).
4. Envía tus cambios a la rama (```git push origin feature/nueva-funcionalidad```).
5. Abre un Pull Request.
## Tecnologías Utilizadas
- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Optuna
- Logging
