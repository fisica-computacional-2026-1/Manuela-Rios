# W09 Report

## Parte A — Limpieza avanzada

### method_synonyms
Se creó la tabla `method_synonyms(raw_norm, canonical)` con más de 6 filas para mapear variaciones textuales de métodos de descubrimiento a una forma canónica en snake_case.

### silver_planet_v3
Se construyó `silver_planet_v3` incluyendo:
- `hostname_canon = LOWER(TRIM(hostname))`
- `discoverymethod_canon` usando sinónimos y `COALESCE` como fallback
- `disc_year_int = TRY_CAST(disc_year AS INTEGER)`
- `disc_year_bad` como bandera de años inválidos o fuera de rango

## Evidencia
- conteo total de filas en `silver_planet_v3`
- conteo de filas marcadas con `disc_year_bad`

## Interpretación
La limpieza avanzada mejora consistencia de texto y hace explícitos los problemas de calidad temporal sin eliminar automáticamente todos los registros sospechosos.
