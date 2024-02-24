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
                <!--
                <th scope="col">Fecha</th>
                <th scope="col">Género</th>
                <th scope="col">Edad</th>
                <th scope="col">¿Demanda tratamiento?</th>
                <th scope="col">Motivo de la consulta</th>
                <th scope="col">Detalle del motivo de la consulta</th>
                <th scope="col">Tipos de malestar emocional</th>
            -->
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
                <!--
                    <td>{{ `${new Date(llamada.fecha_y_hora_carga).getDate() + 1}/${new Date(llamada.fecha_y_hora_carga).getMonth() + 1}/${new Date(llamada.fecha_y_hora_carga).getFullYear()}` }}</td>
                    <td>{{ llamada.municipio.region_sanitaria.tipo }}</td>
                    <td>{{ llamada.identidad_genero_tipo }}</td>
                    <td>{{ llamada.edad }}</td>
                    <td>{{ llamada.demanda_tratamiento ? "Sí" : "No" }}</td>
                    <td>{{ llamada.motivo_nombre }}</td>
                    <td>{{ llamada.detalle_motivo_motivo }}</td>
                    <td>{{ llamada.malestares_emocionales }}</td>
                -->
            </tr>
        </tbody>
    </table>
    <p v-else>No hay personas derivadas registradas en el sistema</p>    
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