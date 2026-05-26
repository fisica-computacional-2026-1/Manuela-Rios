# W09 Quality Gates

## quality_events
Se creó la tabla `quality_events` con la estructura:
- `ts_utc`
- `check_name`
- `status`
- `metric_value`
- `details`

## Checks implementados
1. `null_hostname_canon`
   - Verifica filas donde `hostname_canon IS NULL`
2. `disc_year_bad_rows`
   - Cuenta filas marcadas con `disc_year_bad`
3. `null_discoverymethod_canon`
   - Revisa filas sin método canónico válido
4. `invalid_pl_rade_range`
   - Cuenta radios planetarios inválidos (`<= 0` o `> 30`)

## Propósito
Estos checks convierten supuestos de calidad en eventos consultables y dejan evidencia mínima para futuras corridas del pipeline.
