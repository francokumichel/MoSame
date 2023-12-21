const enlacesPorRol = {
    'Operador 0800': [
      { path: '/llamadas_0800', text: 'Llamadas' },
    ],
    'Operador CETECSM': [
      { path: '/personas_derivadas', text: 'Personas derivadas' },
      { path: '/personas_asignadas', text: 'Personas asignadas' },
    ],
    'Coordinador CETECSM': [
        { path: '/personas_derivadas', text: 'Operadores' },
        { path: '/personas_asignadas', text: 'Personas derivadas' },
    ],
    'Trabajador de salud': [
        { path: '/cargar_actividad', text: 'Actividades' },
    ],
    'Administrador de actividades': [
        { path: '/talleres_cargados', text: 'Talleres' },
        { path: '/estadísticas', text: 'Estadísticas' },
    ],
    'Miembro observatorio': [
        { path: '/llamadas_0800', text: 'Llamadas 0800' },
        { path: '/personas_derivadas_cetecsm', text: 'Personas derivadas a CETEC SM' },
        { path: '/personas_en_seguimiento_cetecsm', text: 'Personas en seguimiento por CETEC SM' },
        { path: '/talleres', text: 'Talleres' },
    ],
    'admin': [
        { path: '/usuarios', text: 'Usuarios' },
    ],
};
  
export default enlacesPorRol;

