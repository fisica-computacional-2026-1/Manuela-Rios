# Reflexión W04

## ¿Qué check te sorprendió más y por qué?
El check que más llama la atención es el de rangos sobre `sy_dist`, porque aunque no siempre se use en análisis introductorios, una distancia inválida puede contaminar filtros, comparaciones y perfiles de hosts sin que sea tan evidente como un valor nulo.

## ¿Qué consecuencias tendría para JOINs o vistas agregadas que `pl_name` o `hostname` tuviera muchos nulos o duplicados?
Si `pl_name` o `hostname` tuvieran muchos nulos o duplicados, el problema no sería solo de limpieza: también afectaría el grain esperado del modelo, rompería joins y volvería poco confiables las vistas agregadas. En otras palabras, la calidad de claves sigue siendo el cuello de botella silencioso de casi todo el pipeline.
