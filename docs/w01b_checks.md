# W01B Checks

## Check 1: tamaño básico del dataset

### SQL
```sql
SELECT COUNT(*) AS n_rows FROM raw_ps;
SELECT COUNT(*) AS n_cols FROM pragma_table_info('raw_ps');
```

### Resultado
- `n_rows = 6087`
- `n_cols = 16`

## Check 2: nulos en `pl_name`

### SQL
```sql
SELECT COUNT(*) AS null_pl_name
FROM raw_ps
WHERE pl_name IS NULL;
```

### Resultado
- `null_pl_name = 0`

## Check 3: muestra de columnas clave

### SQL
```sql
SELECT pl_name, hostname, discoverymethod, disc_year
FROM raw_ps
WHERE pl_name IS NOT NULL
LIMIT 10;
```

### Resultado
La muestra devuelve registros válidos con nombre del planeta, host, método de descubrimiento y año, lo cual confirma que las columnas principales están disponibles para el resto del curso.

## Check 4 (tarea): años de descubrimiento fuera de rango

### SQL
```sql
SELECT
    COUNT(*) AS total_out_of_range,
    MIN(disc_year) AS min_disc_year,
    MAX(disc_year) AS max_disc_year
FROM raw_ps
WHERE disc_year IS NOT NULL
  AND (disc_year < 1980 OR disc_year > 2026);
```

### Resultado
- `total_out_of_range = 0`
- `min_disc_year = NULL`
- `max_disc_year = NULL`

## Interpretación
El sanity check adicional no encontró años de descubrimiento fuera del rango esperado, así que no hay evidencia de errores obvios de fecha en esta columna para la versión actual del dataset.
