from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import subprocess
import sys
import time


def run_stage(mode: str, project_root: Path) -> tuple[float, str, str, int]:
    cmd = [sys.executable, '-m', 'src.pipeline.w07_pipeline', '--project-root', str(project_root), '--mode', mode]
    t0 = time.perf_counter()
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(project_root))
    dt = time.perf_counter() - t0
    return dt, res.stdout, res.stderr, res.returncode


def main() -> int:
    project_root = Path(__file__).resolve().parents[2]
    artifacts = project_root / 'artifacts'
    artifacts.mkdir(parents=True, exist_ok=True)

    stages = []
    stage_logs = []
    for mode in ['silver', 'dims', 'gold', 'export']:
        seconds, stdout, stderr, rc = run_stage(mode, project_root)
        stages.append({'mode': mode, 'seconds': round(seconds, 4), 'returncode': rc})
        stage_logs.append({'mode': mode, 'stdout': stdout, 'stderr': stderr})
        if rc != 0:
            print(stdout)
            print(stderr, file=sys.stderr)
            raise SystemExit(rc)

    report = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'runner': 'src.pipeline.w07b_runner',
        'pipeline_module': 'src.pipeline.w07_pipeline',
        'stages': stages,
        'counts': {
            'n_stages': len(stages),
            'n_failed': sum(1 for s in stages if s['returncode'] != 0),
        },
        'artifacts': [
            'artifacts/w07b_run_report.json',
            'artifacts/w07b_stage_timings.csv',
            'artifacts/gold_by_discoverymethod.csv',
            'artifacts/gold_by_host.csv',
        ],
    }

    (artifacts / 'w07b_run_report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    with (artifacts / 'w07b_stage_timings.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['mode', 'seconds', 'returncode'])
        w.writeheader()
        w.writerows(stages)

    print('W07B runner completed')
    for s in stages:
        print(f"- {s['mode']}: {s['seconds']} s (rc={s['returncode']})")
    print(f"report={artifacts / 'w07b_run_report.json'}")
    print(f"timings={artifacts / 'w07b_stage_timings.csv'}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
