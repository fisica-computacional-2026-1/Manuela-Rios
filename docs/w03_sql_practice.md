# W03 SQL Practice

## Análisis de cardinalidad con `dim_host_full`

### Conteos principales
- `n_fact = 6087`
- `n_join_good = 6087`
- `n_join_bad = 10739`
- `n_join_fixed = 6087`

### Explicación
El JOIN sano conserva el mismo número de filas que la tabla de hechos porque la dimensión corregida tiene una sola fila por `hostname`. En cambio, el JOIN malo infla resultados porque la tabla `dim_host_year_bad` contiene múltiples filas por host, así que varias filas de `fact_planet` se repiten al unir solo por esa clave. Cuando la dimensión se corrige con agregación previa, el conteo vuelve a coincidir con `n_fact`.

## Evidencia de duplicados en la dimensión mala

### SQL
```sql
SELECT
  hostname,
  COUNT(*) AS repeats
FROM dim_host_year_bad
GROUP BY hostname
HAVING COUNT(*) > 1
ORDER BY repeats DESC, hostname ASC
LIMIT 10;
```

### Output (resumen)
- `KOI-351 = 8`
- `TRAPPIST-1 = 7`
- `HD 10180 = 6`
- `HD 110067 = 6`
- `HD 191939 = 6`

## Caso de JOIN malo

### SQL usada para crear la dimensión problemática
```sql
CREATE OR REPLACE TABLE dim_host_year_bad AS
SELECT
  hostname,
  disc_year
FROM fact_planet
WHERE hostname IS NOT NULL
  AND disc_year IS NOT NULL;
```

### SQL usada para la dimensión corregida
```sql
CREATE OR REPLACE TABLE dim_host_year_fixed AS
SELECT
  hostname,
  MIN(disc_year) AS first_disc_year
FROM dim_host_year_bad
GROUP BY hostname;
```

## Consulta extra con JOIN

### SQL
```sql
SELECT
  f.discoverymethod,
  COUNT(*) AS n_planets,
  MIN(d.first_disc_year) AS oldest_host_year,
  MAX(d.first_disc_year) AS newest_host_year
FROM fact_planet f
LEFT JOIN dim_host_year_fixed d
  ON f.hostname = d.hostname
WHERE f.discoverymethod IS NOT NULL
GROUP BY f.discoverymethod
ORDER BY n_planets DESC
LIMIT 10;
```

### Output (resumen)
- `Transit` → `4488`, `oldest_host_year = 2001`, `newest_host_year = 2026`
- `Radial Velocity` → `1161`, `oldest_host_year = 1995`, `newest_host_year = 2026`
- `Microlensing` → `265`, `oldest_host_year = 2004`, `newest_host_year = 2026`

## Consulta extra con CTE

### SQL
```sql
WITH host_summary AS (
  SELECT
    hostname,
    COUNT(*) AS n_planets,
    AVG(pl_rade) AS avg_radius,
    AVG(pl_orbper) AS avg_orbper
  FROM fact_planet
  WHERE hostname IS NOT NULL
  GROUP BY hostname
)
SELECT
  hostname,
  n_planets,
  avg_radius,
  avg_orbper
FROM host_summary
WHERE n_planets >= 2
  AND avg_radius IS NOT NULL
ORDER BY n_planets DESC, avg_radius DESC
LIMIT 10;
```

### Output (resumen)
- `KOI-351` → `n_planets = 8`, `avg_radius = 3.9`
- `TRAPPIST-1` → `n_planets = 7`, `avg_radius ≈ 0.98`
- `HD 34445` → `n_planets = 6`, `avg_radius ≈ 8.86`

## Caso real de JOIN malo para `docs/w03_join_case.md`

### Evidencia
- Antes del JOIN: `n_fact = 6087`
- Después del JOIN malo: `n_join_bad = 10739`
- Después del fix: `n_join_fixed = 6087`

### Diagnóstico
La clave problemática fue `hostname`, porque en la tabla `dim_host_year_bad` no era única. Eso hizo que un mismo host apareciera varias veces y multiplicara filas al unirlo con `fact_planet`.

### Fix aplicado
Se creó `dim_host_year_fixed` con una agregación por `hostname` para asegurar una sola fila por clave antes del JOIN.
