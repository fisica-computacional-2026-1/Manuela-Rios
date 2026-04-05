# W01A Run

## Entorno
- Proyecto: `Manuela-Rios`
- Base de datos: `data/exoplanets.duckdb`
- Archivo raw utilizado: `data/raw/pscomppars.csv`

## Evidencia de carga
- `n_rows = 6087`
- `n_cols = 16`

## Resultado general
Se creó la vista `raw_ps` desde el CSV y se confirmó que el dataset puede consultarse desde DuckDB. También se verificó que el archivo fuente queda identificado de manera trazable mediante hash SHA-256.

## Nota
El objetivo de esta corrida fue dejar una base reproducible para las prácticas posteriores de SQL, calidad y modelado.
