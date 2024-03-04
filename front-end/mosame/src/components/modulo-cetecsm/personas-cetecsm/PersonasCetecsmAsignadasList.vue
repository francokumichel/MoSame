<template>
    <table v-if="personasAsignadas" class="table table-hover">
    <thead class="table-light">
        <tr>
        <th scope="col">Fecha de próximo llamado</th>
        <th v-if="esCoordinador" scope="col">Fecha de último llamado</th>
        <th v-if="esCoordinador" scope="col">Estado de llamada</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Edad</th>
        <th scope="col">DNI</th>
        <th scope="col">Teléfono</th>
        <th scope="col">Municipio</th>
        <th scope="col">Región sanitaria</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="persona in personasAsignadas" :key="persona">
        <td v-if="persona.fecha_prox_llamado_actual">{{ persona.fecha_prox_llamado_actual }}</td>
        <td v-else>-</td>
        <td v-if="esCoordinador">{{ persona.fecha_ultimo_llamado || '-' }}</td>
        <td v-if="esCoordinador">
          <span v-if="!persona.fecha_prox_llamado_actual && !persona.fecha_ultimo_llamado">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="#007bff" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
              <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"/>
            </svg> La persona todavía no ha sido llamada 
          </span>
          <span v-else-if="!persona.fecha_prox_llamado_actual && persona.fecha_ultimo_llamado">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="#007bff" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
              <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"/>
            </svg> Las llamadas a la persona han finalizado 
          </span>
          <span v-else-if="calcularDiferenciaFechas(persona.fecha_prox_llamado_actual, new Date()).esPosterior">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="#28a745" class="bi bi-stopwatch-fill" viewBox="0 0 16 16">
              <path d="M6.5 0a.5.5 0 0 0 0 1H7v1.07A7.001 7.001 0 0 0 8 16a7 7 0 0 0 5.29-11.584l.013-.012.354-.354.353.354a.5.5 0 1 0 .707-.707l-1.414-1.415a.5.5 0 1 0-.707.707l.354.354-.354.354-.012.012A6.97 6.97 0 0 0 9 2.071V1h.5a.5.5 0 0 0 0-1zm2 5.6V9a.5.5 0 0 1-.5.5H4.5a.5.5 0 0 1 0-1h3V5.6a.5.5 0 1 1 1 0"/>
            </svg> Debe llamar en {{ calcularDiferenciaFechas(persona.fecha_prox_llamado_actual, new Date()).diferenciaEnDias }} días
          </span>
          <span v-else>
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="#dc3545" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
              <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5m.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2"/>
            </svg> Debió llamar hace {{ calcularDiferenciaFechas(persona.fecha_prox_llamado_actual, new Date()).diferenciaEnDias }} días
          </span>
        </td>
        <td>{{ persona.nombre }}</td>
        <td>{{ persona.apellido }}</td>
        <td>{{ persona.edad }}</td>
        <td>{{ persona.dni }}</td>
        <td>{{ persona.telefono }}</td>
        <td>{{ persona.municipio.nombre }}</td>
        <td>{{ persona.municipio.region_sanitaria.tipo }}</td>
        <td>
            <div class="d-flex align-items-center column-gap-2">
              <router-link :to="'/cetecsm/persona/perfil/' + persona.id" class="btn btn-outline-primary btn-sm">Ver perfil</router-link>
              <router-link v-if="!esCoordinador" :to="'/cetecsm/llamada/crear/' + persona.id" class="btn btn-outline-success btn-sm">Cargar llamada</router-link>
            </div>
        </td>
        </tr>
    </tbody>
    </table>
    <p v-else>Todavía no posee ninguna persona asignada</p>    
</template>

<script>
export default {
  name: "PersonasCetecsmAsignadasList",
  props: {
    personasAsignadas: {
      type: Array,
      default: () => [],
    },
    esCoordinador: {
      type: Boolean,
      default: false,
    },
  },

  methods: {
    calcularDiferenciaFechas(fecha1, fecha2) {
      const date1 = new Date(fecha1);
      const date2 = new Date(fecha2);

      // Calcular la diferencia en milisegundos
      const diferenciaEnMilisegundos = date1 - date2;

      // Convertir la diferencia a días
      const diferenciaEnDias = Math.floor(diferenciaEnMilisegundos / (1000 * 60 * 60 * 24));

      // Verificar si la fecha1 es posterior a fecha2
      const esPosterior = date1 > date2;

      return {
        diferenciaEnDias: Math.abs(diferenciaEnDias), // Valor absoluto para evitar resultados negativos
        esPosterior,
      };
    },
  },
}
</script>  
