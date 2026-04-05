# W03 Join Case

## Caso real de JOIN malo

### Evidencia antes y después
- `n_fact = 6087`
- `n_join_bad = 10739`
- `n_join_fixed = 6087`
- Inflación detectada: `4652` filas adicionales en el JOIN malo.

## Diagnóstico
El problema apareció al unir `fact_planet` con `dim_host_year_bad` usando solo `hostname`. Esa tabla derivada no tenía una fila única por host, porque conservaba múltiples combinaciones de `hostname` y `disc_year`. Como resultado, varias filas de la tabla de hechos se repitieron al hacer el JOIN.

## Evidencia de duplicados
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

## Fix aplicado
Se creó `dim_host_year_fixed` agregando por `hostname` y conservando un único valor (`MIN(disc_year) AS first_disc_year`) para asegurar una sola fila por clave.

### SQL del fix
```sql
CREATE OR REPLACE TABLE dim_host_year_fixed AS
SELECT
  hostname,
  MIN(disc_year) AS first_disc_year
FROM dim_host_year_bad
GROUP BY hostname;
```

## Conclusión
El caso muestra que un JOIN puede ser sintácticamente correcto y, aun así, analíticamente incorrecto si la dimensión no respeta unicidad por clave. Validar cardinalidad antes de unir evita errores silenciosos en conteos y agregaciones.
