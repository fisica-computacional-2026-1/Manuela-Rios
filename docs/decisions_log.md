# Decisions Log


- **Decisión:** Guardar SHA-256 del CSV raw en artifacts por cada ejecución.
- **Razón:** Detectar cambios invisibles del dato (DDIA reliability/operability).
- **Alternativas:** Confiar en el nombre del archivo (rechazada), usar solo fecha de descarga (rechazada).
- **Evidencia:** raw_sha256=bc7986bad903903a123d13e62117614a27eaffd4f9ee3436c60b1c0ac05a3fe2, n_rows=6087, n_cols=16




- Fecha: 2026-04-05
- Decisión: Usar como métrica de control el tiempo de la etapa `silver` y fijar el umbral inicial en `< 1.0 s` para este dataset local.
- Razón: `silver` concentra limpieza, filtros y creación de la tabla base para el resto del pipeline, así que es una buena etapa para monitorear si el flujo empieza a degradarse.
- Alternativas: medir solo el tiempo total del runner (rechazada), controlar únicamente la etapa `export` (rechazada).
- Evidencia: corrida 1 `silver = 0.7987 s`; corrida 2 `silver = 0.3084 s`; ambas por debajo del umbral de `1.0 s`.


- Fecha: 2026-05-26
- Decisión: Normalizar `discoverymethod` mediante una tabla `method_map` antes de construir `silver_planet_v2`.
- Razón: Diferencias de mayúsculas, espacios y variantes textuales fragmentan los conteos y vuelven menos confiables las comparaciones por método.
- Alternativas: usar el texto raw sin limpiar (rechazada), aplicar solo `LOWER(TRIM())` sin mapa explícito (rechazada).
- Evidencia: creación de `method_map`, construcción de `discoverymethod_clean` con `COALESCE(map, LOWER(TRIM(...)))` y revisión de frecuencias limpias en `silver_planet_v2`.


- Fecha: 2026-05-26
- Decisión: Introducir una tabla `method_synonyms` y una tabla `quality_events` para separar normalización semántica de controles de calidad.
- Razón: Los métodos de descubrimiento llegan con variantes de texto y los problemas de calidad deben quedar registrados como evidencia explícita, no solo implícita en una transformación.
- Alternativas: limpiar directamente sin tabla de sinónimos (rechazada), revisar calidad solo con consultas ad hoc sin persistir eventos (rechazada).
- Evidencia: creación de `method_synonyms`, construcción de `silver_planet_v3` y 4 checks cargados en `quality_events`.
