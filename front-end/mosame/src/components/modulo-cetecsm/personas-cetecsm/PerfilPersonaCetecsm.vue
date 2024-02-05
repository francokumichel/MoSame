<template>
    <div class="p-4 border border-secondary-subtle shadow">
        <h2 class="fw-semibold border-2 border-bottom mb-4">Perfil</h2>
        <div v-if="persona">
            <div class="row g-3">
                <div class="col-md-auto">
                    <h5 class="fw-semibold border-2 border-bottom mb-3">Datos personales</h5>
                    <div class="mb-3 row">
                        <label for="nombre" class="col-sm-auto col-form-label fw-semibold">Nombre:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="nombre" :value="persona.nombre">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="apellido" class="col-sm-auto col-form-label fw-semibold">Apellido:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="apellido" :value="persona.apellido">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="dni" class="col-sm-auto col-form-label fw-semibold">DNI:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="dni" :value="persona.dni || '-'">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="telefono" class="col-sm-auto col-form-label fw-semibold">Teléfono:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="telefono" :value="persona.telefono">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="telefono_alternativo" class="col-sm-auto col-form-label fw-semibold">Teléfono alternativo:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="telefono_alternativo" :value="persona.telefono_alternativo">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="localidad" class="col-sm-auto col-form-label fw-semibold">Localidad:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="localidad" :value="persona.localidad || '-'">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="municipio" class="col-sm-auto col-form-label fw-semibold">Municipio:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="municipio" :value="persona.municipio.nombre || '-'">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="region_sanitaria" class="col-sm-auto col-form-label fw-semibold">Región sanitaria:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="region_sanitaria" :value="persona.municipio.region_sanitaria.tipo || '-'">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="detalle_acompañamiento" class="col-sm-auto col-form-label fw-semibold">Detalle acompañamiento:</label>
                        <div class="col-sm-auto">
                            <textarea type="text" readonly class="form-control-plaintext" id="detalle_acompañamiento" rows="3">{{ persona.detalle_acompanamiento }}</textarea>
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="dio_consentimiento" class="col-sm-auto col-form-label fw-semibold">¿Presta consentimiento?:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="dio_consentimiento" :value="persona.dio_consentimiento ? 'Si' : 'No'">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="grupo_conviviente" class="col-sm-auto col-form-label fw-semibold">Grupo conviviente:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="grupo_conviviente" :value="persona.grupo_conviviente">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="genero_identidad" class="col-sm-auto col-form-label fw-semibold">Identidad de género:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="genero_identidad" :value="persona.identidad_genero ? persona.identidad_genero.tipo : '-'">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="tiene_obra_social" class="col-sm-auto col-form-label fw-semibold">¿Tiene obra social?:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="tiene_obra_social" :value="persona.tiene_obra_social ? 'Sí' : 'No'">
                        </div>
                    </div>
                    <div v-if="persona.tiene_obra_social" class="mb-3 row">
                        <label for="obra_social" class="col-sm-auto col-form-label fw-semibold">Obra social:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="obra_social" :value="persona.obra_social">
                        </div>
                    </div>
                    <div v-if="persona.motivo_gral_acomp" class="mb-3 row">
                        <label for="motivo_gral_acomp" class="col-sm-auto col-form-label fw-semibold">Motivo general de acompañamiento:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="motivo_gral_acomp" :value="persona.motivo_gral_acomp.tipo || ''">
                        </div>
                    </div>
                    <div v-if="persona.motivo_gral_acomp && persona.motivo_gral_acomp.tipo == 'Malestar emocional'">
                        <div class="mb-3 row">
                            <label for="malestares_emocionales" class="col-sm-auto col-form-label fw-semibold">Malestares emocionales:</label>
                            <div class="col-sm-auto">
                                <input type="text" readonly class="form-control-plaintext" id="malestares_emocionales" :value="formatList(persona.motivo_gral_acomp.malestares_emocionales)">
                            </div>
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="situacion_vulnerabilidad" class="col-sm-auto col-form-label fw-semibold">Situaciones de vulnerabilidad:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="situacion_vulnerabilidad" :value="formatList(persona.situaciones_vulnerabilidad)">
                        </div>
                    </div>
                </div>
                <div class="col-md-auto">
                    <h5 class="fw-semibold border-2 border-bottom mb-3">Datos derivación</h5>
                    <div class="mb-3 row">
                        <label for="fecha_derivacion" class="col-sm-auto col-form-label fw-semibold">Fecha de derivación:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="fecha_derivacion" :value="persona.derivacion.fecha">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="descripcion" class="col-sm-auto col-form-label fw-semibold">Descripción:</label>
                        <div class="col-sm-auto">
                            <textarea type="text" readonly class="form-control-plaintext" id="descripcion" rows="2">{{ persona.derivacion.descripcion }}</textarea>
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="dispositivo_derivacion" class="col-sm-auto col-form-label fw-semibold">Dispositivo que deriva:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="dispositivo_derivacion" :value="persona.derivacion.dispositivo_derivacion">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="nombre_operador_derivador" class="col-sm-auto col-form-label fw-semibold">Nombre del operador que deriva:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="nombre_operador_derivador" :value="persona.derivacion.nombre_operador_derivador">
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <label for="mot_gral_derivacion" class="col-sm-auto col-form-label fw-semibold">Motivo general de derivación:</label>
                        <div class="col-sm-auto">
                            <input type="text" readonly class="form-control-plaintext" id="mot_gral_derivacion" :value="persona.derivacion.mot_gral_derivacion.tipo">
                        </div>
                    </div>
                </div>
            </div>
            <div class="d-flex justify-content-center align-items-center column-gap-2">
                <router-link :to="'/cetecsm/persona/llamadas/' + persona.id" class="btn btn-primary shadow-sm">Ver historial de llamadas</router-link>
                <div v-if="esOperador()">
                    <router-link :to="'/cetecsm/persona/editar/' + persona.id" class="btn btn-primary shadow-sm">Editar persona</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
    data() {
        return{
            persona: null,
            roles: [],
            errores: [],
        }
    },

    async created() {
        await apiService.get(import.meta.env.VITE_API_URL + "cetecsm/persona/perfil/" + this.$route.params.id)
            .then((response) => {
                this.persona = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            });

        await apiService.get(import.meta.env.VITE_API_URL + "me/roles")
            .then((response) => {
                this.roles = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })    
    },

    methods: {
        formatList(lista) {
            return lista ? lista.map(l => l.tipo).join(', ') : '';
        },

        esOperador() {
            return this.roles.some((role) => role.name == "Operador CETECSM");
        }
    },
}
</script>

<style>
.label {
    font-weight: bold;
}
</style>