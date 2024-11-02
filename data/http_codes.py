HTTP_CODES = {
    "100": {
        "title": "Continuar",
        "type": "Informativo",
        "description": "El servidor ha recibido los headers de la solicitud y el cliente debería proceder a enviar el cuerpo de la misma.",
        "solutions": [
            "Verificar si el cuerpo de la solicitud se está enviando correctamente",
            "Comprobar si el encabezado Expect se está utilizando adecuadamente"
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
        "title": "Creado",
        "type": "Éxito",
        "description": "La solicitud se ha completado y se ha creado un nuevo recurso.",
        "solutions": [
            "Verificar que el recurso se haya creado correctamente",
            "Comprobar la respuesta para obtener la ubicación del nuevo recurso"
        ],
        "severity": "ninguna"
    },
    "301": {
        "title": "Movido Permanentemente",
        "type": "Redirección",
        "description": "El recurso solicitado ha sido movido permanentemente a una nueva URL.",
        "solutions": [
            "Actualizar marcadores y enlaces",
            "Implementar manejo adecuado de redirecciones",
            "Actualizar URLs hardcodeadas en el código"
        ],
        "severity": "media"
    },
    "400": {
        "title": "Solicitud Incorrecta",
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
        "title": "No Autorizado",
        "type": "Error de Cliente",
        "description": "La solicitud requiere autenticación del usuario.",
        "solutions": [
            "Verificar credenciales de autenticación",
            "Comprobar que el token de acceso sea válido",
            "Asegurarse de incluir las cabeceras de autenticación correctas"
        ],
        "severity": "alta"
    },
    "403": {
        "title": "Prohibido",
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
        "title": "No Encontrado",
        "type": "Error de Cliente",
        "description": "El recurso solicitado no se encuentra en el servidor.",
        "solutions": [
            "Verificar que la URL sea correcta",
            "Comprobar si el recurso existe",
            "Revisar la configuración de rutas"
        ],
        "severity": "alta"
    },
    "429": {
        "title": "Demasiadas Solicitudes",
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
    "500": {
        "title": "Error Interno del Servidor",
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
    "502": {
        "title": "Puerta de Enlace Incorrecta",
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
        "title": "Servicio No Disponible",
        "type": "Error de Servidor",
        "description": "El servidor no está disponible para manejar la solicitud en este momento.",
        "solutions": [
            "Verificar estado del servidor",
            "Comprobar capacidad del sistema",
            "Revisar logs de error",
            "Implementar estrategia de failover"
        ],
        "severity": "crítica"
    }
}