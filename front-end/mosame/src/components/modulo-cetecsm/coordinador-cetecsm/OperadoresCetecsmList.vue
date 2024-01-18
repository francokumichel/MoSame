<template>
    <table v-if="operadores" class="table table-hover">
        <thead class="table-light">
            <tr>
            <th scope="col">Nombre</th>
            <th scope="col">Apellido</th>
            <th scope="col">Email</th>
            <th scope="col">Cantidad de personas derivadas a CETECSM asignadas</th>
            <th scope="col">Fecha del último llamado</th>
            <th scope="col">Acciones</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="operador in operadores" :key="operador">
                <td>{{ operador.email }}</td>
                <td>{{ operador.name }}</td>
                <td>{{ operador.last_name }}</td>
                <td>{{ operador.cantidad_personas_asignadas }}</td>
                <td>{{ operador.fecha_ultimo_llamado }}</td>
                <td>
                    <div class="d-flex flex-row column-gap-2">
                        <router-link :to="'/cetecsm/asignadas/' + operador.id">
                            <button type="button" class="btn btn-outline-primary btn-sm">Actividad</button>
                        </router-link>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
    <p v-else>No hay operadores registrados en el sistema</p>    
</template>
  
<script>
export default {
    name: "OperadoresCetecsmList",
    props: {
        operadores: {
            type: Array,
            default: () => [],
        },
    },
};
</script>

<style>

</style>