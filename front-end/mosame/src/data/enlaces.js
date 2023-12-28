const enlacesPorRol = {
    'Operador 0800': [
      { path: '/calls_0800', text: 'Llamadas' },
    ],
    'Operador CETECSM': [
      { path: '/derived_people', text: 'Personas derivadas' },
      { path: '/assigned_people', text: 'Personas asignadas' },
    ],
    'Coordinador CETECSM': [
        { path: '/derived_people', text: 'Operadores' },
        { path: '/assigned_people', text: 'Personas derivadas' },
    ],
    'Trabajador de salud': [
        { path: '/activity/create', text: 'Actividades' },
    ],
    'Administrador de actividades': [
        { path: '/workshops', text: 'Talleres' },
        { path: '/statistics', text: 'Estadísticas' },
    ],
    'Miembro observatorio': [
        { path: '/calls_0800', text: 'Llamadas 0800' },
        { path: '/derived_people_cetecsm', text: 'Personas derivadas a CETEC SM' },
        { path: '/follow_people_cetecsm', text: 'Personas en seguimiento por CETEC SM' },
        { path: '/workshops', text: 'Talleres' },
    ],
    'Administrador': [
        { path: '/users', text: 'Usuarios' },
    ],
};
  
export default enlacesPorRol;

