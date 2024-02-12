<template>
        <h2 class="fw-bold mb-4">Registrar llamada</h2>
        <form ref="formulario" class="px-5 needs-validation" @submit.prevent="registrarLlamada" novalidate>
            <div class="mb-3">
                <label for="opciones" class="col-form-label fw-semibold">Opciones:</label>
                <div v-for="(opcion, index) in opciones" :key="index" class="d-flex">
                    <input required class="form-control border border-dark-subtle mb-2" type="text" :value="opcion" @input.prevent="updateOpcion(index, $event.target.value)" placeholder="Opción nueva" />
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
        }
    },

    async created() {

        await apiService.get(import.meta.env.VITE_API_URL + "admin/opciones")
            .then((response) => {
                this.opciones = response.data;
                console.log(response.data)
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
    },

    methods: {
        async registrarLlamada() {
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