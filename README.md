# 📝 Survey System (Django)

Un sistema de encuestas construido con **Django**, basado en el clásico ejemplo de *polls*, pero organizado de forma profesional para servir como base de proyectos reales o educativos.

---

## aracterísticas principales

- Creación y gestión de preguntas.
- Registro de opciones de respuesta.
- Sistema de votación funcional.
- Visualización de resultados.
- Panel administrativo para gestionar encuestas.

---

## Tecnologías utilizadas

- **Python 3**
- **Django 5**
- HTML / CSS
- SQLite por defecto

---

## Estructura del proyecto

```
project/
│
├── polls/
│   ├── migrations/
│   ├── static/
│      ├──poll/ 
│   ├── templates/
│   │   └── polls/images
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

## Uso

- `http://127.0.0.1:8000/` — Página principal de encuestas  
- `http://127.0.0.1:8000/admin/` — Administrar preguntas y opciones  

---

## Tests

```bash
python manage.py test
```
