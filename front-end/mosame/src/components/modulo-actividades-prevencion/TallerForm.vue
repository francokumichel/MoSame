<template>
    <h2 class="fw-bold mb-4">Registrar taller</h2>
    <p>Los campos marcados con <span class="text-danger">*</span> son obligatorios.</p>
    <form ref="formulario" class="px-5 needs-validation" @submit.prevent="registrarTaller" novalidate>
        <div class="mb-3">
            <label for="municipio" class="col-form-label fw-semibold">Municipios: <span class="text-danger">*</span></label>
            <select required @change="cargarEscuelasYLocalidades" class="form-select border border-dark-subtle" v-model.lazy="taller.municipio" aria-label="Default select example">
                <option hidden disabled value="">Seleccione una opción</option>
                <option v-for="municipio in municipios" :key="municipio" :value="municipio">
                    {{ municipio.nombre }}
                </option>
            </select>
            <div class="invalid-feedback">
                Por favor, seleccione un municipio.
            </div>
        </div>
        <div class="mb-3">
            <label for="localidad" class="col-form-label fw-semibold">Localidad: <span class="text-danger">*</span></label>
            <select required class="form-select border border-dark-subtle" v-model.lazy="taller.localidad" aria-label="Default select example" :disabled="localidades.length == 0">
                <option hidden disabled value="">Seleccione una opción</option>
                <option v-for="localidad in localidades" :key="localidad" :value="localidad">
                    {{ localidad }}
                </option>
            </select>
            <div class="invalid-feedback">
                Por favor, seleccione una localidad.
            </div>
        </div>
        <div class="mb-3">
            <label for="dispositivo" class="col-form-label fw-semibold">Dispositivo: <span class="text-danger">*</span></label>
            <select required class="form-select border border-dark-subtle" v-model.lazy="taller.dispositivo" aria-label="Default select example">
                <option hidden disabled value="">Seleccione una opción</option>
                <option v-for="dispositivo in dispositivos" :key="dispositivo" :value="dispositivo.nombre">
                    {{ dispositivo.nombre }}
                </option>
            </select>
            <div class="invalid-feedback">
                Por favor, seleccione un dispositivo.
            </div>
        </div>
        <div class="mb-3">
            <label for="tipo_actividad" class="col-form-label fw-semibold">Tipo actividad: <span class="text-danger">*</span></label>
            <select required class="form-select border border-dark-subtle" v-model.lazy="actividad.tipo" aria-label="Default select example">
                <option hidden disabled value="">Seleccione una opción</option>
                <option v-for="(value, key) in tipos_taller" :key="key" :value="value">
                    {{ value }}
                </option>
            </select>
            <div class="invalid-feedback">
                Por favor, seleccione una localidad.
            </div>
        </div>
        <div v-if="actividad.tipo">
            <div v-if="actividad.tipo == 'Talleres de Salud Mental en las Escuelas'">
                <div class="mb-3">
                    <label for="escuela" class="col-form-label fw-semibold">Escuela: <span class="text-danger">*</span></label>
                    <select required class="form-select border border-dark-subtle" v-model.lazy="escuela_seleccionada" aria-label="Default select example" :disabled="escuelas.length == 0">
                        <option hidden disabled value="">Seleccione una opción</option>
                        <option v-for="escuela in escuelas" :key="escuela" :value="escuela">
                            {{ escuela.nombre }}
                        </option>
                    </select>
                    <div class="invalid-feedback">
                        Por favor, seleccione una escuela.
                    </div>
                </div>
                <div v-if="escuela_seleccionada">
                    <div class="mb-3">
                        <label for="edad" class="col-form-label fw-semibold">Nombre escuela:</label>
                        <input v-model="escuela_seleccionada.nombre" type="text" id="nombre_escuela" class="form-control border border-dark-subtle" readonly disabled/>
                    </div>
                    <div class="mb-3">
                        <label for="cue" class="col-form-label fw-semibold">Código único de establecimiento (CUE):</label>
                        <input v-model="escuela_seleccionada.cue" type="text" id="cue" class="form-control border border-dark-subtle" readonly disabled/>
                    </div>
                    <div class="mb-3">
                        <label for="sector" class="col-form-label fw-semibold">Gestión:</label>
                        <input v-model="escuela_seleccionada.sector" type="text" id="sector" class="form-control border border-dark-subtle" readonly disabled/>
                    </div>
                    <div class="mb-3">
                        <label for="nivel" class="col-form-label fw-semibold">Nivel:</label>
                        <input v-model="escuela_seleccionada.niveles" type="text" id="nivel" class="form-control border border-dark-subtle" readonly disabled/>
                    </div>
                    <div class="mb-3">
                        <label for="modalidad" class="col-form-label fw-semibold">Modalidad:</label>
                        <input v-model="escuela_seleccionada.modalidad" type="text" id="modalidad" class="form-control border border-dark-subtle" readonly disabled/>
                    </div>
                </div>
                <div class="mb-3">
                    <label for="años_divisiones" class="col-form-label fw-semibold">Años y sección/curso/división: <span class="text-danger">*</span></label>
                    <div v-for="(item, index) in actividad.anios" :key="index" class="d-flex mb-2">
                        <div class="d-flex">
                            <div class="d-flex flex-column ms-2 mb-2">
                                <select required class="align-self-start form-select" size="1" v-model="item.anio">
                                    <option hidden disabled value="">Seleccione un año</option>
                                    <option v-for="anio in ordenarValores(anios)" :key="anio" :value="anio">
                                        {{ anio }}
                                    </option>
                                </select>
                                <div class="invalid-feedback">
                                    Por favor. seleccione un año.
                                </div>
                            </div>
                            <div class="d-flex flex-column ms-2 mb-2">
                                <select required class="form-select" size="3" v-model="item.divisiones" :disabled="!item.anio" multiple>
                                    <option hidden disabled value="">Seleccione una o varias divisiones</option>
                                    <option v-for="division in ordenarValores(divisiones)" :key="division" :value="division">
                                        {{ division }}
                                    </option>
                                </select>
                                <div v-if="divisionesRepetidas(index) && formEnviado" class="text-danger" style="font-size:14px;">
                                    No se pueden repetir divisiones para el mismo año
                                </div>
                                <div class="invalid-feedback">
                                    Por favor, seleccione al menos una division.
                                </div>
                            </div>
                        </div>
                        <div class="d-flex">
                            <button class="btn btn-secondary align-self-start ms-2 mb-2" @click.prevent="removeAnio(index)" v-if="index > 0">-</button>
                            <button class="btn btn-primary align-self-start ms-2 mb-2" @click.prevent="addAnio(index)" v-if="index === actividad.anios.length - 1">+</button>
                        </div>
                    </div>
                </div>
                <div class="mb-3">
                    <label for="cant_encuentros" class="col-form-label fw-semibold">Cantidad de encuentros: <span class="text-danger">*</span></label>
                    <input required v-model="actividad.cant_encuentros" type="number" min="1" max="10" id="cant_encuentros" class="form-control border border-dark-subtle" />
                    <div class="invalid-feedback">
                        Ingrese una cantidad de encuentros en el rango de 1 a 10.
                    </div>
                </div>
            </div>
            <div class="mb-3">
                <label for="cant_participantes" class="col-form-label fw-semibold">{{ actividad.tipo == 'Talleres de Salud Mental en las Escuelas' ? 'Cantidad Promedio de Jóvenes que participaron:' : 'Cantidad de participantes:'}} <span class="text-danger">*</span></label>
                <input required v-model="actividad.cant_participantes" type="number" min="0" id="cant_participantes" class="form-control border border-dark-subtle"/>
                <div class="invalid-feedback">
                    Por favor, ingrese una cantidad de participantes.
                </div>
            </div>
            <div v-if="actividad.tipo == 'Espacio Grupal en el Dispositivo'" class="mb-3">
                <label for="actividad_interna" class="col-form-label fw-semibold">Actividad: <span class="text-danger">*</span></label>
                <select required class="form-select border border-dark-subtle" v-model.lazy="actividad.actividades" aria-label="Default select example">
                    <option hidden disabled value="">Seleccione una opción</option>
                    <option v-for="actividad in actividades_internas" :key="actividad" :value="actividad.nombre">
                        {{ actividad.nombre }}
                    </option>
                </select>
                <div class="invalid-feedback">
                    Por favor, seleccione una actividad interna.
                </div>
            </div>
            <div v-if="actividad.tipo == 'Acciones de Promoción y Prevención en la Comunidad'" class="mb-3">
                <label for="actividad_externa" class="col-form-label fw-semibold">Actividad: <span class="text-danger">*</span></label>
                <select required class="form-select border border-dark-subtle" v-model.lazy="actividad.actividades" aria-label="Default select example">
                    <option hidden disabled value="">Seleccione una opción</option>
                    <option v-for="actividad in actividades_externas" :key="actividad" :value="actividad.nombre">
                        {{ actividad.nombre }}
                    </option>
                </select>
                <div class="invalid-feedback">
                    Por favor, seleccione una actividad externa.
                </div>
            </div>
            <div class="mb-3">
                <label for="observaciones" class="col-form-label fw-semibold">Observaciones:</label>
                <textarea rows="6" v-model="actividad.observaciones" id="observaciones" class="form-control border border-dark-subtle"></textarea>
            </div>
            <div class="d-flex justify-content-center">
                <button type="submit" class="btn btn-info text-white fw-semibold shadow-sm">Guardar</button>
            </div>
        </div>
    </form>
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
    data() {
        return {
            taller: {
                municipio: '',
                localidad: '',
                dispositivo: ''
            },

            actividad: {
                tipo: '',
                anios: [{anio: '', divisiones: []}],
                cant_participantes: '',
                cant_encuentros: '',
                observaciones: '',
                actividades: '',
            },

            formEnviado: false,
            escuela_seleccionada: null,
            municipios: [],
            localidades: [],
            dispositivos: [],
            tipos_taller: [],
            escuelas: [],
            anios: [],
            divisiones: [],
            actividades_internas: [],
            actividades_externas: [],
            errores: [],
        }
    },

    async created() {
        await apiService.get(import.meta.env.VITE_API_URL + "municipios")
            .then((response) => {
                this.municipios = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
            
        await apiService.get(import.meta.env.VITE_API_URL + "actividades/dispositivos")
            .then((response) => {
                this.dispositivos = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "actividades/tipos_taller")
            .then((response) => {
                this.tipos_taller = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

        await apiService.get(import.meta.env.VITE_API_URL + "actividades/años")
            .then((response) => {
                this.anios = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

        await apiService.get(import.meta.env.VITE_API_URL + "actividades/divisiones")
            .then((response) => {
                this.divisiones = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "actividades/actividades_internas")
            .then((response) => {
                this.actividades_internas = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "actividades/actividades_externas")
            .then((response) => {
                this.actividades_externas = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
    },

    methods: {

        async registrarTaller() {
            const form = this.$refs.formulario;
            this.formEnviado = true;
            const isValid = this.checkValidity();

            if (isValid) {
                try {
                    await apiService.post(import.meta.env.VITE_API_URL + "actividades/registrar_taller",
                        {
                            taller: this.taller,
                            actividad: this.actividad,
                            escuela: this.escuela_seleccionada
                        })
                    .then((response) => {
                        if(response.status == 200) {
                            this.formEnviado = false;
                            displaySuccess(this.$toast, "Taller registrado exitosamente");
                            this.limpiarFormulario()
                            this.$router.push({ path: this.$route.path });
                        }
                    })
                } catch(error) {
                    console.log(error)
                    displayError(this.$toast, error);
                    this.errores.push(error);
                }
            } else {
                console.log('Formulario no válido. Realiza acciones adicionales...');
                form.classList.add('was-validated');
            }
        },

        async cargarEscuelasYLocalidades() {
            this.localidades = this.taller.municipio.localidades.split(', ');
            console.log(this.taller.municipio.nombre)
            await apiService.get(import.meta.env.VITE_API_URL + "actividades/escuelas", {
                    params: {
                        municipio: this.taller.municipio.nombre,
                    } 
                })
                .then((response) => {
                    this.escuelas = response.data;
                    console.log(this.escuelas);
                })
                .catch((e) => {
                    console.log(e)
                    this.errores.push(e);
                })
        },

        addAnio(index) {
            if (this.actividad.anios[index].anio.trim() !== '') {
                this.actividad.anios.push({ anio: '', divisiones: [] });
            }
        },

        removeAnio(index) {
            if (this.actividad.anios.length > 1) {
                this.actividad.anios.splice(index, 1);
            }
        },

        divisionesRepetidas(index) {
            const anioActual = this.actividad.anios[index].anio;
            const divisionesActuales = this.actividad.anios[index].divisiones;

            // Verifica si hay divisiones repetidas para el mismo año
            const otrasDivisionesMismoAnio = this.actividad.anios
                .filter((item, i) => i !== index && item.anio === anioActual)
                .flatMap(item => item.divisiones);

            return divisionesActuales.some(division => otrasDivisionesMismoAnio.includes(division));
        },

        validateForm() {
            const selectedAnios = this.actividad.anios.map(item => item.anio);

            // Verifica que no haya divisiones repetidas para el mismo año
            const hasDuplicateDivisions = selectedAnios.some((anio, index) => this.divisionesRepetidas(index));

            // Realiza otras validaciones según tus criterios
            const basicValidation = this.actividad.anios.every(item => item.anio.trim() !== '' && item.divisiones.length > 0);

            // Retorna true si todas las validaciones son exitosas, false en caso contrario
            return basicValidation && !hasDuplicateDivisions;
        },

        checkValidity() {
            // Realiza tu propia lógica de validación personalizada
            const isValid = this.actividad.tipo != 'Talleres de Salud Mental en las Escuelas' ? true : this.validateForm();

            // Aplica la lógica de validación de Bootstrap
            const form = this.$refs.formulario; // Asegúrate de asignar una referencia a tu formulario en el atributo ref

            // Retorna true si tanto tu lógica personalizada como la de Bootstrap son exitosas, false en caso contrario
            return form.checkValidity() && isValid;
        },


        ordenarValores(diccionario) {
            // Convertir el objeto a una matriz de pares clave-valor
            const arrayDiccionario = Object.entries(diccionario);

            // Ordenar la matriz según los valores (índice 1)
            arrayDiccionario.sort((a, b) => a[1].localeCompare(b[1]));

            // Convertir la matriz ordenada de nuevo a un objeto
            const diccionarioOrdenado = Object.fromEntries(arrayDiccionario);

            return diccionarioOrdenado;
        },

        limpiarFormulario() {

            this.taller = {
                municipio: '',
                localidad: '',
                dispositivo: ''
            };

            this.actividad = {
                tipo: '',
                anios: [{ anio: '', divisiones: [] }],
                cant_participantes: '',
                cant_encuentros: '',
                observaciones: '',
                actividades: '',
            };
        },

    }
}
</script>