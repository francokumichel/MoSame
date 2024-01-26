<template>
        <h2 class="fw-bold mb-4">Registrar llamada</h2>
        <form ref="formulario" class="px-5 needs-validation" @submit.prevent="registrarLlamada" novalidate>
            <div class="mb-3">
                <label for="motivo_de_consulta" class="col-form-label fw-semibold">Motivo de la consulta:</label>
                <select class="form-select border border-dark-subtle" v-model.lazy="llamada.motivo_consulta" aria-label="Default select example">
                    <option v-for="(value, key) in motivos" :key="key" :value="value.nombre">
                        {{ value.nombre }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="como_ubico" class="col-form-label fw-semibold">Cómo nos ubicaste?:</label>
                <select class="form-select border border-dark-subtle" v-model.lazy="llamada.como_ubico" aria-label="Default select example">
                    <option v-for="(value, key) in formas_ubico" :key="key" :value="value.forma">
                        {{ value.forma }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="municipio" class="col-form-label fw-semibold">Municipio:</label>
                <select class="form-select border border-dark-subtle" v-model.lazy="llamada.municipio" aria-label="Default select example">
                    <option v-for="(value, key) in municipios" :key="key" :value="value.nombre">
                        {{ value.nombre }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="sujeto" class="col-form-label fw-semibold">Sujeto de la consulta:</label>
                <select required class="form-select border border-dark-subtle" v-model.lazy="llamada.sujeto" aria-label="Default select example">
                    <option v-for="(value, key) in sujetos" :key="key" :value="value">
                        {{ value }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="edad" class="col-form-label fw-semibold">Edad:</label>
                <input v-model="llamada.edad" type="number" min="0" max="120" id="edad" class="form-control border border-dark-subtle"/>
                <div class="invalid-feedback">
                    Por favor, ingrese una edad en el rango de 0 a 120.
                </div>
            </div>
            <div class="mb-3">
                <label for="identidad_genero" class="col-form-label fw-semibold">Identidad de género:</label>
                <select class="form-select border border-dark-subtle" v-model="llamada.identidad_genero" aria-label="Default select example">
                    <option v-for="genero in generos" :key="genero" :value="genero.tipo">
                        {{ genero.tipo }}
                    </option>
                </select>
            </div>
            <div v-if="llamada.identidad_genero == 'Otra identidad'" class="mb-3">
                <label for="identidad_genero_otro" class="col-form-label fw-semibold">Indique otra identidad de género:</label>
                <input v-model="llamada.identidad_genero_otra" type="text" id="identidad_genero_otro" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa otra identidad de genero.
                </div>
            </div>
            <div class="mb-3">
                <label for="pronombre" class="col-form-label fw-semibold">Pronombre:</label>
                <select class="form-select border border-dark-subtle" v-model.lazy="llamada.pronombre" aria-label="Default select example">
                    <option v-for="(value, key) in pronombres" :key="key" :value="value">
                        {{ value }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="grupo_conviviente" class="col-form-label fw-semibold">Grupo conviviente:</label>
                <select class="form-select border border-dark-subtle" v-model.lazy="llamada.grupo_conviviente" aria-label="Default select example">
                    <option v-for="(value, key) in grupos" :key="key" :value="value">
                        {{ value }}
                    </option>
                </select>
            </div>
            <div v-if="llamada.grupo_conviviente == 'Otro'" class="mb-3">
                <label for="grupo_conviviente_otro" class="col-form-label fw-semibold">Indique otro grupo conviviente:</label>
                <input v-model.lazy="llamada.grupo_conviviente_otro" type="text" id="grupo_conviviente_otro" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa otro grupo conviviente.
                </div>
            </div>
            <div class="mb-3">
                <label for="detalle_motivo_consulta" class="col-form-label fw-semibold">Detalle del motivo de la consulta:</label>
                <select class="form-select border border-dark-subtle" v-model.lazy="llamada.detalle_motivo_consulta" aria-label="Default select example">
                    <option v-for="detalle in detalle_motivos" :key="detalle.motivo" :value="detalle.motivo">
                        {{ detalle.motivo }}
                    </option>
                </select>
            </div>
            <fieldset v-if="llamada.detalle_motivo_consulta == 'Malestar emocional'" class="row mb-3">
                <legend class="col-form-label col-sm-2 pt-0 fw-semibold">Malestares emocionales</legend>
                <div v-for="malestar in malestares" :key="malestar" class="form-check ms-3">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="malestar.tipo"
                        :value="malestar.tipo"
                        @change="actualizarLista(llamada.malestares_emocionales, malestar.tipo)"
                    />
                    <label :for="malestar" class="form-check-label">{{ malestar.tipo }}</label>
                </div>    
            </fieldset>
            <div v-if="llamada.malestares_emocionales.includes('Otro')" class="mb-3">
                <label for="grupo_conviviente_otro" class="col-form-label fw-semibold">Indique otro malestar emocional:</label>
                <input v-model.lazy="llamada.malestares_emocionales_otro" type="text" id="grupo_conviviente_otro" class="form-control shadow-sm" required />
                <div class="invalid-feedback">
                    Por favor, ingresa otro malestar emocional.
                </div>
            </div>
            <fieldset class="row mb-3">
                <legend class="col-form-label fw-semibold">Situación de vulnerabilidad:</legend>
                <div v-for="situacion in situaciones" :key="situacion" class="form-check ms-3">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="situacion.tipo"
                        :value="situacion.tipo"
                        @change="actualizarLista(llamada.situaciones_vulnerabilidad, situacion.tipo)"
                    />
                    <label :for="situacion" class="form-check-label">{{ situacion.tipo }}</label>
                </div>    
            </fieldset>
            <div class="mb-3">
                <label for="definicion" class="col-form-label fw-semibold">Definición del llamado:</label>
                <select requiered class="form-select border border-dark-subtle" v-model.lazy="llamada.definicion" aria-label="Default select example">
                    <option v-for="(value, key) in definiciones" :key="key" :value="value">
                        {{ value }}
                    </option>
                </select>
            </div>
            <div v-if="llamada.definicion == 'Derivación a CETEC SM'">
                <div class="mb-3">
                    <label for="intervencion_sugerida" class="col-form-label fw-semibold">Intervención sugerida:</label>
                    <select requiered class="form-select border border-dark-subtle" v-model.lazy="llamada.intervencion_sugerida" aria-label="Default select example">
                        <option v-for="(value, key) in intervenciones" :key="key" :value="value">
                            {{ value }}
                        </option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="motivo_derivacion" class="col-form-label fw-semibold">Motivo general de la derivación:</label>
                    <select class="form-select border border-dark-subtle" v-model="llamada.motivo_derivacion" aria-label="Default select example">
                        <option v-for="motivo in motivos_grales_derivacion" :key="motivo" :value="motivo.tipo">
                            {{ motivo.tipo }}
                        </option>
                    </select>
                </div>
                <div v-if="llamada.motivo_derivacion == 'Otro'" class="mb-4">
                    <label for="otro_mot_gral_derivacion" class="col-form-label fw-semibold">Otro tipo de motivo general de derivación:</label>
                    <input v-model="llamada.motivo_derivacion_otro" type="text" id="otro_mot_gral_derivacion" class="form-control border border-dark-subtle" required />
                    <div class="invalid-feedback">
                        Por favor, ingrese otro tipo de motivo general de derivación.
                    </div>
                </div>
            </div>
            <div class="mb-3">
                <label for="nombre" class="col-form-label fw-semibold">Nombre:</label>
                <input v-model="llamada.nombre" type="text" id="nombre" class="form-control border border-dark-subtle"/>
                <div class="invalid-feedback">
                    Por favor, ingresa un el nombre de la persona derivada.
                </div>
            </div>
            <div class="mb-3">
                <label for="apellido" class="col-form-label fw-semibold">Apellido:</label>
                <input v-model="llamada.apellido" type="text" id="apellido" class="form-control border border-dark-subtle"/>
                <div class="invalid-feedback">
                    Por favor, ingresa el apellido de la persona derivada.
                </div>
            </div>
            <div class="mb-3">
                <label for="dni" class="col-form-label fw-semibold">DNI:</label>
                <input v-model="llamada.dni" type="text" id="dni" pattern="[0-9]{7,8}" title="Ingrese el número de DNI sin puntos ('Ej: 42456789')" class="form-control border border-dark-subtle" />
                <div class="invalid-feedback">
                    El DNI debe ingresarse sin puntos y contener entre 7 y 8 dígitos.
                </div>
            </div>
            <!-- <div v-if="!existeDato.localidad" class="mb-3">
                <label for="localidad" class="col-form-label fw-semibold">Localidad:</label>
                <input v-model.lazy="persona.localidad" type="text" id="localidad" class="form-control shadow-sm" />
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
                motivo_consulta: '',
                como_ubico: '',
                municipio: '',
                sujeto: '',
                edad: '',
                identidad_genero: '',
                identidad_genero_otra: '',
                pronombre: '',
                grupo_conviviente:'',
                grupo_conviviente_otro:'',
                detalle_motivo_consulta: '',
                malestares_emocionales: [],
                malestares_emocionales_otro: '',
                situaciones_vulnerabilidad: [],
                definicion: '',
                intervencion_sugerida: '',
                motivo_derivacion: '',
                motivo_derivacion_otro: '',
                nombre: '',
                apellido: '',
                dni: '',
            },

            motivos: [],
            formas_ubico: [],
            municipios: [],
            sujetos: [],
            generos: [],
            pronombres: [],
            grupos: [],
            detalle_motivos: [],
            malestares: [],
            situaciones: [],
            definiciones: [],
            intervenciones: [],
            motivos_grales_derivacion: [],
            errores: [],
        }
    },

    async created() {
        
        await apiService.get(import.meta.env.VITE_API_URL + "motivos_consulta")
            .then((response) => {
                this.motivos = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "como_ubico")
            .then((response) => {
                this.formas_ubico = response.data;
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
        
        await apiService.get(import.meta.env.VITE_API_URL + "sujetos_consulta")
            .then((response) => {
                this.sujetos = response.data;
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

        await apiService.get(import.meta.env.VITE_API_URL + "pronombres")
            .then((response) => {
                this.pronombres = response.data;
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
        
        await apiService.get(import.meta.env.VITE_API_URL + "detalle_motivos_consulta")
            .then((response) => {
                this.detalle_motivos = response.data;
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

        await apiService.get(import.meta.env.VITE_API_URL + "definiciones_llamada_0800")
            .then((response) => {
                this.definiciones = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

        await apiService.get(import.meta.env.VITE_API_URL + "intervenciones_sugeridas")
            .then((response) => {
                this.intervenciones = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
            
        await apiService.get(import.meta.env.VITE_API_URL + "mot_grales_derivacion")
            .then((response) => {
                this.motivos_grales_derivacion = response.data;
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
            return lista.some((l) => l == elemento)
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