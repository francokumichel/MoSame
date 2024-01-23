<template>
        <h2 class="fw-bold mb-4">Registrar llamada</h2>
        <form ref="formulario" class="px-5 needs-validation" @submit.prevent="registrarLlamada" novalidate>
                <div class="mb-3">
                    <label for="motivo_de_consulta" class="col-form-label fw-semibold">Motivo de la consulta:</label>
                    <select class="form-select border border-dark-subtle" v-model.lazy="llamada.motivo_consulta" aria-label="Default select example">
                        <option v-for="(value, key) in grupos" :key="key" :value="value">
                            {{ value }}
                        </option>
                    </select>
                </div> <!-- TODO -->
                <!-- <div class="mb-3">
                    <label for="grupo_conviviente" class="col-form-label fw-semibold">Grupo conviviente:</label>
                    <select class="form-select border border-dark-subtle" v-model.lazy="persona.grupo_conviviente" aria-label="Default select example">
                        <option v-for="(value, key) in grupos" :key="key" :value="value">
                            {{ value }}
                        </option>
                    </select>
                </div>
                <div v-if="persona.grupo_conviviente == 'Otro'" class="mb-3">
                    <label for="grupo_conviviente_otro" class="col-form-label fw-semibold">Indique otro grupo conviviente:</label>
                    <input v-model.lazy="persona.grupo_conviviente_otro" type="text" id="grupo_conviviente_otro" class="form-control shadow-sm" required />
                    <div class="invalid-feedback">
                        Por favor, ingresa otro grupo conviviente.
                    </div>
                </div>
            <div v-if="!existeDato.localidad" class="mb-3">
                <label for="localidad" class="col-form-label fw-semibold">Localidad:</label>
                <input v-model.lazy="persona.localidad" type="text" id="localidad" class="form-control shadow-sm" />
            </div>
            <div v-if="!existeDato.identidad_genero">
                <div class="mb-3">
                    <label for="identidad_genero" class="col-form-label fw-semibold">Identidad de género:</label>
                    <select class="form-select border border-dark-subtle" v-model="persona.identidad_genero" aria-label="Default select example">
                        <option v-for="genero in generos" :key="genero" :value="genero">
                            {{ genero.tipo }}
                        </option>
                    </select>
                </div>
                <div v-if="persona.identidad_genero">
                    <div v-if="persona.identidad_genero.tipo == 'Otra identidad'" class="mb-3">
                        <label for="identidad_genero_otro" class="col-form-label fw-semibold">Indique otra identidad de género:</label>
                        <input v-model="persona.identidad_genero.otro_tipo" type="text" id="identidad_genero_otro" class="form-control shadow-sm" required />
                        <div class="invalid-feedback">
                            Por favor, ingresa otra identidad de genero.
                        </div>
                    </div>
                </div>    
            </div>
            <div v-if="!existeDato.tiene_obra_social">    
                <fieldset class="mb-3">
                    <legend class="col-form-label pt-0 fw-semibold">¿Tiene obra social?:</legend>
                    <div class="d-flex column-gap-4">
                        <div class="form-check">
                            <input class="form-check-input shadow-sm" type="radio" name="si_tiene_obra_social" id="si_tiene_obra_social" v-model.lazy="persona.tiene_obra_social" :value="true">
                            <label class="form-check-label" for="si_tiene_obra_social">
                                Sí
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input shadow-sm" type="radio" name="no_tiene_obra_social" id="no_tiene_obra_social" v-model.lazy="persona.tiene_obra_social" :value="false">
                            <label class="form-check-label" for="no_tiene_obra_social">
                                No
                            </label>
                        </div>
                    </div>    
                </fieldset>
                <div v-if="persona.tiene_obra_social" class="mb-3">
                    <label for="obra_social" class="col-form-label fw-semibold">¿Cual obra social posee?:</label>
                    <input v-model="persona.obra_social" type="text" id="obra_social" class="form-control shadow-sm" required />
                    <div class="invalid-feedback">
                        Por favor, ingrese el nombre de la obra social que posee.
                    </div>
                </div>
            </div>
            <div v-if="!existeDato.motivo_gral_acomp">    
                <div class="mb-3">
                    <label for="motivo_gral_acomp" class="col-form-label fw-semibold">Motivo general de acompañamiento:</label>
                    <select class="form-select border border-dark-subtle" v-model.lazy="persona.motivo_gral_acomp" aria-label="Default select example">
                        <option v-for="motivo in motivosAcomp" :key="motivo" :value="motivo">
                            {{ motivo.tipo }}
                        </option>
                    </select>
                </div>
                <div v-if="persona.motivo_gral_acomp">
                    <fieldset v-if="persona.motivo_gral_acomp.tipo == 'Malestar emocional'" class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0 fw-semibold">Malestar emocional</legend>
                        <div v-for="malestar in malestares" :key="malestar" class="form-check">
                            <input
                                class="form-check-input shadow-sm"
                                type="checkbox"
                                :id="malestar.tipo"
                                :value="malestar.tipo"
                                @change="actualizarLista(persona.motivo_gral_acomp.malestares_emocionales, malestar)"
                            />
                            <label :for="malestar" class="form-check-label">{{ malestar.tipo }}</label>
                        </div>    
                    </fieldset>
                </div>
            </div>    
            <fieldset v-if="!existeDato.situaciones_vulnerabilidad" class="row mb-3">
                <legend class="col-form-label col-sm-2 pt-0 fw-semibold">Situación de vulnerabilidad</legend>
                <div v-for="situacion in situaciones" :key="situacion" class="form-check">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="situacion.tipo"
                        :value="situacion.tipo"
                        @change="actualizarLista(persona.situaciones_vulnerabilidad, situacion)"
                    />
                    <label :for="situacion" class="form-check-label">{{ situacion.tipo }}</label>
                </div>    
            </fieldset>
            <div class="mb-3">
                <label for="detalle_acompanamiento" class="col-form-label fw-semibold">Detalle del acompañamiento:</label>
                <input v-model.lazy="persona.detalle_acompanamiento" type="text" id="detalle_acompanamiento" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese un breve detalle del acompañamiento.
                </div>
            </div>
            <div class="mb-3">
                <label for="detalle" class="col-form-label fw-semibold">Detalle:</label>
                <input v-model="llamada.detalle" type="text" id="detalle" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese un breve detalle de la llamada.
                </div>
            </div>
            <div class="mb-3">
                <label for="resolucion" class="col-form-label fw-semibold">Resolución:</label>
                <select class="form-select border border-dark-subtle" v-model="llamada.resolucion" aria-label="Default select example">
                    <option v-for="(value, key) in resoluciones" :key="key" :value="value">
                        {{ value }}
                    </option>
                </select>
            </div>
            <div v-if="llamada.resolucion == 'Continua acompañamiento' || llamada.resolucion == 'Comunicación fallida' " class="mb-3">
                <label for="fecha_prox_llamado" class="col-form-label fw-semibold">Fecha del próximo llamado:</label>
                <input v-model="llamada.fecha_prox_llamado" type="date" id="fecha_prox_llamado" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese una fecha del próximo llamado.
                </div>
            </div>
            <div class="d-flex justify-content-center">
                <button type="submit" class="btn btn-info text-white fw-semibold shadow-sm">Guardar</button>
            </div>
        --> </form>
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
    data() {
        return {
            persona: null,

            existeDato: {},

            llamada: {
                detalle: '',
                resolucion: '',
                fecha_prox_llamado: null,
            },

            grupos: [],
            generos: [],
            motivosAcomp: [],
            malestares: [],
            situaciones: [],
            resoluciones: [],
            errores: [],
        }
    },

    async created() {
        
        await apiService.get(import.meta.env.VITE_API_URL + "cetecsm/persona/perfil/" + this.$route.params.id)
            .then((response) => {
                this.persona = response.data;
                this.comprobarDatos();
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            });
        
        await apiService.get(import.meta.env.VITE_API_URL + "mot_grales_acomp")
            .then((response) => {
                this.motivosAcomp = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "grupos_convivientes")
            .then((response) => {
                this.grupos = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

        await apiService.get(import.meta.env.VITE_API_URL + "identidades_genero")
            .then((response) => {
                this.generos = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "malestares_emocionales")
            .then((response) => {
                this.malestares = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "situaciones_vulnerabilidad")
            .then((response) => {
                this.situaciones = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

        await apiService.get(import.meta.env.VITE_API_URL + "resoluciones")
            .then((response) => {
                this.resoluciones = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })      
    },

    methods: {
        async registrarLlamada() {
            const form = this.$refs.formulario;
            if (form.checkValidity()) {
                try {
                    await apiService.post(import.meta.env.VITE_API_URL + "cetecsm/llamada/crear/" + this.$route.params.id, 
                    {
                        persona: this.persona,
                        llamada: this.llamada,
                    })
                    .then((response) => {
                        if(response.status == 200) {
                            displaySuccess(this.$toast, "Llamada creada exitosamente");
                            this.$router.push("/cetecsm/asignaciones");
                        }
                    })
                } catch(error) {
                    displayError(this.$toast, error);
                    this.errores.push(error);
                }
            } else {
                console.log('Formulario no válido. Realiza acciones adicionales...');
                form.classList.add('was-validated');
            }    
        },

        actualizarLista(lista, elemento) {
            if (this.chequearLista(lista, elemento)) {
                lista.splice(lista.indexOf(elemento), 1); 
            } else {
                lista.push(elemento)
            }
        },

        chequearLista(lista, elemento) {
            return lista.some((l) => l.tipo == elemento.tipo)
        },

        comprobarDatos() {
            const camposAVerificar = ["grupo_conviviente", "localidad", "identidad_genero", "tiene_obra_social", "motivo_gral_acomp", "situaciones_vulnerabilidad"]
            camposAVerificar.forEach((campo) => {
                if(Array.isArray(this.persona[campo])){
                    this.existeDato[campo] = this.persona[campo].length > 0;
                } else {
                    this.existeDato[campo] = this.persona[campo] !== null && this.persona[campo] !== undefined;
                }
            });
        },
    }
}
</script>