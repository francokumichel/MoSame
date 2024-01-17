<template>
    <div v-if="persona" class="p-4 border border-secondary-subtle shadow">
        <h2 class="fw-bold mb-4">Editar persona</h2>
        <form ref="formulario" class="px-5 needs-validation" @submit.prevent="editarPersona" novalidate>
            <div class="mb-3 has-validation">
                <label for="nombre" class="col-form-label fw-semibold">Nombre:</label>
                <input v-model="persona.nombre" type="text" id="nombre" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa un el nombre de la persona derivada.
                </div>
            </div>
            <div class="mb-3">
                <label for="apellido" class="col-form-label fw-semibold">Apellido:</label>
                <input v-model="persona.apellido" type="text" id="apellido" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa el apellido de la persona derivada.
                </div>
            </div>
            <div class="mb-3">
                <label for="dni" class="col-form-label fw-semibold">DNI:</label>
                <input v-model="persona.dni" type="text" id="dni" pattern="[0-9]{7,8}" title="Ingrese el número de DNI sin puntos ('Ej: 42456789')" class="form-control shadow-sm" />
                <div class="invalid-feedback">
                    El DNI debe ingresarse sin puntos y contener entre 7 y 8 dígitos.
                </div>
            </div>
            <div class="mb-3">
                <label for="telefono" class="col-form-label fw-semibold">Telefono:</label>
                <input v-model="persona.telefono" type="tel" id="telefono" pattern="[0-9]{8,14}" title="Ingrese un número de teléfono sin guiones ni puntos" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese un teléfono que contenga entre 8 y 14 dígitos (ej: '1122334455').
                </div>
            </div>
            <div class="mb-3">
                <label for="telefono_alternativo" class="col-form-label fw-semibold">Telefono alternativo (opcional):</label>
                <input v-model="persona.telefono_alternativo" type="tel" id="telefono_alternativo" pattern="[0-9]{8,14}" title="Ingrese un número de teléfono sin guiones ni puntos" class="form-control shadow-sm" />
                <div class="invalid-feedback">
                    El teléfono debe contener entre 8 y 14 dígitos (ej: '1122334455').
                </div>
            </div>
            <div class="mb-3">
                <label for="localidad" class="col-form-label fw-semibold">Localidad:</label>
                <input v-model="persona.localidad" type="text" id="localidad" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese una localidad.
                </div>
            </div>
            <div class="mb-3">
                <label for="municipio" class="col-form-label fw-semibold">Municipio:</label>
                <select class="form-select border border-dark-subtle" v-model="persona.municipio.nombre" aria-label="Default select example">
                    <option v-for="municipio in municipios" :key="municipio">
                        {{ municipio.nombre }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="detalle_acompanamiento" class="col-form-label fw-semibold">Detalle del acompañamiento:</label>
                <input v-model="persona.detalle_acompanamiento" type="text" id="detalle_acompanamiento" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa un el nombre de la persona derivada.
                </div>
            </div>
            <fieldset class="mb-3">
                <legend class="col-form-label pt-0 fw-semibold">¿Dio consentimiento?</legend>
                <div class="d-flex column-gap-4">
                    <div class="form-check">
                        <input class="form-check-input shadow-sm" type="radio" name="flexRadioDefault" id="flexRadioDefault1" v-model="persona.dio_consentimiento" :value="true" :checked="persona.dio_consentimiento">
                        <label class="form-check-label" for="flexRadioDefault1">
                            Sí
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input shadow-sm" type="radio" name="flexRadioDefault" id="flexRadioDefault2" v-model="persona.dio_consentimiento" :value="false" :checked="!persona.dio_consentimiento">
                        <label class="form-check-label" for="flexRadioDefault2">
                            No
                        </label>
                    </div>
                </div>    
            </fieldset>
            <div class="mb-3">
                <label for="grupo_conviviente" class="col-form-label fw-semibold">Grupo conviviente:</label>
                <select class="form-select border border-dark-subtle" v-model="persona.grupo_conviviente" aria-label="Default select example">
                    <option v-for="(value, key) in grupos" :key="key" :value="value">
                        {{ value }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="identidad_genero" class="col-form-label fw-semibold">Identidad de género:</label>
                <select class="form-select border border-dark-subtle" v-model="persona.identidad_genero.tipo" aria-label="Default select example">
                    <option v-for="genero in generos" :key="genero">
                        {{ genero.tipo }}
                    </option>
                </select>
            </div>
            <fieldset class="mb-3">
                <legend class="col-form-label pt-0 fw-semibold">¿Tiene obra social?</legend>
                <div class="d-flex column-gap-4">
                    <div class="form-check">
                        <input class="form-check-input shadow-sm" type="radio" name="si_dio_consentimiento" id="si_dio_consentimiento" v-model="persona.tiene_obra_social" :value="true" :checked="persona.tiene_obra_social">
                        <label class="form-check-label" for="flexRadioDefault1">
                            Sí
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input shadow-sm" type="radio" name="no_dio_consentimiento" id="no_dio_consentimiento" v-model="persona.tiene_obra_social" :value="false" :checked="!persona.tiene_obra_social">
                        <label class="form-check-label" for="flexRadioDefault2">
                            No
                        </label>
                    </div>
                </div>    
            </fieldset>
            <div v-if="persona.tiene_obra_social" class="mb-3">
                <label for="obra_social" class="col-form-label fw-semibold">¿Cual?</label>
                <input v-model="persona.obra_social" type="text" id="obra_social" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese una localidad.
                </div>
            </div>
            <div class="mb-3">
                <label for="motivo_gral_acomp" class="col-form-label fw-semibold">Motivo general de acompañamiento:</label>
                <select class="form-select border border-dark-subtle" v-model="persona.motivo_gral_acomp.tipo" aria-label="Default select example">
                    <option v-for="motivo in motivosAcomp" :key="motivo">
                        {{ motivo.tipo }}
                    </option>
                </select>
            </div>
            <fieldset v-if="persona.motivo_gral_acomp.tipo == 'Malestar emocional'" class="row mb-3">
                <legend class="col-form-label col-sm-2 pt-0 fw-semibold">Malestar emocional</legend>
                <div v-for="malestar in malestares" :key="malestar" class="form-check">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="malestar.tipo"
                        :value="malestar.tipo"
                        :checked="chequearLista(persona.motivo_gral_acomp.malestares_emocionales, malestar)"
                        @change="actualizarLista(persona.motivo_gral_acomp.malestares_emocionales, malestar)"
                    />
                    <label :for="malestar" class="form-check-label">{{ malestar.tipo }}</label>
                </div>    
            </fieldset>
            <fieldset class="row mb-3">
                <legend class="col-form-label col-sm-2 pt-0 fw-semibold">Situación de vulnerabilidad</legend>
                <div v-for="situacion in situaciones" :key="situacion" class="form-check">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="situacion.tipo"
                        :value="situacion.tipo"
                        :checked="chequearLista(persona.situaciones_vulnerabilidad, situacion)"
                        @change="actualizarLista(persona.situaciones_vulnerabilidad, situacion)"
                    />
                    <label :for="situacion" class="form-check-label">{{ situacion.tipo }}</label>
                </div>    
            </fieldset>
            <div class="d-flex justify-content-center">
                <button type="submit" class="btn btn-info text-white fw-semibold shadow-sm">Guardar</button>
            </div>
        </form>
    </div>
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
    data() {
        return {
            persona: null,
            grupos: [],
            generos: [],
            municipios: [],
            motivosAcomp: [],
            malestares: [],
            situaciones: [],
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
        
        await apiService.get(import.meta.env.VITE_API_URL + "municipios")
            .then((response) => {
                this.municipios = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

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
        
    },

    methods: {
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

        async editarPersona() {
            const form = this.$refs.formulario;
            if (form.checkValidity()) {
                try {
                    await apiService.post(import.meta.env.VITE_API_URL + "cetecsm/persona/editar/" + this.$route.params.id, 
                    {
                        persona: this.persona,
                    })
                    .then((response) => {
                        if(response.status == 200) {
                            displaySuccess(this.$toast, "Persona editada exitosamente");
                            this.$router.push("/cetecsm/asignaciones");
                        }
                    })
                } catch(error) {
                    displayError(this.$toast, error);
                    this.errors.push(error);
                }
            } else {
                console.log('Formulario no válido. Realiza acciones adicionales...');
                form.classList.add('was-validated');
            }    
        },
    }
};
</script>