# Glossary

- **Raw / Bronze**: capa inicial de datos, cercana a la fuente original, con limpieza mínima.
- **Silver**: capa intermedia donde se aplican reglas de calidad y estructura más estable.
- **Gold**: capa orientada a análisis o consumo final, normalmente agregada o resumida.
- **Grain**: nivel de detalle de una tabla. En este proyecto, una fila de `fact_planet` representa aproximadamente un planeta.
- **Primary key candidate**: columna o conjunto de columnas que podrían identificar filas de manera única.
- **NULL**: valor faltante o desconocido en una columna.
- **JOIN**: operación que combina filas de dos tablas a partir de una clave compartida.
- **Cardinalidad**: relación entre filas de dos tablas al hacer un JOIN (uno a uno, uno a muchos, etc.).
- **Sanity check**: validación rápida para detectar valores imposibles o inesperados.
- **Traceability / Trazabilidad**: capacidad de rastrear qué datos, archivos o transformaciones originaron un resultado.
- **EXPLAIN**: instrucción que muestra el plan estimado de ejecución de una consulta.
- **EXPLAIN ANALYZE**: instrucción que ejecuta la consulta y muestra tiempos y cardinalidades reales.
