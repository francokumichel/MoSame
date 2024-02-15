<template>
  <div ref="mapa"></div>
</template>
  
<script>
import { apiService } from '@/services/api';
import * as d3 from 'd3';
import d3Tip from 'd3-tip';

export default {
  data() {
    return {
      geojson: null,
      dataReady: false,
    }
  },

  async created() {
    await apiService.get("municipios_geojson")
      .then((response) => {
          this.geojson = response.data;
          this.dataReady = true;
      })
      .catch((e) => {
          console.log(e)
          this.errores.push(e);
      });
  },

  watch: {
    dataReady: function(newVal) {
        if (newVal) {
            this.initializeMap();
        }
    }
  },

  methods: {
    initializeMap() {
      // Configurar dimensiones del mapa
      const width = 1200;
      const height = 800;

      // Crear lienzo SVG
      const mapa = this.$refs.mapa;
      const svg = d3.select(mapa)
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      // Configurar proyección y ruta
      const projection = d3.geoMercator().fitSize([width, height], this.geojson);
      const path = d3.geoPath().projection(projection);

      const Tooltip = d3.select(mapa)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "2px")
        .style("border-radius", "5px")
        .style("padding", "5px")
        .style("margin", "20px")
        .style("width", "600px")


        var mouseover = function(d) {
          Tooltip
            .style("opacity", 1)
          d3.select(this)
            .style("stroke", "black")
            .style("opacity", 1)
        }
        var mousemove = function(event, d) {
          var tooltipContent = "Municipio: " + d.properties.nombre;
          console.log(tooltipContent)
          Tooltip
            .html(tooltipContent)
            .style("left", (event.pageX - mapa.getBoundingClientRect().left + 10) + "px")
            .style("top", (event.pageY - mapa.getBoundingClientRect().top + 10) + "px")
        }
        var mouseout = function(d) {
          Tooltip
            .style("opacity", 0)
          d3.select(this)
            .style("stroke", "black")
            .style("opacity", 0.8)
        }
        
        var zoomed = function(event, d) {
          svg.selectAll('path')
            .attr('transform', event.transform);  // Aplicar la transformación de zoom a los elementos del mapa
        }

        const zoom = d3.zoom()
          .scaleExtent([1, 8])  // Establecer el rango de escala permitido
          .on("zoom", zoomed);

        svg.call(zoom);

      // Dibujar límites de municipios
      svg.selectAll('path')
        .data(this.geojson.features)
        .enter().append('path')
        .attr('d', path)
        .attr('stroke', 'black')
        .attr('stroke-width', 0.5)
        .attr('fill', '#FFFFFF')
        .on('mouseover', mouseover)
        .on("mousemove", mousemove)
        .on('mouseout', mouseout);
    }
  }
  
};
</script>

<style>

.d3-tip {
  line-height: 1;
  font-weight: bold;
  padding: 10px;
  background: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 4px;
  pointer-events: none;
}
</style>