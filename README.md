# SimplePyModule
> **SimplePyModule** es un módulo básico de Python que se encarga de aportar 4 submódulos básicos para facilitar operaciones sobre un dataset en el tratamiento de archivos, procesamiento de datos, filtrado y análisis gráfico.

## Índice
- [Instalación de Dependencias y Gestión](#instalación-de-dependencias-y-gestión)

- [Implementación](#implementación)
	- [Uso en archivos .PY](#uso-en-archivos-.py)
	- [Ejecución de Tests](#ejecución-de-tests)

- [Submódulos](#submódulos)
- [Funciones](#funciones)
  - [Módulo: fileManagement](#módulo-filemanagement)
  - [Módulo: dataProcessing](#módulo-dataProcessing)
  - [Módulo: dataFiltering](#módulo-dataFiltering)
  - [Módulo: graphicalAnalisis](#módulo-graphicalAnalisis)

- [Licenciamiento](#licenciamiento)

## Instalación de Dependencias y Gestión

Para instalar las dependencias necesarias para este proyecto, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Instalación del Paquete (Opcional)

Si queréis, podéis instalar **SimplePyModule** mediante el archivo *setup.py*. Este paso es recomendado si deseamos trabajar con el paquete en un entorno local.

```bash
python setup.py install
```

### Gestión Adicional

Una vez instalado localmente si la instalación es correcta deberíamos poder verlo listado como uno de los módulos locales.

```bash
pip list
```

#### Desinstalar el Módulo

Podremos desinstalarlo haciendo uso de la utilidad `PIP` de nuevo.

```bash
pip uninstall SimplePyModule
```

# Implementación

## Uso en archivos .py

Para poder utilizar el archivo bastará con importar el módulo una vez instalado.
(Revisar proceso de instalación referido en la documentación).

### Ex1
```python
import SimplePyModule as spm
```

### Ex2
```python
from SimplePyModule.dataFiltering import canceledSeries
```

## Ejecución de tests

**SimplePyModule** utiliza `unittest` para ejecutar sus tests. De esta manera podremos ejecutar tests unitarios o todos a la vez.

### SetUp de los tests

Para que los tests funcionen correctamente podemos setearlos desde el *root* del directorio de la siguiente manera:

```bash
python .\tests\test_decompressFile.py
```

### Ejecutar 1 Testcase

Para ejecutar un Testcase en concreto, seleccionaremos la función correspondiente y ejecutaremos ***.\tests\test_<función>.py***<br>
(*Siempre después de hacer el SetUp*)
```sh
python -m unittest .\tests\test_seriesByDecade.py
```

### Ejecutar todos los Tests

Para ejecutar todos los tests, desde la misma ruta ejecutamos el siguiente código.<br>
(*Siempre después de hacer el SetUp*)

```
python .\tests\run_all_tests.py
```

>También podremos utilizar el flag **--clean** para que elimine los ficheros *dummy* creados.

## Submódulos

| Módulo            | Descripción                                    |
| ----------------- | ---------------------------------------------- |
| **fileManagement**     | Funciones para descomprimir archivos y gestionar distintos formatos           |
| **dataProcessing**     | Funciones para procesar datos                  |
| **dataFiltering**          | Funciones para filtrar datos                   |
| **graphicalAnalisis**  | Funciones para realizar diferentes plots y gráficos                |

## Funciones

### Módulo: fileManagement

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| **decompressFile**| Función que descomprime ficheros en formato zip y tar.gz.               |
| **csvToDataFrame** | Función que lee csvs y los integra en un único dataframe                |
| **csvToDictionary** | Función que lee csvs y los integra en un único diccionario               |

### Módulo: dataProcessing

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| **addAirDays** | Función que añade air_days al dataFrame                |
| **seriesIntoDict** | Creación de un diccionario ordenado                |

### Módulo: dataFiltering

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| **canceledSeries** | Lista de las series que han empezado en 2023 y han sido canceladas                |
| **filterKeywords** | Búsqueda de series de género *mystery* o *crime*                |
| **jpDataframe** | Generación de dataframe cuyo idoma sea el japonés                |

### Módulo: graphicalAnalisis

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| **seriesByDecade** | Series por décadas desde 1940                |
| **seriesByGenre** | Series por género |
| **seriesByStartYear** | Series por año de inicio                |

# Licenciamiento
Este proyecto está licenciado bajo la Licencia MIT - revisa el archivo [LICENSE](LICENSE) para más detalles.
