# HTTPMind 🌐

HTTPMind es una aplicación web moderna y elegante diseñada para ayudarte a entender y explorar los códigos de estado HTTP. Con una interfaz intuitiva en modo oscuro, proporciona información detallada sobre cada código de estado, incluyendo descripciones, soluciones prácticas y niveles de severidad.

![image](https://github.com/user-attachments/assets/39b97747-2dba-4125-829d-ec746dd9f40f)

## 🚀 Características

- **Búsqueda Instantánea**: Encuentra rápidamente cualquier código HTTP
- **Interfaz Moderna**: Diseño elegante en modo oscuro para mejor legibilidad
- **Información Detallada**: Para cada código HTTP, obtienes:
  - Título oficial
  - Descripción detallada
  - Lista de soluciones prácticas
  - Nivel de severidad
- **Responsive**: Funciona perfectamente en dispositivos móviles y escritorio
- **Base de Datos Completa**: Incluye todos los códigos HTTP estándar (1xx-5xx)

## 🛠️ Tecnologías Utilizadas

- Python con Flask para el backend
- JavaScript vanilla para interacciones del frontend
- CSS moderno para estilos y animaciones
- Arquitectura RESTful

## 🚦 Códigos Soportados

- **1xx**: Respuestas informativas
- **2xx**: Respuestas exitosas
- **3xx**: Redirecciones
- **4xx**: Errores del cliente
- **5xx**: Errores del servidor

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/betooxx-dev/httpmind.git
```

2. Instala las dependencias:
```bash
pip install flask
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre http://localhost:5000 en tu navegador

## 💡 Uso

1. Ingresa un código HTTP en el campo de búsqueda (ej: 404, 500)
2. Haz clic en el botón "Buscar" o presiona Enter
3. Obtén información detallada sobre el código HTTP incluyendo:
   - Descripción
   - Posibles soluciones
   - Nivel de severidad
