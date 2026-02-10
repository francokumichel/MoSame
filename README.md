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

Podes utilizar Github Codespaces para realizar pruebas. Se deben seguir los siguientes pasos:

1. Crear entorno codespaces

Dirigite a la sección `<> code` en Github, selecciona la pestaña `Codespaces` y luego la opción "create a codespace on main".

2. Levantar la infraestructura

Una vez que el entorno de Codespaces haya terminado de cargar, abri una terminal y ejecuta el siguiente comando para construir y levantar los contenedores:

```Bash
docker-compose up -d --build
```

3. Configurar el acceso (Puertos Públicos)

Para que el frontend pueda comunicarse con el backend desde tu navegador, es obligatorio que el puerto del Backend sea público:

- Dirigite a la pestaña Ports (Puertos) en la parte inferior de VS Code.
- Encontra el puerto 5000 (Backend - Flask).
- Hace clic derecho sobre él y selecciona Port Visibility > Public.
- Hace lo mismo con el puerto 8080 (Frontend - Vue) para poder visualizar la aplicación.

4. Acceder a la aplicación
El puerto 8080 te proporcionará una URL similar a: https://...-8080.app.github.dev. Hace clic en el icono del globo o en el enlace que aparece en la terminal para abrir la aplicación en el navegador.

## Credenciales de Acceso (Prueba)

El sistema incluye usuarios y datos asociados pre-cargados para probar los diferentes niveles de permisos y funcionalidades.

| Usuario / Rol | Email | Contraseña |
| :--- | :--- | :--- |
| **Administrador General** | `admin@gmail.com` | `1234` |
| **Administrador de Actividades** | `adminactividades@gmail.com` | `1234` |
| **Operador 0800** | `Operador0800@gmail.com` | `1234` |
| **Operador CETECSM** | `OperadorCETECSM@gmail.com` | `1234` |
| **Coordinador CETECSM** | `CoordinadorCETECSM@gmail.com` | `1234` |
| **Observatorio** | `Observatorio@gmail.com` | `1234` |
| **Trabajador de Salud** | `trabajadorsalud@gmail.com` | `1234` |