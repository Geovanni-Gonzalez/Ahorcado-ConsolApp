# Proyecto Programado #1: Ahorcado

## Información del Estudiante

- **Nombre del Curso**: Programación
- **Número de semestre y año lectivo**: I Semestre 2026
- **Nombre del Estudiante**: [Nombre del Estudiante]
- **Número de carné del estudiante**: [Carné]
- **Estatus de la entrega**: Excelente

## Descripción del Problema

Este proyecto consiste en una aplicación de consola en Python para jugar al Ahorcado. El sistema permite administrar palabras y frases mediante un módulo administrativo protegido por contraseña, y jugar en dos niveles de dificultad (Principiante y Avanzado). Además, guarda un historial de juegos y estadísticas.

## Manual de Usuario

### Ejecución

1. Abra una terminal en la carpeta principal del proyecto.
2. Ejecute el comando:

   ```bash
   python main.py
   ```

### Uso

- **Menú Principal**:
  - **(A) Opciones Administrativas**: Requiere clave (`admin123`). Permite gestionar palabras y frases.
  - **(J) Opciones de Jugador**: Accede al juego, historia y estadísticas.
  - **(S) Salir**: Cierra la aplicación.

- **Juego**:
  - Seleccione "Nuevo Juego".
  - Ingrese su nombre.
  - Seleccione el idioma (ES/EN).
  - Seleccione el modo (Principiante/Avanzado).
  - Intente adivinar la palabra letra por letra.

## Decisiones de Desarrollo

- **Restricciones Técnicas**: Se implementaron funciones personalizadas (`my_len`, `my_split`, `my_strip`, `my_in`, `my_append`) en `src/utils.py` para cumplir con la restricción de NO utilizar funciones built-in prohibidas (`len`, `split`, `strip`, `append`, `in`).
- **Persistencia**: Todos los datos (palabras, frases, historial, juegos) se almacenan en archivos de texto en la carpeta `data/`.
- **Estructura Modular**: El código se dividió en módulos (`admin`, `auth`, `game`, `stats`, `utils`) para facilitar el mantenimiento.

## Librerías Usadas

- `os`: Para manejo de archivos y limpieza de pantalla.
- `random`: Para selección aleatoria de palabras.
- No se utilizaron librerías externas.

## Análisis de Resultados

- **Objetivos Alcanzados**:
  - Juego funcional en dos modos.
  - Gestión administrativa completa (CRUD).
  - Persistencia de datos.
  - Soporte bilingüe (Español/Inglés).
  - Cumplimiento de restricciones de funciones built-in.
- **Objetivos No Alcanzados**: N/A

## Conclusión

El proyecto cumple con todos los requerimientos funcionales y técnicos establecidos, incluyendo las funcionalidades extra de soporte de idiomas.
