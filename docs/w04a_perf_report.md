# W04A Performance Report

## Plan 1: consulta agregada por método de descubrimiento

### SQL
```sql
SELECT
    discoverymethod,
    COUNT(*) AS n_planets,
    AVG(pl_rade) AS avg_radius
FROM silver_planet
WHERE disc_year BETWEEN 2010 AND 2025
  AND discoverymethod IS NOT NULL
  AND pl_rade IS NOT NULL
GROUP BY discoverymethod
ORDER BY n_planets DESC;
```

### EXPLAIN (resumen)
El plan muestra principalmente estos operadores:
- `SEQ_SCAN` sobre `silver_planet`
- `HASH_GROUP_BY`
- `ORDER_BY`

### Conclusión
El costo principal está en leer filas de `silver_planet` y luego agregarlas por `discoverymethod`. Una mejora razonable sería mantener filtros tempranos y proyectar solo las columnas necesarias para reducir lectura innecesaria.

## Plan 2: JOIN sano entre `fact_planet` y `dim_host_full`

### SQL
```sql
SELECT
    f.pl_name,
    f.hostname,
    f.discoverymethod,
    d.sy_dist,
    d.st_mass
FROM fact_planet f
LEFT JOIN dim_host_full d
  ON f.hostname = d.hostname
WHERE f.disc_year >= 2010
  AND f.pl_bmasse IS NOT NULL;
```

### EXPLAIN (resumen)
El plan muestra principalmente:
- `HASH_JOIN`
- `SEQ_SCAN` sobre `fact_planet`
- `SEQ_SCAN` sobre `dim_host_full`

### Conclusión
El JOIN es sano porque no infla cardinalidad y la dimensión mantiene una fila por `hostname`. Aun así, el costo crecería si se arrastran columnas innecesarias o si los filtros se aplican demasiado tarde.

## EXPLAIN ANALYZE
Se ejecutó `EXPLAIN ANALYZE` sobre la consulta agregada. El reporte mostró una ejecución rápida (aprox. `0.0105s`) y confirmó que el flujo real pasa por `TABLE_SCAN`, `HASH_GROUP_BY` y `ORDER_BY`.

## Evidencia exportada
- `artifacts/w04a_explain_q1.txt`
