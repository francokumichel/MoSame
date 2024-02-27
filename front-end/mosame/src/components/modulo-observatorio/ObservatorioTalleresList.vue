<template>
    <table v-if="talleres" class="table table-sm table-hover">
        <thead class="table-light">
            <tr>
                <th scope="col">Región sanitaria</th>
                <th scope="col">Municipio</th>
                <th scope="col">Localidad</th>
                <th scope="col">Dispositivo</th>
                <th scope="col">Gestión de la escuela</th>
                <th scope="col">Nivel de la escuela</th>
                <th scope="col">Modalidad de la escuela</th>
                <th scope="col">Cantidad de personas alcanzadas</th>
                <th scope="col">Cantidad de encuentros</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="taller in talleres" :key="talleres">
                <td>{{ taller.municipio.region_sanitaria.tipo }}</td>
                <td>{{ taller.municipio.nombre }}</td>
                <td>{{ taller.localidad }}</td>
                <td>{{ taller.dispositivo_id }}</td>
                <td>{{ taller.actividad.escuela ? taller.actividad.escuela.sector : '' }}</td>
                <td>{{ taller.actividad.escuela ? taller.actividad.escuela.niveles : '' }}</td>
                <td>{{ taller.actividad.escuela ? taller.actividad.escuela.modalidad : '' }}</td>
                <td>{{ taller.actividad.cant_participantes }}</td>
                <td>{{ taller.actividad.cant_encuentros }}</td>
            </tr>
        </tbody>
    </table>
    <p v-else>No hay talleres registrados en el sistema</p>    
</template>
  
<script>
export default {
    name: "ObservatorioTalleresList",
    props: {
        talleres: {
            type: Array,
            default: () => [],
        },
    },
};
</script>