const enlacesPorRol = {
    'Operador 0800': [
      { path: '/modulo_0800/llamadas', text: 'Llamadas' },
      { path: '/modulo_0800/cargar_llamada', text: 'Cargar llamada'},
    ],
    'Operador CETECSM': [
      { path: '/cetecsm/derivaciones', text: 'Personas derivadas' },
      { path: '/cetecsm/asignaciones', text: 'Personas asignadas' },
    ],
    'Coordinador CETECSM': [
        { path: '/cetecsm/operadores', text: 'Operadores' },
        { path: '/cetecsm/derivaciones', text: 'Personas derivadas' },
        { path: "/cetecsm/personas/asignadas_todas", text: 'Personas en seguimiento' },
    ],
    'Trabajador de salud': [
        { path: '/actividades/create', text: 'Actividades' },
    ],
    'Administrador de actividades': [
        { path: '/actividades/talleres', text: 'Talleres' },
        { path: '/actividades/estadisticas', text: 'Estadísticas' },
    ],
    'Miembro observatorio': [
        { path: '/observatorio/llamadas_0800', text: 'Llamadas 0800' },
        { path: '/observatorio/personas_cetecsm_derivadas', text: 'Personas derivadas CETEC SM' },
        { path: '/observatorio/personas_cetecsm_seguimiento', text: 'Personas en seguimiento CETEC SM' },
        { path: '/observatorio/cantidad_llamadas_cetecsm', text: 'Cantidad total de llamadas CETEC SM' },
        { path: '/observatorio/talleres', text: 'Talleres' },
    ],
    'Administrador': [
        { path: '/users', text: 'Usuarios' },
        { path: '/editar_opciones', text: 'Editar opciones' }
    ],
};
  
export default enlacesPorRol;

