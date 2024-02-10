<template>
    <table v-if="personas" class="table table-sm table-hover">
        <thead class="table-light">
            <tr>
                <th scope="col">Región sanitaria</th>
                <th scope="col">Dispositivo que deriva</th>
                <th scope="col">¿Dio consentimiento?</th>
                <th scope="col">Edad</th>
                <th scope="col">Genero</th>
                <th scope="col">Motivo de la derivación</th>
                <th scope="col">Fecha de derivación</th>
                <th scope="col">Operador que deriva</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="persona in personas" :key="persona">
                <td>{{ persona.municipio.region_sanitaria.tipo }}</td>
                <td>{{ persona.derivacion.dispositivo_derivacion }}</td>
                <td>{{ persona.dio_consentimiento ? "Sí" : "No" }}</td>
                <td>{{ persona.edad }}</td>
                <td>{{ persona.identidad_genero ? persona.identidad_genero.tipo : '-'}}</td>
                <td>{{ persona.derivacion.mot_gral_derivacion.tipo }}</td>
                <td>{{ persona.derivacion.fecha }}</td>
                <td>{{ persona.derivacion.nombre_operador_derivador }}</td>
            </tr>
        </tbody>
    </table>
    <p v-else>No hay personas derivadas registradas en el sistema</p>    
</template>
  
<script>
export default {
    name: "PersonasCetecsmDerivadasList",
    props: {
        personas: {
            type: Array,
            default: () => [],
        },
    },
};
</script>