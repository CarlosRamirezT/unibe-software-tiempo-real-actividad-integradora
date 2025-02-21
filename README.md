# Monitoreo en Tiempo Real de la Actividad del Usuario

El proyecto consiste en un sistema que monitorea en tiempo real la actividad del usuario en la PC. La aplicación captura datos como la aplicación activa, el consumo de internet, las pulsaciones del teclado y los movimientos y clics del mouse, permitiendo almacenar y visualizar esta información de forma dinámica para el análisis y optimización de la productividad.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requerimientos](#requerimientos)
- [Instalación en macOS](#instalación-en-macos)
- [Ejecución de la Aplicación](#ejecución-de-la-aplicación)
- [Licencia](#licencia)

## Descripción del Proyecto

El sistema fue diseñado para capturar y analizar, en tiempo real, la actividad del usuario en una PC. Se monitorizó la aplicación en uso, el consumo de internet, las pulsaciones de teclado y los movimientos/clics del mouse. La solución procesa y almacena los datos para generar reportes y gráficos en tiempo real, permitiendo al usuario evaluar su comportamiento y mejorar su productividad. Además, el sistema notifica al usuario sobre posibles errores (por ejemplo, fallos en permisos) o situaciones de sobrecarga e inactividad, ofreciendo recomendaciones para optimizar el uso del equipo.

## Estructura del Proyecto

La estructura del proyecto se organiza de la siguiente forma:

```plaintext
.
├── LICENSE
├── README.md
├── backend
│   ├── data_capture.py
│   ├── data_processor.py
│   └── db_handler.py
├── main.py
├── requirements.txt
└── ui
    ├── app.py
    └── ui_helper.py
```


> **Nota:** La carpeta `monitoring_system_stageX` representa la etapa del proyecto (por ejemplo, `stage1` sin semáforos y `stage2` con semáforos).

## Requerimientos

### Python y Librerías

Se recomienda usar **Python 3.8 o superior**.

#### Librerías de la Biblioteca Estándar (incluidas en Python)
- `threading` – Para gestionar la concurrencia y crear hilos.
- `time` – Para gestionar temporizaciones y pausas.
- `random` – Para generar datos simulados (valores aleatorios).
- `datetime` – Para generar marcas de tiempo en los eventos.
- `tkinter` – Para la creación de la interfaz gráfica de escritorio.
- `sqlite3` (opcional) – Para el almacenamiento en una base de datos local.

#### Librerías de Terceros (instalables vía pip)

- `matplotlib==3.6.3` – Para la generación de gráficos en tiempo real.
- `numpy==1.23.5` – Para cálculos y manipulación de datos numéricos.
- `wheel==0.38.4` – Para facilitar el empaquetado y distribución del proyecto.

### El archivo **requirements.txt** contiene:

```plaintext
matplotlib==3.6.3
numpy==1.23.5
wheel==0.38.4
```

## Instalación en macOS

Sigue estos pasos para instalar y ejecutar el proyecto en macOS:

### Instalar Homebrew (si no lo tienes instalado):

Abre la Terminal y ejecuta:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Instalar pyenv:

```bash
brew update
brew install pyenv
pyenv init
pyenv virtualenv-init
```

### Instalar Python 3.8 (o superior) usando pyenv:

```bash
brew install python-tk@3.9
pyenv install 3.11.11
pyenv local 3.11.11
```

### Verificar la versión de Python:

```bash
python --version
```

### Clonar el repositorio o descargar el código fuente:


```bash
git clone <URL_del_repositorio>
cd monitoring_system_stageX
```

### Crear un entorno virtual (opcional, pero recomendado):

```bash
rm -rf ~/.pyenv/versions/unibe-software-tiempo-real-actividad-4
pyenv virtualenv 3.11.11 unibe-software-tiempo-real-actividad-4
pyenv activate unibe-software-tiempo-real-actividad-4
python --version
```

### Instalar las dependencias:

```bash
python -m pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
```

## Ejecución de la Aplicación

### El proyecto se divide en dos partes: el backend y la interfaz gráfica (UI).

Ejecutar el Backend:

Abre una Terminal y navega a la carpeta backend:

```bash
python main.py
```

### Ejecutar la Interfaz de Usuario:

Abre otra Terminal y navega a la carpeta ui:

```bash
cd ui
python app.py
```

La interfaz gráfica se iniciará mostrando la monitorización en tiempo real de la actividad del usuario.

