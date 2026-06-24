# Expense Tracker — Gestor de Gastos

Aplicación web desarrollada con Django para el registro, control y análisis de gastos personales. Permite agregar, editar, eliminar y filtrar gastos por categoría, con resúmenes visuales y totales automáticos.

## Características

- **Registro de gastos** con monto, descripción, categoría y fecha.
- **Categorías predefinidas**: Alimentación, Transporte, Vivienda, Salud, Educación, Entretenimiento, Ropa, Servicios y Otros.
- **Filtro por categoría** para visualizar gastos específicos.
- **Resumen automático** con total general y desglose por categoría.
- **Operaciones CRUD** completas: crear, editar y eliminar gastos con confirmación.
- **Interfaz responsive** adaptable a dispositivos móviles y de escritorio.
- **Panel de administración** Django para gestión avanzada.

## Requisitos

- Python 3.12+
- Django 6.0+

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/iroennys-admin/Expense-Tracker.git
cd Expense-Tracker

# Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python gestor_gastos/manage.py migrate

# Iniciar servidor de desarrollo
python gestor_gastos/manage.py runserver
```

Accede a la aplicación en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Uso

1. **Agregar un gasto**: Haz clic en "+ Nuevo gasto", completa el formulario y guarda.
2. **Filtrar gastos**: Selecciona una categoría en el filtro y haz clic en "Filtrar".
3. **Editar un gasto**: Haz clic en "Editar" junto al gasto que deseas modificar.
4. **Eliminar un gasto**: Haz clic en "Eliminar" y confirma la operación.

## Estructura del proyecto

```
Expense-Tracker/
├── gestor_gastos/
│   ├── gastos/                  # Aplicación principal
│   │   ├── templates/           # Plantillas HTML
│   │   │   ├── main.html        # Plantilla base
│   │   │   └── gastos/          # Plantillas de la app
│   │   ├── admin.py             # Configuración del panel admin
│   │   ├── forms.py             # Formularios
│   │   ├── models.py            # Modelo de datos
│   │   ├── urls.py              # Rutas de la aplicación
│   │   └── views.py             # Lógica de las vistas
│   ├── gestor_gastos/           # Configuración del proyecto
│   │   ├── settings.py          # Configuración general
│   │   └── urls.py              # Rutas principales
│   └── manage.py                # Script de gestión
├── requirements.txt             # Dependencias
└── README.md                    # Documentación
```

## Modelo de datos

| Campo       | Tipo          | Descripción                          |
|-------------|---------------|--------------------------------------|
| `monto`     | DecimalField  | Valor del gasto (hasta 10 dígitos, 2 decimales) |
| `descripcion` | CharField   | Descripción opcional del gasto       |
| `categoria` | CharField     | Categoría del gasto (con opciones predefinidas) |
| `fecha`     | DateField     | Fecha del gasto (por defecto: hoy)   |

## Licencia

Este proyecto es de uso libre y abierto.
