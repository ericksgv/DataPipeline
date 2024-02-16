# DataPipeline

## Descripción del Proyecto

DataPipeline es un proyecto diseñado para extraer, transformar, cargar y analizar datos de redes sociales sobre políticos en Bogotá y Colombia. Este proyecto tiene como objetivo determinar el impacto que tienen estos políticos en las redes sociales mediante análisis de texto para identificar temas principales y análisis de sentimientos.

## Tecnologías Utilizadas

- Python 3.8+
- twscrape para la extracción de datos de Twitter
- MongoDB para el almacenamiento de datos
- Pandas y NLTK para el procesamiento y análisis de datos
- Docker para la contenerización y despliegue

## Configuración del Entorno

Para comenzar con el proyecto, es necesario configurar el entorno de desarrollo:

1. Clona el repositorio:

```bash
git clone <url_del_repositorio>
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate 
# En Windows usa venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno copiando el archivo `.env.example` a `.env` y ajustando los valores según sea necesario.

## Uso

Descripción paso a paso de cómo usar el proyecto, incluyendo cómo ejecutar los scripts de extracción de datos, y cómo realizar análisis básicos. Por ejemplo:

```bash 
python src/etl/fetch_tweets.py
```


## Cómo Contribuir

Invitamos a contribuciones de todos los que estén interesados. Si deseas contribuir, por favor:

1. Haz un fork del proyecto.
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`).
3. Haz commit de tus cambios (`git commit -am 'Add some amazing feature'`).
4. Haz push a la rama (`git push origin feature/amazing-feature`).
5. Abre un Pull Request.

## Licencia

Este proyecto es un trabajo conjunto con los estudiantes de la Pontificia Universidad Javeriana, del curso de Análisis de de Algoritmos 2024 - I. 

---

DataPipeline © [Cristhiam Daniel Campos Julca]. Todos los derechos reservados.
