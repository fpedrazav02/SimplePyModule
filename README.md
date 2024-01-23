# SimplePyModule
> **SimplePyModule** es un módulo básico de Python que se encarga de aportar 4 submódulos básicos para facilitar operaciones sobre un dataset en el tratamiento de archivos, procesamiento de datos, filtrado y análisis gráfico.

## Índice
- [Instalación de Dependencias y Gestión](#instalación-de-dependencias-y-gestión)

- [Implementación](#implementación)
	- [Uso en archivos .PY](#uso-en-archivos-.py)
	- [Ejecución de Tests](#ejecución-de-tests)

- [Submódulos](#submódulos)
- [Funciones](#funciones)
  - [Módulo: Descompresión](#módulo-descompresión)
  - [Módulo: Procesamiento](#módulo-procesamiento)
  - [Módulo: Filtrado](#módulo-filtrado)
  - [Módulo: Análisis Gráfico](#módulo-análisis-gráfico)

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

### Módulo: Descompresión

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| Nombre de la Función 1 | Breve descripción de la Función 1                |
| Nombre de la Función 2 | Breve descripción de la Función 2                |

### Módulo: Procesamiento

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| Nombre de la Función 1 | Breve descripción de la Función 1                |
| Nombre de la Función 2 | Breve descripción de la Función 2                |

### Módulo: Filtrado

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| Nombre de la Función 1 | Breve descripción de la Función 1                |
| Nombre de la Función 2 | Breve descripción de la Función 2                |

### Módulo: Análisis Gráfico

| Función                | Descripción                                      |
| ---------------------- | ------------------------------------------------ |
| Nombre de la Función 1 | Breve descripción de la Función 1                |
| Nombre de la Función 2 | Breve descripción de la Función 2                |

