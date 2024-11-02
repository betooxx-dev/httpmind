HTTP_CODES = {
    "100": {
        "title": "Continue",
        "type": "Informativo",
        "description": "El servidor ha recibido los headers de la solicitud y el cliente debería proceder a enviar el cuerpo de la misma.",
        "solutions": [
            "Verificar si el cuerpo de la solicitud se está enviando correctamente",
            "Comprobar si el encabezado Expect se está utilizando adecuadamente"
        ],
        "severity": "baja"
    },
    "101": {
        "title": "Switching Protocols",
        "type": "Informativo",
        "description": "El servidor acepta el cambio de protocolo propuesto por el cliente mediante el encabezado Upgrade.",
        "solutions": [
            "Verificar que el nuevo protocolo sea compatible",
            "Asegurar que la negociación de protocolos sea correcta"
        ],
        "severity": "baja"
    },
    "102": {
        "title": "Processing",
        "type": "Informativo",
        "description": "El servidor está procesando la solicitud pero aún no ha completado la respuesta.",
        "solutions": [
            "Esperar a que el servidor complete el procesamiento",
            "Implementar un mecanismo de timeout apropiado",
            "Considerar la implementación de un sistema de notificación asíncrono"
        ],
        "severity": "baja"
    },
    "103": {
        "title": "Early Hints",
        "type": "Informativo",
        "description": "Indica al cliente que puede comenzar a precargar recursos mientras el servidor prepara una respuesta.",
        "solutions": [
            "Implementar precarga de recursos críticos",
            "Optimizar el uso del encabezado Link",
            "Evaluar la prioridad de los recursos a precargar"
        ],
        "severity": "baja"
    },
    "200": {
        "title": "OK",
        "type": "Éxito",
        "description": "La solicitud se ha completado exitosamente.",
        "solutions": ["Respuesta exitosa estándar, no se requiere acción"],
        "severity": "ninguna"
    },
    "201": {
        "title": "Created",
        "type": "Éxito",
        "description": "La solicitud se ha completado y se ha creado un nuevo recurso.",
        "solutions": [
            "Verificar que el recurso se haya creado correctamente",
            "Comprobar la respuesta para obtener la ubicación del nuevo recurso"
        ],
        "severity": "ninguna"
    },
    "202": {
        "title": "Accepted",
        "type": "Éxito",
        "description": "La solicitud ha sido aceptada para procesamiento, pero el procesamiento no ha sido completado.",
        "solutions": [
            "Implementar un sistema de seguimiento del estado del procesamiento",
            "Proporcionar un endpoint para consultar el estado del proceso",
            "Considerar notificaciones asíncronas del resultado"
        ],
        "severity": "ninguna"
    },
    "203": {
        "title": "Non-Authoritative Information",
        "type": "Éxito",
        "description": "La respuesta fue exitosa, pero los contenidos han sido modificados por un proxy intermedio.",
        "solutions": [
            "Verificar la integridad de los datos recibidos",
            "Considerar la implementación de verificaciones de integridad",
            "Evaluar la necesidad de conexiones directas"
        ],
        "severity": "baja"
    },
    "204": {
        "title": "No Content",
        "type": "Éxito",
        "description": "La solicitud se ha completado exitosamente pero no hay contenido para enviar.",
        "solutions": [
            "Verificar que la ausencia de contenido sea intencional",
            "Actualizar la interfaz de usuario según corresponda",
            "Considerar el uso de códigos alternativos si se espera contenido"
        ],
        "severity": "ninguna"
    },
    "205": {
        "title": "Reset Content",
        "type": "Éxito",
        "description": "El servidor indica al cliente que reinicie la vista del documento.",
        "solutions": [
            "Implementar la lógica de reinicio en el cliente",
            "Verificar que los formularios se limpien correctamente",
            "Asegurar que la interfaz de usuario se actualice apropiadamente"
        ],
        "severity": "ninguna"
    },
    "206": {
        "title": "Partial Content",
        "type": "Éxito",
        "description": "El servidor está entregando solo parte del recurso debido a un encabezado de rango enviado por el cliente.",
        "solutions": [
            "Implementar manejo de rangos en el cliente",
            "Verificar la integridad de las partes recibidas",
            "Considerar la implementación de descarga resumible"
        ],
        "severity": "ninguna"
    },
    "300": {
        "title": "Multiple Choices",
        "type": "Redirección",
        "description": "Existen múltiples opciones para el recurso solicitado.",
        "solutions": [
            "Implementar lógica de selección en el cliente",
            "Proporcionar una interfaz clara para la selección del usuario",
            "Considerar redirección automática a la opción preferida"
        ],
        "severity": "baja"
    },
    "301": {
        "title": "Moved Permanently",
        "type": "Redirección",
        "description": "El recurso solicitado ha sido movido permanentemente a una nueva URL.",
        "solutions": [
            "Actualizar marcadores y enlaces",
            "Implementar manejo adecuado de redirecciones",
            "Actualizar URLs hardcodeadas en el código"
        ],
        "severity": "media"
    },
    "302": {
        "title": "Found",
        "type": "Redirección",
        "description": "El recurso solicitado se encuentra temporalmente en una URL diferente.",
        "solutions": [
            "Implementar seguimiento de redirecciones temporales",
            "Mantener la URL original para futuras solicitudes",
            "Verificar la cadena de redirecciones"
        ],
        "severity": "baja"
    },
    "303": {
        "title": "See Other",
        "type": "Redirección",
        "description": "El recurso puede ser encontrado en otra URL usando GET.",
        "solutions": [
            "Implementar redirección GET automática",
            "Mantener el contexto de la solicitud original",
            "Verificar la seguridad de la redirección"
        ],
        "severity": "baja"
    },
    "304": {
        "title": "Not Modified",
        "type": "Redirección",
        "description": "El recurso no ha sido modificado desde la última solicitud.",
        "solutions": [
            "Implementar cache-control adecuado",
            "Utilizar ETags para validación",
            "Optimizar el uso de caché en el cliente"
        ],
        "severity": "ninguna"
    },
    "307": {
        "title": "Temporary Redirect",
        "type": "Redirección",
        "description": "El recurso se encuentra temporalmente en otra URL y se debe mantener el método HTTP original.",
        "solutions": [
            "Mantener el método HTTP en la redirección",
            "Implementar límite de redirecciones",
            "Verificar la seguridad de la redirección"
        ],
        "severity": "baja"
    },
    "308": {
        "title": "Permanent Redirect",
        "type": "Redirección",
        "description": "El recurso se ha movido permanentemente a otra URL y se debe mantener el método HTTP original.",
        "solutions": [
            "Actualizar referencias permanentes",
            "Mantener el método HTTP en la redirección",
            "Implementar actualización automática de enlaces"
        ],
        "severity": "media"
    },
    "400": {
        "title": "Bad Request",
        "type": "Error de Cliente",
        "description": "El servidor no puede procesar la solicitud debido a un error del cliente.",
        "solutions": [
            "Verificar la sintaxis de la solicitud",
            "Revisar parámetros y encabezados",
            "Validar el formato de los datos de entrada"
        ],
        "severity": "alta"
    },
    "401": {
        "title": "Unauthorized",
        "type": "Error de Cliente",
        "description": "La solicitud requiere autenticación del usuario.",
        "solutions": [
            "Verificar credenciales de autenticación",
            "Comprobar que el token de acceso sea válido",
            "Asegurarse de incluir las cabeceras de autenticación correctas"
        ],
        "severity": "alta"
    },
    "402": {
        "title": "Payment Required",
        "type": "Error de Cliente",
        "description": "Se requiere pago para acceder al recurso (código reservado para uso futuro).",
        "solutions": [
            "Verificar estado de la suscripción",
            "Implementar proceso de pago",
            "Validar métodos de pago disponibles"
        ],
        "severity": "alta"
    },
    "403": {
        "title": "Forbidden",
        "type": "Error de Cliente",
        "description": "El servidor ha entendido la solicitud pero se niega a autorizarla.",
        "solutions": [
            "Verificar permisos del usuario",
            "Comprobar roles y niveles de acceso",
            "Revisar políticas de seguridad"
        ],
        "severity": "alta"
    },
    "404": {
        "title": "Not Found",
        "type": "Error de Cliente",
        "description": "El recurso solicitado no se encuentra en el servidor.",
        "solutions": [
            "Verificar que la URL sea correcta",
            "Comprobar si el recurso existe",
            "Revisar la configuración de rutas"
        ],
        "severity": "alta"
    },
    "405": {
        "title": "Method Not Allowed",
        "type": "Error de Cliente",
        "description": "El método HTTP utilizado no está permitido para el recurso solicitado.",
        "solutions": [
            "Verificar los métodos HTTP permitidos",
            "Implementar los métodos necesarios",
            "Revisar la configuración de CORS"
        ],
        "severity": "alta"
    },
    "406": {
        "title": "Not Acceptable",
        "type": "Error de Cliente",
        "description": "El recurso no puede generar una respuesta que cumpla con los requisitos de contenido especificados.",
        "solutions": [
            "Revisar los encabezados Accept",
            "Implementar formatos de respuesta adicionales",
            "Verificar la negociación de contenido"
        ],
        "severity": "alta"
    },
    "407": {
        "title": "Proxy Authentication Required",
        "type": "Error de Cliente",
        "description": "Se requiere autenticación con el proxy antes de procesar la solicitud.",
        "solutions": [
            "Verificar credenciales del proxy",
            "Implementar autenticación de proxy",
            "Revisar configuración de proxy"
        ],
        "severity": "alta"
    },
    "408": {
        "title": "Request Timeout",
        "type": "Error de Cliente",
        "description": "El servidor agotó el tiempo de espera mientras aguardaba la solicitud.",
        "solutions": [
            "Optimizar el tiempo de solicitud",
            "Implementar reintentos automáticos",
            "Revisar la conectividad de red"
        ],
        "severity": "alta"
    },
    "409": {
        "title": "Conflict",
        "type": "Error de Cliente",
        "description": "La solicitud genera un conflicto con el estado actual del recurso.",
        "solutions": [
            "Implementar control de concurrencia",
            "Manejar conflictos de versiones",
            "Proporcionar mecanismo de resolución de conflictos"
        ],
        "severity": "alta"
    },
    "410": {
        "title": "Gone",
        "type": "Error de Cliente",
        "description": "El recurso solicitado ya no está disponible y no lo estará de nuevo.",
        "solutions": [
            "Eliminar referencias al recurso",
            "Implementar redirección a alternativas",
            "Actualizar enlaces y referencias"
        ],
        "severity": "alta"
    },
    "411": {
        "title": "Length Required",
        "type": "Error de Cliente",
        "description": "El servidor requiere que se especifique la longitud del contenido.",
        "solutions": [
            "Incluir encabezado Content-Length",
            "Verificar el tamaño del contenido",
            "Implementar manejo de contenido chunked"
        ],
        "severity": "media"
    },
    "412": {
        "title": "Precondition Failed",
        "type": "Error de Cliente",
        "description": "Una precondición especificada en los encabezados no se cumple.",
        "solutions": [
            "Verificar condiciones previas",
            "Actualizar encabezados condicionales",
            "Implementar manejo de condiciones"
        ],
        "severity": "media"
    },
    "413": {
        "title": "Payload Too Large",
        "type": "Error de Cliente",
        "description": "La solicitud es más grande de lo que el servidor está dispuesto a procesar.",
        "solutions": [
            "Reducir el tamaño de la solicitud",
            "Implementar carga fragmentada",
            "Ajustar límites del servidor"
        ],
        "severity": "alta"
    },
    "414": {
        "title": "URI Too Long",
        "type": "Error de Cliente",
        "description": "La URI solicitada es más larga de lo que el servidor puede procesar.",
        "solutions": [
            "Reducir la longitud de la URI",
            "Usar métodos POST para datos extensos",
            "Optimizar parámetros de consulta"
        ],
        "severity": "alta"
    },
    "415": {
        "title": "Unsupported Media Type",
        "type": "Error de Cliente",
        "description": "El formato del contenido de la solicitud no es soportado.",
        "solutions": [
            "Verificar tipos de contenido aceptados",
            "Ajustar el formato de la solicitud",
            "Implementar conversión de formatos"
        ],
        "severity": "alta"
    },
    "416": {
        "title": "Range Not Satisfiable",
        "type": "Error de Cliente",
        "description": "El rango especificado en la solicitud no puede ser satisfecho.",
        "solutions": [
            "Verificar rangos válidos",
            "Implementar manejo de rangos apropiado",
            "Ajustar solicitud de rangos"
        ],
        "severity": "media"
    },
    "417": {
        "title": "Expectation Failed",
        "type": "Error de Cliente",
        "description": "El servidor no puede cumplir con las expectativas indicadas en el encabezado Expect.",
        "solutions": [
            "Revisar los encabezados Expect",
            "Ajustar las expectativas del cliente",
            "Verificar capacidades del servidor"
        ],
        "severity": "media"
    },
    "418": {
        "title": "I'm a teapot",
        "type": "Error de Cliente",
        "description": "El servidor se niega a preparar café porque es una tetera (código de error de broma).",
        "solutions": [
            "Utilizar una cafetera en lugar de una tetera",
            "Verificar el tipo de dispositivo correcto",
            "Considerar preparar té en su lugar"
        ],
        "severity": "baja"
    },
    "421": {
        "title": "Misdirected Request",
        "type": "Error de Cliente",
        "description": "La solicitud fue dirigida a un servidor que no puede producir una respuesta.",
        "solutions": [
            "Verificar la configuración del servidor",
            "Revisar el enrutamiento de la solicitud",
            "Actualizar la dirección del servidor"
        ],
        "severity": "alta"
    },
    "422": {
        "title": "Unprocessable Entity",
        "type": "Error de Cliente",
        "description": "La solicitud está bien formada pero contiene errores semánticos.",
        "solutions": [
            "Validar la semántica de los datos",
            "Corregir errores de validación",
            "Verificar la lógica de negocio"
        ],
        "severity": "alta"
    },
    "423": {
        "title": "Locked",
        "type": "Error de Cliente",
        "description": "El recurso que se está accediendo está bloqueado.",
        "solutions": [
            "Esperar a que el recurso se desbloquee",
            "Implementar sistema de cola",
            "Verificar el estado del bloqueo"
        ],
        "severity": "alta"
    },
    "424": {
        "title": "Failed Dependency",
        "type": "Error de Cliente",
        "description": "La solicitud falló debido a una falla en una solicitud previa.",
        "solutions": [
            "Verificar dependencias previas",
            "Implementar manejo de errores en cadena",
            "Revisar el flujo de operaciones"
        ],
        "severity": "alta"
    },
    "426": {
        "title": "Upgrade Required",
        "type": "Error de Cliente",
        "description": "El cliente debe actualizar a un protocolo diferente.",
        "solutions": [
            "Actualizar el protocolo del cliente",
            "Implementar el protocolo requerido",
            "Verificar compatibilidad de protocolos"
        ],
        "severity": "alta"
    },
    "428": {
        "title": "Precondition Required",
        "type": "Error de Cliente",
        "description": "El servidor requiere que la solicitud sea condicional.",
        "solutions": [
            "Implementar validación condicional",
            "Agregar encabezados de precondición",
            "Manejar conflictos de actualización"
        ],
        "severity": "alta"
    },
    "429": {
        "title": "Too Many Requests",
        "type": "Error de Cliente",
        "description": "El usuario ha enviado demasiadas solicitudes en un período de tiempo determinado.",
        "solutions": [
            "Implementar limitación de velocidad en el cliente",
            "Agregar throttling de solicitudes",
            "Cachear respuestas cuando sea posible",
            "Revisar patrones de uso de la API"
        ],
        "severity": "alta"
    },
    "431": {
        "title": "Request Header Fields Too Large",
        "type": "Error de Cliente",
        "description": "Los campos de encabezado son demasiado grandes para ser procesados.",
        "solutions": [
            "Reducir el tamaño de los encabezados",
            "Optimizar la información enviada",
            "Ajustar límites del servidor"
        ],
        "severity": "alta"
    },
    "451": {
        "title": "Unavailable For Legal Reasons",
        "type": "Error de Cliente",
        "description": "El recurso no está disponible por razones legales.",
        "solutions": [
            "Verificar restricciones legales",
            "Implementar alternativas permitidas",
            "Consultar requisitos legales aplicables"
        ],
        "severity": "alta"
    },
    "500": {
        "title": "Internal Server Error",
        "type": "Error de Servidor",
        "description": "El servidor ha encontrado una situación inesperada que le impide completar la solicitud.",
        "solutions": [
            "Revisar logs del servidor para errores",
            "Depurar código del lado del servidor",
            "Verificar configuración del servidor",
            "Implementar manejo de errores adecuado"
        ],
        "severity": "crítica"
    },
    "501": {
        "title": "Not Implemented",
        "type": "Error de Servidor",
        "description": "El servidor no soporta la funcionalidad requerida para completar la solicitud.",
        "solutions": [
            "Implementar la funcionalidad faltante",
            "Documentar características no soportadas",
            "Planificar desarrollo de funcionalidades"
        ],
        "severity": "crítica"
    },
    "502": {
        "title": "Bad Gateway",
        "type": "Error de Servidor",
        "description": "El servidor recibió una respuesta inválida del servidor upstream.",
        "solutions": [
            "Verificar estado del servidor upstream",
            "Comprobar conectividad de red",
            "Revisar configuración del proxy",
            "Verificar logs del servidor"
        ],
        "severity": "crítica"
    },
    "503": {
        "title": "Service Unavailable",
        "type": "Error de Servidor",
        "description": "El servidor no está disponible para manejar la solicitud en este momento.",
        "solutions": [
            "Verificar estado del servidor",
            "Comprobar capacidad del sistema",
            "Revisar logs de error",
            "Implementar estrategia de failover"
        ],
        "severity": "crítica"
    },
    "504": {
        "title": "Gateway Timeout",
        "type": "Error de Servidor",
        "description": "El servidor, actuando como gateway, no recibió una respuesta a tiempo del servidor upstream.",
        "solutions": [
            "Verificar tiempos de respuesta upstream",
            "Ajustar configuración de timeouts",
            "Implementar circuit breakers",
            "Monitorear latencia de red"
        ],
        "severity": "crítica"
    },
    "505": {
        "title": "HTTP Version Not Supported",
        "type": "Error de Servidor",
        "description": "El servidor no soporta la versión del protocolo HTTP utilizada en la solicitud.",
        "solutions": [
            "Actualizar servidor para soportar la versión",
            "Utilizar versión compatible de HTTP",
            "Documentar versiones soportadas"
        ],
        "severity": "crítica"
    },
    "506": {
        "title": "Variant Also Negotiates",
        "type": "Error de Servidor",
        "description": "Error de configuración del servidor en la negociación de contenido.",
        "solutions": [
            "Corregir configuración de negociación",
            "Revisar política de contenido",
            "Verificar configuración del servidor"
        ],
        "severity": "crítica"
    },
    "507": {
        "title": "Insufficient Storage",
        "type": "Error de Servidor",
        "description": "El servidor no puede almacenar la representación necesaria para completar la solicitud.",
        "solutions": [
            "Liberar espacio en el servidor",
            "Implementar gestión de almacenamiento",
            "Monitorear uso de recursos"
        ],
        "severity": "crítica"
    },
    "508": {
        "title": "Loop Detected",
        "type": "Error de Servidor",
        "description": "El servidor detectó un bucle infinito al procesar la solicitud.",
        "solutions": [
            "Verificar lógica de redirección",
            "Implementar detección de ciclos",
            "Revisar configuración de enrutamiento"
        ],
        "severity": "crítica"
    },
    "510": {
        "title": "Not Extended",
        "type": "Error de Servidor",
        "description": "El servidor requiere extensiones adicionales para completar la solicitud.",
        "solutions": [
            "Implementar extensiones requeridas",
            "Verificar requisitos del servidor",
            "Actualizar configuración del servidor"
        ],
        "severity": "crítica"
    },
    "511": {
        "title": "Network Authentication Required",
        "type": "Error de Servidor",
        "description": "El cliente debe autenticarse para obtener acceso a la red.",
        "solutions": [
            "Completar autenticación de red",
            "Verificar credenciales de red",
            "Implementar portal cautivo"
        ],
        "severity": "alta"
    }
}