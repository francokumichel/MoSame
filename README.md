# MoSame: Modernización del Observatorio de Salud Mental de la PBA
Sistema integral para la gestión, seguimiento y anonimización de datos de salud mental, diseñado para la Subsecretaría de Salud Mental, Consumos Problemáticos y Violencia en el Ámbito de la Salud Pública (PBA).

## Resumen del proyecto
MoSame centraliza la información proveniente de tres frentes críticos: el Dispositivo 0800 (atención primaria), el CETEC SM (seguimiento y derivación) y las Actividades de Prevención comunitarias. El sistema permite la carga de datos sensibles asegurando la privacidad mediante procesos de anonimización automática para el análisis estadístico del Observatorio.

## Stack tecnológico

### Backend
- **Framework**: Flask (Python)
- **ORM**: Flask-SQLAlchemy
- **Autenticación**: JWT-Flask-Extended (Seguridad basada en roles)
- **Base de Datos**: SQL Server

### Frontend

- **Framework**: Vue.js
- **Arquitectura**: Single Page Application (SPA)

## Metodología y flujo de trabajo

El proyecto se desarrolló siguiendo un ciclo de vida de software centrado en la precisión de los requerimientos y la validación constante con el cliente:

1. **Elicitación de requerimientos**: Entrevistas presenciales/virtuales con los diferentes actores.

2. **Diseño y documentación**: Elaboración de artefactos clave:

    - Casos de uso
    - Diseño de base de datos (modelo Entidad-Relacion)
    - Prototipado (Mockups)
    - Especificación de Requisitos de Software (SRS)

3. **Desarrollo**: Construcción de módulos (Front-end y Back-end) con entregas parciales y feedback constante del cliente, asegurando la alineación con las necesidades operativas de la Subsecretaría.

## Arquitectura del sistema

El sistema se organiza en dos grandes componentes comunicados vía API REST:

```
MoSame/
├── back-end/      # API REST en Flask y lógica de negocio
├── front-end/     # Interfaz de usuario reactiva en Vue.js
├── .gitignore
└── README.md
```

### Roles implementados (RBAC)

- **Operador 0800**: Gestión de llamadas iniciales.
- **Coordinador/Operador CETEC**: Seguimiento cronológico y derivaciones.
- **Administrador de Actividades**: Carga de talleres y georreferenciación.
- **Miembro del Observatorio**: Acceso a datos anonimizados para reportes.
- **Superusuario**: Gestión de catálogos y permisos.

## Instalación y uso

### Requisitos previos

- Python 3.x
- Node.js & npm
- Instancia de SQL Server

### Backend

1. Navegar a `back-end`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Configurar variables de entorno (DB Connection).
4. Ejecutar: `flask run`

### Frontend

1. Navegar a `front-end/`
2. Instalar dependencias: `npm install`
3. Ejecutar: `npm run serve`

