# W08 Report

## A1 — method_map
Se creó la tabla `method_map` con al menos 6 mapeos raw → canonical para normalizar variaciones de los métodos de descubrimiento, incluyendo ejemplos como `Transit`, `transit`, ` TRANSIT ` y `Radial Velocity`.

## A2 — silver_planet_v2
Se construyó `silver_planet_v2` a partir de `raw_ps` con tres transformaciones principales:
- `hostname_clean = LOWER(TRIM(hostname))`
- `discoverymethod_clean = COALESCE(map, LOWER(TRIM(discoverymethod_norm)))`
- `disc_era` como categorización por década (`pre_1990`, `1990s`, `2000s`, `2010s`, `2020s`)

### Evidencia
- Se verificó el conteo total de filas en `silver_planet_v2`.
- Se revisó que `hostname_clean` no quedara nulo.
- Se listaron los métodos limpios más frecuentes usando `discoverymethod_clean`.

## B1 — Many-to-Many (toy schema)
Se creó un ejemplo M:N con las tablas:
- `planet_demo(planet_id PRIMARY KEY, name NOT NULL)`
- `method_demo(method_id PRIMARY KEY, method_name UNIQUE NOT NULL)`
- `planet_method_demo(planet_id, method_id)` con PK compuesta y FKs hacia ambas tablas.

Se insertaron 4 planetas, 3 métodos y relaciones M:N, incluyendo planetas con más de un método.

### Pregunta 1 — # planetas por método
Se respondió con una consulta usando `COUNT(DISTINCT pm.planet_id)` agrupada por `method_name`.

### Pregunta 2 — # métodos por planeta
Se respondió con una consulta usando `COUNT(DISTINCT pm.method_id)` agrupada por nombre del planeta.

## B2 — Check de duplicados en la link table
Se ejecutó el check:

```sql
SELECT planet_id, method_id, COUNT(*) AS c
FROM planet_method_demo
GROUP BY planet_id, method_id
HAVING COUNT(*) > 1;
```

El resultado debe retornar vacío, lo que confirma que no existen pares duplicados y que la PK compuesta protege la cardinalidad esperada.

## Decisión tomada
Se decidió normalizar los métodos de descubrimiento antes de crear nuevas capas analíticas, para evitar que variaciones de texto fragmenten conteos y comparaciones.
