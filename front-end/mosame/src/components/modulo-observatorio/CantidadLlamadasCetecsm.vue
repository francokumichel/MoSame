<template>
    <label class="fw-semibold fs-5">Filtros:</label>
    <div class="row mb-5">
        <div class="col-5">
            <label for="fecha_derivacion" class="col-form-label fw-semibold">Fecha de llamado:</label>
            <div class="row">
                <div class="col-auto">
                    <label for="fecha_desde" class="col-form-label">Desde:</label>
                    <input v-model="fecha_desde" type="date" class="form-control shadow-sm" placeholder="Desde" aria-label="fecha_desde">
                </div>
                <div class="col-auto">
                    <label for="fecha_hasta" class="col-form-label">Hasta:</label>
                    <input v-model="fecha_hasta" type="date" class="form-control shadow-sm" placeholder="Hasta" aria-label="fecha_hasta">
                </div>
            </div>
        </div>
        <div class="col-2">
            <label for="usuario_id" class="col-form-label fw-semibold">Usuario:</label>
            <select class="form-select border border-dark-subtle" v-model="usuario_id" aria-label="Default select example">
                <option></option>
                <option v-for="usuario in usuarios_cetecsm" :key="usuario" :value="usuario.id">
                    {{ usuario.name }}
                </option>
            </select>
        </div>
        <div class="col-3">
            <label for="resolucion" class="col-form-label fw-semibold">Resolución de llamado:</label>
            <select class="form-select border border-dark-subtle" v-model="resolucion_llamado" aria-label="Default select example">
                <option></option>
                <option v-for="resolucion in resoluciones" :key="resolucion" :value="resolucion">
                    {{ resolucion }}
                </option>
            </select>
        </div>
        <div class="col-2 d-flex align-items-center justify-content-center">
            <button @click="obtenerTotalLlamadasUsuario" type="button" class="btn btn-outline-success rounded-circle">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                </svg>
            </button>
        </div>
    </div>
    <p class="fw-bold fs-3 text-center mb-5">Cantidad total de llamados: <span>{{ cant_total_llamadas }}</span></p>
</template>

<script>
import { apiService } from "@/services/api";

export default {
    data() {
        return {
            fecha_desde: null,
            fecha_hasta: null,
            usuarios_cetecsm: [],
            usuario_id: '',
            resoluciones: [],
            resolucion_llamado: '',
            cant_total_llamadas: 0,
        }
    },

    async created() {
        this.obtenerTotalLlamadasUsuario();
        await apiService.get(import.meta.env.VITE_API_URL + "resoluciones")
            .then((response) => {
                this.resoluciones = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            });

        await apiService.get(import.meta.env.VITE_API_URL + "cetecsm/operadores_cetecsm")
            .then((response) => {
                this.usuarios_cetecsm = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            });
    },

    methods: {
        async obtenerTotalLlamadasUsuario() {
            await apiService.get(import.meta.env.VITE_API_URL + "observatorio/cantidad_llamadas", {
                params: {
                    "fecha_desde": this.fecha_desde,
                    "fecha_hasta": this.fecha_hasta,
                    "usuario_id": this.usuario_id,
                    "resolucion_llamado": this.resolucion_llamado
                }
            })
                .then((response) => {
                    this.cant_total_llamadas = response.data.total_llamados;
                })
                .catch((e) => {
                    console.log(e)
                    this.errores.push(e);
                });
        },

        change: function() {
            this.obtenerTotalLlamadasUsuario();
        },
    }
}
</script>

<style>
.item-enter-active, .item-leave-active {
  transition: all 1s;
}
.item-enter, .item-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
</style>