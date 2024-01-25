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
    mujer = identidad_genero.create(tipo="Mujer")
    varon = identidad_genero.create(tipo="Varón")
    mujer_trans = identidad_genero.create(tipo="Mujer trans")
    varon_trans = identidad_genero.create(tipo="Varón trans")
    no_binarie = identidad_genero.create(tipo="No binarie")
    otra_identidad = identidad_genero.create(tipo="Otra identidad")
    ns_nc = identidad_genero.create(tipo="NS/NC")


    # Carga de tabla motivo general de acompañamiento
    malestar_emocional_acomp = motivo_general_acompanamiento.create(tipo="Malestar emocional")
    orientacion_acomp = motivo_general_acompanamiento.create(tipo="Orientación y asesoramiento")
    acceso = motivo_general_acompanamiento.create(tipo="Acceso a atención en Salud Mental")

    # Carga de tabla malestar emocional
    angustia = malestar_emocional.create(tipo="Angustia/Ansiedad")
    temor = malestar_emocional.create(tipo="Temor/Miedo")
    soledad = malestar_emocional.create(tipo="Sentimiento de soledad")
    duelo = malestar_emocional.create(tipo="Duelo")
    insomnio = malestar_emocional.create(tipo="Dificultades para dormir - insomnio")
    ideacion_suicida = malestar_emocional.create(tipo="Ideación suicida")
    intento_suicidio = malestar_emocional.create(tipo="Intento de suicidio")
    alucinaciones = malestar_emocional.create(tipo="Presentación de delirios - alucinaciones")
    trastorno_alimentacion = malestar_emocional.create(tipo="Trastornos de la alimentación")
    violencias = malestar_emocional.create(tipo="Violencias")
    consumos_problematicos = malestar_emocional.create(tipo="Consumos problemáticos")
    otro_malestar_emocional = malestar_emocional.create(tipo="Otro")

    # Carga de tabla de situaciones de vulnerabilidad
    fallecimiento = situaciones_vulnerabilidad.create(tipo="Fallecimiento de vinculo significativo")
    situacion_calle = situaciones_vulnerabilidad.create(tipo="Situación de calle")
    violencia_genero = situaciones_vulnerabilidad.create(tipo="Violencia de género")
    violencia_intrafamiliar = situaciones_vulnerabilidad.create(tipo="Violencia intrafamiliar")
    violencia_institucional = situaciones_vulnerabilidad.create(tipo="Violencia institucional")
    violencia_laboral = situaciones_vulnerabilidad.create(tipo="Violencia laboral")
    dificultad_acceso_salud = situaciones_vulnerabilidad.create(tipo="Dificultades para el acceso al sistema de salud")
    dificultad_acceso_alimento = situaciones_vulnerabilidad.create(tipo="Dificultad para el acceso al alimento")
    dificultad_acceso_medicacion_sm = situaciones_vulnerabilidad.create(tipo="Dificultad para el acceso a medicación - SM")
    dificultad_acceso_medicacion = situaciones_vulnerabilidad.create(tipo="Dificultad para el acceso a medicación - otra (no SM)")
    pedido_certificado = situaciones_vulnerabilidad.create(tipo="Pedido certificado CUD")
    otra_situacion_vulnerabilidad = situaciones_vulnerabilidad.create(tipo="Otro")
    ninguna_sit_vuln = situaciones_vulnerabilidad.create(tipo="Ninguna situación de vulnerabilidad")


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
        identidad_genero = varon,
        municipio = municipio_1
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
        identidad_genero = mujer,
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
        identidad_genero = varon,
        municipio = municipio_11
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


    persona_cetecsm_1.situaciones_vulnerabilidad.append(dificultad_acceso_salud)
    persona_cetecsm_1.situaciones_vulnerabilidad.append(pedido_certificado)
    persona_cetecsm.update_persona_cetecsm(
        id=llamada_cetecsm_1.persona_cetecsm_id,
        fecha_prox_llamado_actual=llamada_cetecsm_1.fecha_prox_llamado,
        detalle_acompanamiento = "En la primer llamada hablamos bastante."        
    )

    llamada_cetecsm_2 = llamada_cetecsm.create_llamada_cetecsm(
        detalle = "Segunda llamada",
        resolucion = ResolucionLlamado.RESOLUCION.value,
        usuario_carga = user_operator_cetecsm,
        persona_cetecsm_llamada = persona_cetecsm_1,
    )

    persona_cetecsm.update_persona_cetecsm(
        id=llamada_cetecsm_1.persona_cetecsm_id,
        fecha_prox_llamado_actual=llamada_cetecsm_2.fecha_prox_llamado,
        detalle_acompanamiento = "En la primer llamada hablamos bastante. En la segunda llamada hablamos menos.",
        motivo_gral_acomp = orientacion_acomp
    )


    llamada_cetecsm_3 = llamada_cetecsm.create_llamada_cetecsm(
        detalle = "Primer llamada a persona 3",
        resolucion = ResolucionLlamado.CONTINUA.value,
        fecha_prox_llamado = datetime(2024, 1, 17),
        usuario_carga = user_operator_cetecsm,
        persona_cetecsm_llamada = persona_cetecsm_3
    )

    persona_cetecsm_3.situaciones_vulnerabilidad.append(dificultad_acceso_medicacion)
    persona_cetecsm.update_persona_cetecsm(
        id=llamada_cetecsm_3.persona_cetecsm_id, 
        fecha_prox_llamado_actual=llamada_cetecsm_3.fecha_prox_llamado,
        detalle_acompanamiento = "Llamado por primera vez a la persona y me brindo todos los datos",
        motivo_gral_acomp = acceso,
    )

    # Cargas del 0800

    # Carga de tabla de motivo de consulta
    llamada_0800.create_motivo_consulta("Asistencia en Salud Mental")
    llamada_0800.create_motivo_consulta("Orientación en Salud Mental")
    llamada_0800.create_motivo_consulta("Otros")

    # Carga la tabla de cómo el paciente puede haber ubicado al 0800
    llamada_0800.create_como_ubico("Búsqueda en Internet")
    llamada_0800.create_como_ubico("Redes sociales")
    llamada_0800.create_como_ubico("Material gráfico")
    llamada_0800.create_como_ubico("Por conocidos")
    llamada_0800.create_como_ubico("Derivación de un profesional")
    llamada_0800.create_como_ubico("Usuario habitual")
    llamada_0800.create_como_ubico("Medios de comunicación")
    llamada_0800.create_como_ubico("Otros")

    # Carga la tabla de detalles de motivo de la consulta
    llamada_0800.create_detalle_motivo_consulta("Consumo Problemático")
    llamada_0800.create_detalle_motivo_consulta("Violencia de Género")
    llamada_0800.create_detalle_motivo_consulta("Otras violencias")
    llamada_0800.create_detalle_motivo_consulta("Malestar emocional")

    print("Seeds cargados!")