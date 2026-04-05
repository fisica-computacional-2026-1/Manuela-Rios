# W06B Run Log

## Comando
```bash
python -m src.pipeline.w06b_runner
```

## Stdout (corrida 1)
```text
W06B runner completed
- silver: 0.7987 s (rc=0)
- dims: 0.6121 s (rc=0)
- gold: 0.3268 s (rc=0)
- export: 0.2813 s (rc=0)
report=/home/manuela-rios/Documentos/Física computacional/Manuela-Rios/artifacts/w06b_run_report.json
timings=/home/manuela-rios/Documentos/Física computacional/Manuela-Rios/artifacts/w06b_stage_timings.csv
```

## Stdout (corrida 2)
```text
W06B runner completed
- silver: 0.3084 s (rc=0)
- dims: 0.4514 s (rc=0)
- gold: 0.2528 s (rc=0)
- export: 0.3025 s (rc=0)
report=/home/manuela-rios/Documentos/Física computacional/Manuela-Rios/artifacts/w06b_run_report.json
timings=/home/manuela-rios/Documentos/Física computacional/Manuela-Rios/artifacts/w06b_stage_timings.csv
```

## Interpretación
En la primera corrida, la etapa más lenta fue `silver` con `0.7987 s`. En la segunda corrida, la etapa más lenta fue `dims` con `0.4514 s`, aunque la diferencia con `silver` ya fue mucho menor.

Los tiempos cambian entre una corrida y otra porque la primera ejecución suele pagar más costo de lectura inicial, creación de objetos y calentamiento del entorno. En la segunda, parte del trabajo ya queda más “caliente” en caché del sistema o del motor, por eso varias etapas bajan de tiempo.
