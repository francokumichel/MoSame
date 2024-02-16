<template>
        <h2 class="fw-bold mb-4">Editar opciones</h2>
        <form ref="formulario" class="px-5 needs-validation" @submit.prevent="guardarOpciones" novalidate>
            <div class="mb-3">
                <label for="opciones" class="col-form-label fw-semibold">Seleccione las opciones a editar:</label>
                <select required class="form-select border border-dark-subtle" v-model.lazy="opcion" @change="getOpciones()">
                    <option value="motivos_consulta">Motivos de la consulta</option>
                    <option value="como_ubico">Medios por el cual se ubicó al 0800</option>
                    <option value="generos">Identidades de género</option>
                    <option value="detalles_motivo_consulta">Detalles del motivo de la consulta</option>
                    <option value="malestares_emocionales">Tipos de malestar emocional</option>
                    <option value="situaciones_vulnerabilidad">Tipos de situación de vulnerabilidad</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="opciones" class="col-form-label fw-semibold">Opciones:</label>
                <div v-for="(opcion, index) in opciones" :key="index" class="d-flex">
                    <input required class="form-control border border-dark-subtle mb-2" maxlength="100" type="text" :value="opcion" @input.prevent="updateOpcion(index, $event.target.value)" placeholder="Opción nueva" />
                    <button class="btn btn-secondary ms-2 mb-2" @click.prevent="removeOpcion(index)" v-if="opciones.length > 1">-</button>
                    <button class="btn btn-primary ms-2 mb-2" @click.prevent="addOpcion(index)" v-if="index === opciones.length - 1">+</button>
                </div>
            </div>
            <div class="d-flex justify-content-center">
                <button type="submit" class="btn btn-info text-white fw-semibold shadow-sm">Guardar</button>
            </div>
        </form>
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
    data() {
        return {
            opciones: [],
            errores: [],
            opcion: "motivos_consulta"
        }
    },

    async created() {

        this.getOpciones();
        
    },

    methods: {

        async getOpciones() {
            await apiService.get(import.meta.env.VITE_API_URL + "admin/opciones/" + `${this.opcion}`)
            .then((response) => {
                this.opciones = response.data;
                console.log(response.data)
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        },

        async guardarOpciones() {
            const form = this.$refs.formulario;

        // Verificar si alguna opción está vacía
        if (this.opciones.some(opcion => opcion.trim() === '')) {
            displayError(this.$toast, 'No se pueden dejar opciones vacías.');
            return;
        }

            if (form.checkValidity()) {
                try {
                    const opciones_str = JSON.stringify(this.opciones);
                                        
                    await apiService.post(import.meta.env.VITE_API_URL + "admin/guardar-opciones",
                        {
                            opcion: this.opcion,
                            opciones: opciones_str,
                        })
                    .then((response) => {
                        if(response.status == 200) {
                            displaySuccess(this.$toast, "Se guardaron los cambios");
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

        
        addOpcion(index) {
            console.log(index)
            if (this.opciones[index].trim() !== '') {
                this.opciones.push('');
            }
        },

        removeOpcion(index) {
            if (this.opciones.length > 1) {
                this.opciones.splice(index, 1);
            }
        },

        updateOpcion(index, value) {
            this.opciones[index] = value;
        },
    }
}
</script>