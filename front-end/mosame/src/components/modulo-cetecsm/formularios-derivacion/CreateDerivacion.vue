<template>
    <div class="p-4 border border-secondary-subtle shadow">
        <h2 class="fw-bold mb-4">Registrar derivación</h2>
        <form ref="formulario" class="px-5 needs-validation" @submit.prevent="saveDerivation" novalidate>
            <div class="mb-3 has-validation">
                <label for="fecha" class="col-form-label fw-semibold">Fecha de derivación:</label>
                <input v-model="derivacion.fecha" type="date" id="fecha" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, selecciona una fecha válida.
                </div>
            </div>
            <fieldset class="mb-3">
                <legend class="col-form-label pt-0 fw-semibold">¿Dio consentimiento?</legend>
                <div class="d-flex column-gap-4">
                    <div class="form-check">
                        <input class="form-check-input shadow-sm" type="radio" name="flexRadioDefault" id="flexRadioDefault1" v-model="persona.dio_consentimiento" :value="true" checked>
                        <label class="form-check-label" for="flexRadioDefault1">
                            Sí
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input shadow-sm" type="radio" name="flexRadioDefault" id="flexRadioDefault2" v-model="persona.dio_consentimiento" :value="false">
                        <label class="form-check-label" for="flexRadioDefault2">
                            No
                        </label>
                    </div>
                </div>    
            </fieldset>
            <div class="mb-3">
                <label for="dispositivo_derivador" class="col-form-label fw-semibold">Dispositivo que deriva:</label>
                <input v-model="derivacion.dispositivo_derivacion" type="text" id="dispositivo_derivador" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese el dispositivo que deriva.
                </div>
            </div>
            <div class="mb-3">
                <label for="nombre_operador_derivador" class="col-form-label fw-semibold">Nombre del operador que deriva:</label>
                <input v-model="derivacion.nombre_operador_derivador" type="text" id="nombre_operador_derivador" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa el nombre del operador que deriva.
                </div>
            </div>
            <div class="mb-3">
                <label for="municipio" class="col-form-label fw-semibold">Municipio:</label>
                <select class="form-select border border-dark-subtle" v-model="persona.municipio" aria-label="Default select example" required>
                    <option v-for="municipio in municipios" :key="municipio">
                        {{ municipio.nombre }}
                    </option>
                </select>
                <div class="invalid-feedback">
                    Por favor, seleccione un municipio.
                </div>
            </div>
            <div class="mb-3">
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
                <label for="edad" class="col-form-label fw-semibold">Edad:</label>
                <input v-model="persona.edad" type="number" min="0" max="120" id="edad" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese una edad en el rango de 0 a 120.
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
                <label for="telefono_alternativo" class="col-form-label fw-semibold">Motivo general de derivación:</label>
                <select class="form-select border border-dark-subtle" v-model="derivacion.mot_gral_derivacion.tipo" aria-label="Default select example">
                    <option v-for="motivo in motivos_grales_derivacion" :key="motivo">
                        {{ motivo.tipo }}
                    </option>
                </select>
                <p>{{ derivacion.mot_gral_derivacion.tipo }}</p>
            </div>
            <div v-if="derivacion.mot_gral_derivacion">
                <div v-if="derivacion.mot_gral_derivacion.tipo == 'Otro'" class="mb-4">
                    <label for="otro_mot_gral_derivacion" class="col-form-label fw-semibold">Otro tipo de motivo general de derivación:</label>
                    <input v-model="derivacion.mot_gral_derivacion.otro_tipo" type="text" id="otro_mot_gral_derivacion" class="form-control shadow-sm" required />
                    <div class="invalid-feedback">
                        Por favor, ingrese otro tipo de motivo general de derivación.
                    </div>
                </div>
            </div>    
            <div class="mb-4">
                <label for="descripcion" class="col-form-label fw-semibold">Descripción:</label>
                <input v-model="derivacion.descripcion" type="text" id="descripcion" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingrese una descripcion de la derivación.
                </div>
            </div>
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
            persona: {
                municipio: '',
                dio_consentimiento: false,
                nombre: '',
                apellido: '',
                edad: 0,
                dni: '',
                telefono: '',
                telefono_alternativo: '',
            },

            derivacion: {
                fecha: '',
                dispositivo_derivacion: '',
                nombre_operador_derivador: '',
                mot_gral_derivacion: {
                    tipo: '',
                    otro_tipo:'',
                },
                descripcion: '',
            },

            errors: [],
            motivos_grales_derivacion: [],
            municipios: [],
        };
    },

    async created() {
        await apiService.get(import.meta.env.VITE_API_URL + "mot_grales_derivacion")
            .then((response) => {
                this.motivos_grales_derivacion = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "municipios")
            .then((response) => {
                this.municipios = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
           
    },

    methods: {
        async saveDerivation() {
            const form = this.$refs.formulario;
            if (form.checkValidity()) {
                try {
                    await apiService.post(import.meta.env.VITE_API_URL + "cetecsm/derivacion/create", 
                    {
                        persona: this.persona,
                        derivacion: this.derivacion,
                    })
                    .then((response) => {
                        if(response.status == 200) {
                            displaySuccess(this.$toast, "Derivacion registrada exitosamente");
                            this.$router.push("/cetecsm/derivaciones");
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
        }
    }
}
</script>