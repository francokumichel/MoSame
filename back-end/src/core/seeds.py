from datetime import datetime
from src.core import prueba
from src.core import users
from src.core import permissions
from src.core import motivo_general_derivacion
from src.core import identidad_genero
from src.core import motivo_general_acompanamiento
from src.core import malestar_emocional
from src.core import situaciones_vulnerabilidad
from src.core import persona_cetecsm
from src.core.persona_cetecsm.persona_cetecsm import GrupoConviviente
from src.core import derivacion
from src.core import llamada_cetecsm
from src.core.llamada_cetecsm.llamada_cetecsm import ResolucionLlamado
from src.core import llamada_0800

def run():

    datos_prueba = prueba.create_prueba(
        name="Por favor funciona :)"
    )

    # Permisos acceder a funcionalidades del usuario
    user_index = permissions.create_permission(name="user_index")
    user_new = permissions.create_permission(name="user_new")
    user_destroy = permissions.create_permission(name="user_destroy")
    user_update = permissions.create_permission(name="user_update")
    user_show = permissions.create_permission(name="user_show")
    
    role_admin = permissions.create_role(name="Administrador")

    role_admin.permissions.append(user_index)
    role_admin.permissions.append(user_new)
    role_admin.permissions.append(user_destroy)
    role_admin.permissions.append(user_update)
    role_admin.permissions.append(user_show)

    # Permisos para acceder a permisos a funcionalidades relacionadas a modulo 0800
    call_0800_index = permissions.create_permission(name="call_0800_index")
    call_0800_new = permissions.create_permission(name="call_0800_new")
    call_0800_show = permissions.create_permission(name="call_0800_show")

    role_operator_0800 = permissions.create_role(name="Operador 0800")
    
    role_operator_0800.permissions.append(call_0800_index)
    role_operator_0800.permissions.append(call_0800_new)
    role_operator_0800.permissions.append(call_0800_show)

    # Permisos para acceder a permisos a funcionalidades relacionadas a módulo CETECSM
    # Permisos operador CETECSM
    derivation_index = permissions.create_permission(name="derivation_index")
    derivation_new = permissions.create_permission(name="derivation_new")
    derivation_update = permissions.create_permission(name="derivation_update")
    derivation_show = permissions.create_permission(name="derivation_show")
    call_cetecsm_index = permissions.create_permission(name="call_cetecsm_index")
    call_cetecsm_new = permissions.create_permission(name="call_cetecsm_new")

    # Permisos coordinador CETECSM
    operator_cetecsm_index = permissions.create_permission(name="operator_cetecsm_index")

    role_operator_cetecsm = permissions.create_role(name="Operador CETECSM")
    role_operator_cetecsm.permissions.append(derivation_index)
    role_operator_cetecsm.permissions.append(derivation_new)
    role_operator_cetecsm.permissions.append(derivation_update)
    role_operator_cetecsm.permissions.append(derivation_show)
    role_operator_cetecsm.permissions.append(call_cetecsm_index)
    role_operator_cetecsm.permissions.append(call_cetecsm_new)

    role_coordinator_cetecsm = permissions.create_role(name="Coordinador CETECSM")
    role_coordinator_cetecsm.permissions.append(derivation_index)
    role_coordinator_cetecsm.permissions.append(derivation_show)
    role_coordinator_cetecsm.permissions.append(call_cetecsm_index)
    role_coordinator_cetecsm.permissions.append(call_cetecsm_new)
    role_coordinator_cetecsm.permissions.append(operator_cetecsm_index)

    # Permisos observatorio
    role_observatorio = permissions.create_role(name="Miembro observatorio")

    llamadas_0800_index = permissions.create_permission(name="llamadas_0800_index")
    llamadas_0800_export = permissions.create_permission(name="llamadas_0800_export")
    personas_cetecsm_asignadas_index = permissions.create_permission(name="personas_cetecsm_asignadas_index")
    personas_cetecsm_derivadas_export = permissions.create_permission(name="personas_cetecsm_derivadas_export")
    personas_cetecsm_seguimiento_index = permissions.create_permission(name="personas_cetecsm_seguimiento_index")
    personas_cetecsm_seguimiento_export = permissions.create_permission(name="personas_cetecsm_seguimiento_export")
    cantidad_total_llamadas_show = permissions.create_permission(name="cantidad_total_llamadas_show")
    talleres_salud_escuelas_index = permissions.create_permission(name="talleres_salud_escuelas_index")
    talleres_salud_escuelas_export = permissions.create_permission(name="talleres_salud_escuelas_export")

    role_observatorio.permissions.append(llamadas_0800_index)
    role_observatorio.permissions.append(llamadas_0800_export)
    role_observatorio.permissions.append(personas_cetecsm_asignadas_index)
    role_observatorio.permissions.append(personas_cetecsm_derivadas_export)
    role_observatorio.permissions.append(personas_cetecsm_seguimiento_index)
    role_observatorio.permissions.append(personas_cetecsm_seguimiento_export)
    role_observatorio.permissions.append(cantidad_total_llamadas_show)
    role_observatorio.permissions.append(talleres_salud_escuelas_index)
    role_observatorio.permissions.append(talleres_salud_escuelas_export)
    


    user_admin = users.create_user(
        name="Admin",
        last_name="Admin",
        email="admin@gmail.com",
        password="1234"
    )
    users.update_roles(user_admin, [role_admin])

    user_operator_0800 = users.create_user(
        name="Operador 0800",
        last_name="Operador 0800",
        email="Operador0800@gmail.com",
        password="1234"
    )

    users.update_roles(user_operator_0800, [role_operator_0800])

    user_operator_cetecsm = users.create_user(
        name="Operador CETECSM",
        last_name="Operador CETECSM",
        email="OperadorCETECSM@gmail.com",
        password="1234"
    )

    users.update_roles(user_operator_cetecsm, [role_operator_cetecsm])
    
    user_coordinator_cetecsm = users.create_user(
        name="Coordinador CETECSM",
        last_name="Coordinador CETECSM",
        email="CoordinadorCETECSM@gmail.com",
        password="1234"
    )

    users.update_roles(user_coordinator_cetecsm, [role_coordinator_cetecsm])

    user_observatorio = users.create_user(
        name="Observatorio",
        last_name="Observatorio",
        email="Observatorio@gmail.com",
        password="1234"
    )

    users.update_roles(user_observatorio, [role_observatorio])

    # Carga de datos correspondientes a módulo cetecsm

    # Carga de tabla de region sanitaria
    region_1 = persona_cetecsm.create_region_sanitaria(tipo="I")
    region_2 = persona_cetecsm.create_region_sanitaria(tipo="II")
    region_3 = persona_cetecsm.create_region_sanitaria(tipo="III")
    region_4 = persona_cetecsm.create_region_sanitaria(tipo="IV")
    region_5 = persona_cetecsm.create_region_sanitaria(tipo="V")
    region_6 = persona_cetecsm.create_region_sanitaria(tipo="VI")
    region_7 = persona_cetecsm.create_region_sanitaria(tipo="VII")
    region_8 = persona_cetecsm.create_region_sanitaria(tipo="VIII")
    region_9 = persona_cetecsm.create_region_sanitaria(tipo="IX")
    region_10 = persona_cetecsm.create_region_sanitaria(tipo="X")
    region_11 = persona_cetecsm.create_region_sanitaria(tipo="XI")
    region_12 = persona_cetecsm.create_region_sanitaria(tipo="XII")

    # Carga de tabla de municipios (solo algunos para pruebas)
    municipio_1 = persona_cetecsm.create_municipio(nombre="Bahía Blanca", region_sanitaria=region_1)
    municipio_2 = persona_cetecsm.create_municipio(nombre="Daireaux", region_sanitaria=region_2)
    municipio_3 = persona_cetecsm.create_municipio(nombre="Junín", region_sanitaria=region_3)
    municipio_4 = persona_cetecsm.create_municipio(nombre="Pergamino", region_sanitaria=region_4)
    municipio_5 = persona_cetecsm.create_municipio(nombre="Tigre", region_sanitaria=region_5)
    municipio_6 = persona_cetecsm.create_municipio(nombre="Berazategui", region_sanitaria=region_6)
    municipio_7 = persona_cetecsm.create_municipio(nombre="General Rodríguez", region_sanitaria=region_7)
    municipio_8 = persona_cetecsm.create_municipio(nombre="Partido de La Costa", region_sanitaria=region_8)
    municipio_9 = persona_cetecsm.create_municipio(nombre="Azul", region_sanitaria=region_9)
    municipio_10 = persona_cetecsm.create_municipio(nombre="Mercedes", region_sanitaria=region_10)
    municipio_11 = persona_cetecsm.create_municipio(nombre="La Plata", region_sanitaria=region_11)
    municipio_12 = persona_cetecsm.create_municipio(nombre="La Matanza", region_sanitaria=region_12)

    # Carga de tabla de motivo general de derivación
    malestar_emocional_der = motivo_general_derivacion.create_motivo_gral_der(tipo="Malestar emocional")
    consumo_problematico = motivo_general_derivacion.create_motivo_gral_der(tipo="Consumo problematico")
    orientacion_deriv = motivo_general_derivacion.create_motivo_gral_der(tipo="Orientación/asesoramiento en Salud Mental")
    acceso_asistencia = motivo_general_derivacion.create_motivo_gral_der(tipo="Acceso a asistencia en Salud Mental")
    acceso_medicacion = motivo_general_derivacion.create_motivo_gral_der(tipo="Acceso a medicación")
    violencia_gnro = motivo_general_derivacion.create_motivo_gral_der(tipo="Violencia de género")
    otras_violencias = motivo_general_derivacion.create_motivo_gral_der(tipo="Otras violencias")
    otro_mot_gral_derivacion = motivo_general_derivacion.create_motivo_gral_der(tipo="Otro")

    # Carga de tabla de identidad de genero
    mujer = identidad_genero.create_identidad_genero(tipo="Mujer")
    varon = identidad_genero.create_identidad_genero(tipo="Varón")
    mujer_trans = identidad_genero.create_identidad_genero(tipo="Mujer trans")
    varon_trans = identidad_genero.create_identidad_genero(tipo="Varón trans")
    no_binarie = identidad_genero.create_identidad_genero(tipo="No binarie")
    otra_identidad = identidad_genero.create_identidad_genero(tipo="Otra identidad")
    ns_nc = identidad_genero.create_identidad_genero(tipo="NS/NC")


    # Carga de tabla motivo general de acompañamiento
    malestar_emocional_acomp = motivo_general_acompanamiento.create_mot_gral_acomp(tipo="Malestar emocional")
    orientacion_acomp = motivo_general_acompanamiento.create_mot_gral_acomp(tipo="Orientación y asesoramiento")
    acceso = motivo_general_acompanamiento.create_mot_gral_acomp(tipo="Acceso a atención en Salud Mental")

    # Carga de tabla malestar emocional
    angustia = malestar_emocional.create_malestar_emocional(tipo="Angustia/Ansiedad")
    temor = malestar_emocional.create_malestar_emocional(tipo="Temor/Miedo")
    soledad = malestar_emocional.create_malestar_emocional(tipo="Sentimiento de soledad")
    duelo = malestar_emocional.create_malestar_emocional(tipo="Duelo")
    insomnio = malestar_emocional.create_malestar_emocional(tipo="Dificultades para dormir - insomnio")
    ideacion_suicida = malestar_emocional.create_malestar_emocional(tipo="Ideación suicida")
    intento_suicidio = malestar_emocional.create_malestar_emocional(tipo="Intento de suicidio")
    alucinaciones = malestar_emocional.create_malestar_emocional(tipo="Presentación de delirios - alucinaciones")
    trastorno_alimentacion = malestar_emocional.create_malestar_emocional(tipo="Trastornos de la alimentación")
    violencias = malestar_emocional.create_malestar_emocional(tipo="Violencias")
    consumos_problematicos = malestar_emocional.create_malestar_emocional(tipo="Consumos problemáticos")
    otro_malestar_emocional = malestar_emocional.create_malestar_emocional(tipo="Otro")

    # Carga de tabla de situaciones de vulnerabilidad
    fallecimiento = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Fallecimiento de vinculo significativo")
    situacion_calle = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Situación de calle")
    violencia_genero = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Violencia de género")
    violencia_intrafamiliar = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Violencia intrafamiliar")
    violencia_institucional = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Violencia institucional")
    violencia_laboral = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Violencia laboral")
    dificultad_acceso_salud = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Dificultades para el acceso al sistema de salud")
    dificultad_acceso_alimento = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Dificultad para el acceso al alimento")
    dificultad_acceso_medicacion_sm = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Dificultad para el acceso a medicación - SM")
    dificultad_acceso_medicacion = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Dificultad para el acceso a medicación - otra (no SM)")
    pedido_certificado = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Pedido certificado CUD")
    otra_situacion_vulnerabilidad = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Otro")
    ninguna_sit_vuln = situaciones_vulnerabilidad.create_situacion_vulnerabilidad(tipo="Ninguna situación de vulnerabilidad")


    # Carga de tabla de personas_cetecsm
    persona_cetecsm_1 = persona_cetecsm.create_persona_cetecsm(
        dni = "35123456",
        grupo_conviviente = GrupoConviviente.AM.value,
        dio_consentimiento = True,
        localidad = "Berazategui",
        tiene_obra_social = False,
        nombre = "Roberto",
        apellido = "Fernandez",
        edad = 30,
        telefono = "1122334455",
        identidad_genero_id = "Varón",
        municipio = municipio_1,
        situaciones_vulnerabilidad = '["Dificultades para el acceso al sistema de salud","Pedido certificado CUD"]'
    )

    persona_cetecsm_2 = persona_cetecsm.create_persona_cetecsm(
        dni = "40345678",
        grupo_conviviente = GrupoConviviente.A.value,
        dio_consentimiento = True,
        localidad = "Hudson",
        tiene_obra_social = True,
        obra_social = "OSDE",
        nombre = "Florencia",
        apellido = "Gomez",
        edad = 25,
        telefono = "221345678",
        identidad_genero_id = "Mujer",
        municipio = municipio_6
    )

    persona_cetecsm_3 = persona_cetecsm.create_persona_cetecsm(
        dni = "42444555",
        grupo_conviviente = GrupoConviviente.O.value,
        grupo_conviviente_otro = "Familia",
        dio_consentimiento = True,
        localidad = "El Pato",
        tiene_obra_social = False,
        nombre = "Eduardo",
        apellido = "Sanchez",
        edad = 26,
        telefono = "1144556677",
        identidad_genero_id = "Varón",
        municipio = municipio_11,
        situaciones_vulnerabilidad = '["Dificultad para el acceso a medicación - SM"]'
    )
    
    derivacion_1 = derivacion.create_derivation(
        dispositivo_derivacion = "Dispositivo 1",
        nombre_operador_derivador = "Carlos",
        descripcion = "Soy la primer derivación de todas",
        mot_gral_derivacion = orientacion_deriv,
        persona_cetecsm_derivada = persona_cetecsm_1
    )

    derivacion_2 = derivacion.create_derivation(
        fecha = datetime(2024, 1, 6),
        dispositivo_derivacion = "Dispositivo 2",
        nombre_operador_derivador = "Alicia",
        descripcion = "Soy la segunda derivación",
        mot_gral_derivacion = malestar_emocional_der,
        persona_cetecsm_derivada = persona_cetecsm_2
    )

    derivacion_3 = derivacion.create_derivation(
        dispositivo_derivacion = "Dispositivo 3",
        nombre_operador_derivador = "Santiago",
        descripcion = "Soy la tercer derivación",
        mot_gral_derivacion = acceso_medicacion,
        persona_cetecsm_derivada = persona_cetecsm_3
    )
    
    users.asignar_persona(user_operator_cetecsm, persona_cetecsm_1)
    persona_cetecsm_1.update(esta_asignada=True)
    users.asignar_persona(user_operator_cetecsm, persona_cetecsm_3)
    persona_cetecsm_3.update(esta_asignada=True)

    llamada_cetecsm_1 = llamada_cetecsm.create_llamada_cetecsm(
        detalle = "Primer llamada",
        resolucion = ResolucionLlamado.CONTINUA.value,
        fecha_llamado = datetime(2024, 1, 3),
        fecha_prox_llamado = datetime(2024, 1, 9),
        usuario_carga = user_operator_cetecsm,
        persona_cetecsm_llamada = persona_cetecsm_1,
    )


    persona_cetecsm.update_persona_cetecsm(
        id=llamada_cetecsm_1.persona_cetecsm_id,
        fecha_prox_llamado_actual=llamada_cetecsm_1.fecha_prox_llamado,
        detalle_acompanamiento = "En la primer llamada hablamos bastante."        
    )

    llamada_cetecsm_2 = llamada_cetecsm.create_llamada_cetecsm(
        detalle = "Segunda llamada",
        resolucion = ResolucionLlamado.RESOLUCION.value,
        fecha_llamado = datetime(2024, 1, 9),
        usuario_carga = user_operator_cetecsm,
        persona_cetecsm_llamada = persona_cetecsm_1,
    )

    persona_cetecsm.update_persona_cetecsm(
        id=llamada_cetecsm_1.persona_cetecsm_id,
        fecha_prox_llamado_actual=llamada_cetecsm_2.fecha_prox_llamado,
        detalle_acompanamiento = "En la primer llamada hablamos bastante. En la segunda llamada hablamos menos.",
        motivo_gral_acomp = "Orientación y asesoramiento"
    )


    llamada_cetecsm_3 = llamada_cetecsm.create_llamada_cetecsm(
        detalle = "Primer llamada a persona 3",
        resolucion = ResolucionLlamado.CONTINUA.value,
        fecha_llamado = datetime(2024, 1, 10),
        fecha_prox_llamado = datetime(2024, 1, 17),
        usuario_carga = user_operator_cetecsm,
        persona_cetecsm_llamada = persona_cetecsm_3
    )

    persona_cetecsm.update_persona_cetecsm(
        id=llamada_cetecsm_3.persona_cetecsm_id, 
        fecha_prox_llamado_actual=llamada_cetecsm_3.fecha_prox_llamado,
        detalle_acompanamiento = "Llamado por primera vez a la persona y me brindo todos los datos",
        motivo_gral_acomp = "Acceso a atención en Salud Mental",
    )

    # Cargas del 0800

    # Carga de tabla de motivo de consulta
    llamada_0800.create_motivo_consulta(nombre="Asistencia en Salud Mental")
    llamada_0800.create_motivo_consulta(nombre="Orientación en Salud Mental")
    llamada_0800.create_motivo_consulta(nombre="Otros")

    # Carga la tabla de cómo el paciente puede haber ubicado al 0800
    llamada_0800.create_como_ubico(forma="Búsqueda en Internet")
    llamada_0800.create_como_ubico(forma="Redes sociales")
    llamada_0800.create_como_ubico(forma="Material gráfico")
    llamada_0800.create_como_ubico(forma="Por conocidos")
    llamada_0800.create_como_ubico(forma="Derivación de un profesional")
    llamada_0800.create_como_ubico(forma="Usuario habitual")
    llamada_0800.create_como_ubico(forma="Medios de comunicación")
    llamada_0800.create_como_ubico(forma="Otros")

    # Carga la tabla de detalles de motivo de la consulta
    llamada_0800.create_detalle_motivo_consulta(motivo="Consumo Problemático")
    llamada_0800.create_detalle_motivo_consulta(motivo="Violencia de Género")
    llamada_0800.create_detalle_motivo_consulta(motivo="Otras violencias")
    llamada_0800.create_detalle_motivo_consulta(motivo="Malestar emocional")

    # Carga una llamada de prueba
    llamada_0800.create_llamada_0800(
        motivo_nombre = 'Asistencia en Salud Mental',
        como_ubico_forma = 'Búsqueda en Internet',
        como_ubico_otro = '',
        municipio_nombre = 'Azul',
        sujeto = 'Propia',
        edad = '18',
        identidad_genero_tipo = 'Mujer',
        identidad_genero_otra = '',
        pronombre = 'Ella',
        grupo_conviviente = 'Solo',
        grupo_conviviente_otro = '',
        detalle_motivo_motivo = 'Consumo Problemático',
        malestares_emocionales = '',
        malestares_emocionales_otro = '',
        situaciones_vulnerabilidad = '',
        definicion = 'Intervención finalizada',
        persona_cetecsm_id = '',
        intervencion_sugerida = '',
        motivo_derivacion = '',
        motivo_derivacion_otro = '',
        nombre = 'Anabella',
        apellido = 'Grugs',
        dni = '12345678',
        telefonos = '',
        emails = '',
        domicilio = 'En algún lugar',
        nacionalidad = 'Argentina',
        nacimiento = '',
        detalle_intervencion = 'Hablamos',
        duracion = 'Como 20 mins',
        demanda_tratamiento = True,
        email_operador = 'Operador0800@gmail.com'
    )

    print("Seeds cargados!")