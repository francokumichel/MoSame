<template>
    <table v-if="talleres" class="table table-sm table-hover">
        <thead class="table-light">
            <tr>
                <th scope="col">Fecha y hora de carga</th>
                <th scope="col">Region sanitaria</th>
                <th scope="col">Dispositivo</th>
                <th v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" scope="col">Nombre de la escuela</th>
                <th v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" scope="col">Tipo de escuela</th>
                <th v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" scope="col">Años y cursos</th>
                <th v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" scope="col">Cantidad de encuentros</th>
                <th v-if="tipoTaller == 'Espacio Grupal en el Dispositivo' || tipoTaller == 'Acciones de Promoción y Prevención en la Comunidad'" scope="col">Nombre de actividad</th>
                <th scope="col">{{ tipoTaller == 'Talleres de Salud Mental en las Escuelas' ? 'Cantidad de jóvenes alcanzados' : 'cantidad de participantes' }}</th>
                <th scope="col">Observaciones</th>
                <th scope="col">Localidad</th>
                <th scope="col">Municipio</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="taller in talleres" :key="taller">
                <td>{{ taller.fecha_hora_carga }}</td>
                <td>{{ taller.municipio.region_sanitaria.tipo }}</td>
                <td>{{ taller.dispositivo_id }}</td>
                <td v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" >{{ taller.actividad.escuela.nombre }}</td>
                <td v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" >{{ taller.actividad.escuela.modalidad }}</td>
                <td v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" >{{ formatAnioDivisiones(taller.actividad.anios) }}</td>
                <td v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" >{{ taller.actividad.cant_encuentros }}</td>
                <td v-if="tipoTaller == 'Espacio Grupal en el Dispositivo'">{{ taller.actividad.actividades_internas_id }}</td>
                <td v-else-if="tipoTaller == 'Acciones de Promoción y Prevención en la Comunidad'">{{ taller.actividad.actividades_externas_id }}</td>
                <td>{{ taller.actividad.cant_participantes }}</td>
                <td>{{ taller.actividad.observaciones }}</td>
                <td>{{ taller.localidad_id }}</td>
                <td>{{ taller.municipio.nombre }}</td>
            </tr>
        </tbody>
    </table>
<p v-else>No hay talleres registrados en el sistema</p>    
</template>
  
<script>
export default {
    name: "TallerList",
    props: {
        talleres: {
            type: Array,
            default: () => [],
        },
        tipoTaller: {
            type: String,
            default: () => '',
        }
    },

    methods: {
        formatAnioDivisiones(anios) {
            return anios.map(anio => {
                return `${anio.anio} (${anio.divisiones})`;
            }).join(', ');
        },
            
    },
};
</script>