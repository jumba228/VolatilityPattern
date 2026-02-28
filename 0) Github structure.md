volatility-4point-regime/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── configs/
│   ├── base.yaml
│   ├── exp_kmeans.yaml
│   ├── exp_hdbscan.yaml
│   └── exp_sensitivity.yaml
│
├── docs/
│   ├── 01_problem_definition.md
│   ├── 02_methodology.md
│   ├── 03_hypotheses.md
│   ├── 04_metrics_and_validation.md
│   ├── 05_experiment_protocol.md
│   └── decision_log.md
│
├── data/
│   ├── raw/              # ignored
│   ├── interim/          # ignored
│   ├── processed/        # ignored
│   └── sample/
│       └── sample_btc_1h.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_visualization.ipynb
│   ├── 03_clustering_experiment.ipynb
│   └── 04_robustness_analysis.ipynb
│
├── experiments/
│   ├── exp_001_kmeans/
│   │   ├── config.yaml
│   │   └── results.json
│   ├── exp_002_hdbscan/
│   │   ├── config.yaml
│   │   └── results.json
│   └── summary.csv
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── loader.py
│   │
│   ├── zigzag/
│   │   ├── __init__.py
│   │   └── detector.py
│   │
│   ├── features/
│   │   ├── __init__.py
│   │   └── builder.py
│   │
│   ├── clustering/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── kmeans.py
│   │   ├── hdbscan.py
│   │   └── stability.py
│   │
│   ├── validation/
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── statistical_tests.py
│   │   └── temporal_split.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── transition_matrix.py
│   │
│   └── pipeline.py
│
└── tests/
    ├── test_zigzag.py
    ├── test_features.py
    ├── test_clustering.py
    └── test_validation.py