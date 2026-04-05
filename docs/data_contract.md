# Data Contract

## Datasets
- `silver_planet`
- `dim_host_sk`
- `fact_planet_sk`
- `gold_by_discoverymethod`
- `gold_by_host`

## Grain
- `dim_host_sk`: 1 fila por `hostname`
- `fact_planet_sk`: 1 fila por `pl_name`

## Keys
- PK dimensión: `host_id`
- UNIQUE dimensión: `hostname`
- PK fact: `pl_name`
- FK: `fact_planet_sk.host_id -> dim_host_sk.host_id`

## Checks mínimos
- Unicidad dimensión: `COUNT(*) == COUNT(DISTINCT hostname)`
- Conteo dimensión actual: `4537 == 4537`
- Huérfanos: `orphan_rows == 0`
- Resultado actual de huérfanos: `0`

## Consistencia del modelo
- `dim_host_sk` contiene una surrogate key entera para cada host.
- `fact_planet_sk` referencia hosts mediante `host_id`, no por `hostname`.
- Las vistas Gold se construyen a partir de este modelo relacional mínimo.
