# Introducción

<p>Siempre me sorprende cuando veo ejemplos en los que solo unas pocas líneas de código Python pueden resolver un problema comercial real y ahorrar a las organizaciones mucho tiempo y dinero. También me impresiona cuando la gente descubre cómo hacer esto sin una capacitación formal, solo con un poco de trabajo duro y la voluntad de perseverar en la curva de aprendizaje.</p>

<p>Este ejemplo proviene de <i>Mark Doll</i>. Le daré la palabra para que dé su experiencia:</p>

<blockquote>He estado aprendiendo / usando Python durante aproximadamente 3 años para ayudar a automatizar los procesos comerciales y los informes. Nunca tuve ningún entrenamiento formal en Python, pero descubrí que es una herramienta confiable que me ha ayudado en mi trabajo.</blockquote>

## El problema

<p>Aquí está la descripción general del problema de Mark:</p>

<blockquote>Surgió una necesidad empresarial de separar las filas de un archivo Excel a una lista de ~ 500 usuarios y nos presentó una gran tarea para completar manualmente. Hacer esta tarea más difícil fue el hecho de que tuvimos que dividir los datos por usuario de un archivo maestro de Excel para crear su propio archivo específico dividido por fecha. Dentro de la carpeta data y adjuntos</blockquote>

<blockquote>Imagine el tiempo que tomaría filtrar, cortar y pegar manualmente los datos en un archivo, luego guardarlo y enviarlo por correo electrónico, ¡500 veces! Con este enfoque de Python pudimos automatizar todo el proceso y ahorrar un tiempo valioso.</blockquote>

<p>He visto este tipo de problema varias veces en mi experiencia. Si no tiene experiencia con un lenguaje de programación, entonces puede parecer abrumador. Con Python, es muy factible automatizar este tedioso proceso. En el siguiente código está la solución</p>

## Instalación

### Crear entorno virtual

```
    virtualenv venv
```

### Activar entorno virtual

```
    venv\Scripts\activate
```

### Instalar requerimientos

```
    pip install -r requirements.txt
```

### Disfrutar la aplicación

```
    python main.py
```
