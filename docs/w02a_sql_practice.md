# W02 SQL Practice

## 1) Consulta de calidad: registros sin nombre de planeta o sin hostname

### SQL
```sql
SELECT
  SUM(CASE WHEN pl_name IS NULL THEN 1 ELSE 0 END) AS null_pl_name,
  SUM(CASE WHEN hostname IS NULL THEN 1 ELSE 0 END) AS null_hostname
FROM raw_ps;
```

### Output
- `null_pl_name = 0`
- `null_hostname = 0`

## 2) Consulta de calidad: métodos de descubrimiento poco frecuentes

### SQL
```sql
SELECT
  discoverymethod,
  COUNT(*) AS n_rows
FROM raw_ps
WHERE discoverymethod IS NOT NULL
GROUP BY discoverymethod
HAVING COUNT(*) <= 3
ORDER BY n_rows ASC, discoverymethod ASC;
```

### Output
- `Disk Kinematics = 1`
- `Pulsation Timing Variations = 2`

## 3) Consulta analítica: métodos con menor periodo orbital mediano

### SQL
```sql
SELECT
  discoverymethod,
  COUNT(*) AS n_planets,
  MEDIAN(pl_orbper) AS median_orbper
FROM raw_ps
WHERE pl_orbper IS NOT NULL
GROUP BY discoverymethod
HAVING COUNT(*) >= 5
ORDER BY median_orbper ASC
LIMIT 10;
```

### Output (resumen)
- `Orbital Brightness Modulation` → `n_planets = 9`, `median_orbper = 0.81161`
- `Transit` → `n_planets = 4488`, `median_orbper = 8.15909335`
- `Pulsar Timing` → `n_planets = 7`, `median_orbper = 25.262`
- `Transit Timing Variations` → `n_planets = 39`, `median_orbper = 30.0`
- `Radial Velocity` → `n_planets = 1161`, `median_orbper = 305.5`

### Interpretación
Esta consulta sugiere que ciertos métodos detectan con mayor frecuencia planetas de órbita corta. También deja ver sesgos observacionales: por ejemplo, `Transit` concentra muchos hallazgos con periodos orbitales relativamente pequeños.

## 4) Consulta analítica: años con más descubrimientos y masa promedio reportada

### SQL
```sql
SELECT
  disc_year,
  COUNT(*) AS n_discoveries,
  AVG(pl_bmasse) AS avg_mass_earth
FROM raw_ps
WHERE disc_year IS NOT NULL
GROUP BY disc_year
HAVING COUNT(*) >= 20
ORDER BY n_discoveries DESC, disc_year DESC
LIMIT 10;
```

### Output (resumen)
- `2016` → `n_discoveries = 1496`, `avg_mass_earth = 82.8153`
- `2014` → `n_discoveries = 869`, `avg_mass_earth = 113.1603`
- `2021` → `n_discoveries = 554`, `avg_mass_earth = 250.9270`
- `2022` → `n_discoveries = 369`, `avg_mass_earth = 843.4636`
- `2023` → `n_discoveries = 326`, `avg_mass_earth = 546.7222`

### Interpretación
Los años con más descubrimientos reflejan cambios en capacidad observacional y campañas científicas más intensivas. La masa promedio disponible también ayuda a ver qué tan completas estaban las mediciones en esos periodos.

## Reflexión

### ¿Qué consulta te pareció más difícil y por qué?
La parte más delicada fue decidir cuándo una consulta era realmente comparable entre grupos, porque en este dataset varias columnas tienen valores faltantes y eso cambia bastante el significado de un promedio o una mediana.

### Si el dataset creciera 100×, ¿qué consultas crees que empeoran más?
Esperaría más costo en agregaciones con `GROUP BY` sobre categorías amplias y en consultas que ordenan resultados completos antes de aplicar `LIMIT`, especialmente si además usan columnas con muchos valores nulos.
