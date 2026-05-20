# Portal de Clase 1114 - Python y Flask

## Que es este proyecto

Es un **Portal Web educativo** donde estudiantes y profesor acceden a informacion de la clase.

**Los alumnos van a construirlo paso a paso en 8 tareas**, aprendiendo:
- Rutas y plantillas Flask
- Datos dinamicos con Jinja2
- Multiples paginas
- Bucles y listas
- Formularios
- Base de datos SQLite
- Autenticacion y sesiones
- CRUD (Create, Read, Update, Delete)

## El Portal incluye

- Pagina de inicio con info de la clase
- Formulario de inscripcion para estudiantes
- Base de datos de estudiantes inscritos
- Login para Profesor y Estudiantes
- Panel del Profesor: crear, editar, eliminar tareas
- Panel del Estudiante: ver tareas asignadas
- Sistema de permisos por rol

## Requisitos

- Python 3.8+
- Terminal
- Editor de codigo (VS Code, PyCharm, etc)

## Instalacion rapida

1. Copia la carpeta a tu computadora
2. Abre terminal en la carpeta

Crear entorno virtual (Windows):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

O en Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:
```powershell
pip install -r requirements.txt
```

4. Ejecuta el portal:
```powershell
python app.py
```

5. Abre http://127.0.0.1:5000 en tu navegador

## Las 8 Tareas

| # | Tarea | Que aprendes |
|---|-------|-------------|
| 1 | Portal base | Levantar Flask, HTML, rutas basicas |
| 2 | Datos dinamicos | Jinja2, variables de Python en HTML |
| 3 | Multiple paginas | Varias rutas, menu de navegacion |
| 4 | Listas y bucles | For en Jinja2, mostrar listas |
| 5 | Formularios | Recibir datos del usuario |
| 6 | Base de datos | SQLite, guardar datos persistentes |
| 7 | Autenticacion | Login, sesiones, roles (Profesor vs Estudiante) |
| 8 | CRUD completo | Crear, editar, eliminar tareas |

## Estructura del proyecto

```
clase-python-flask-1114/
├── app.py              # Aplicacion principal
├── requirements.txt    # Dependencias
├── portal.db          # Base de datos (se crea)
├── templates/         # Plantillas HTML
│   ├── index.html
│   ├── login.html
│   ├── panel_profesor.html
│   ├── panel_estudiante.html
│   └── ...mas templates
└── tasks/             # Consignas de trabajo
    ├── tarea-1.md
    ├── tarea-2.md
    └── ... tarea-8.md
```

## Como iniciar cada tarea

1. Lee la consigna en `tasks/tarea-X.md`
2. Sigue los pasos
3. Modifica `app.py` y `templates/`
4. Verifica en el navegador
5. Entrga evidencia (capturas, archivos modificados)

## Datos de prueba (Tarea 7+)

Profesor:
- Usuario: `henry`
- Contraseña: `password123`

## Conceptos que vas a dominar

- Backend web con Python y Flask
- Frontend HTML con Jinja2
- Bases de datos relacionales (SQLite)
- Autenticacion y sesiones
- Operaciones CRUD
- Arquitectura MVC
- Seguridad (hashing de contraseñas)

## Proximos pasos (Opcional)

- Agregar calificaciones
- Sistema de entregas de trabajos
- Notificaciones por email
- Interfaz mejorada con CSS
- Deploy en internet (Heroku, PythonAnywhere)
- API REST

## Creditos

Diseño y contenido: Henry Ortegon (Kyrbot Innovations)

Portal de Clase 1114 - Introduccion a Python y Flask
