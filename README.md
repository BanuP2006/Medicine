# Clinical Medicine & Health Informatics Toolkit (`medkit`)

[![CI](https://github.com/medtech-oss/clinical-medicine-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A production-ready, open-source Python toolkit for clinical decision support, standardized medical risk scores, early warning metrics (NEWS2), and structured medical knowledge evaluation.

---

## 📋 Features

- **Evidence-Based Clinical Calculators**:
  - **eGFR (CKD-EPI 2021)**: Estimated Glomerular Filtration Rate without race coefficient.
  - **CHA₂DS₂-VASc**: Stroke risk stratification in non-valvular atrial fibrillation.
  - **CURB-65**: Community-acquired pneumonia mortality risk assessment.
  - **NEWS2 (National Early Warning Score 2)**: Standardized acute physiological deterioration detection.
  - **Wells Score**: Pulmonary Embolism & Deep Vein Thrombosis probability index.
- **Medical Assessment Engine**:
  - Multiple True/False (MTF / 5-stem MCQs) scoring with per-question floor handling.
  - Single Best Answer (SBA) validation and performance reporting.
- **Clinical Reference Ranges**:
  - Comprehensive adult normal laboratory reference intervals in SI and conventional units.
- **CI/CD Ready**: Includes GitHub Actions for linting, testing, and automated type checks.

---

## 🚀 Quick Start

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/clinical-medicine-toolkit.git
cd clinical-medicine-toolkit
pip install -r requirements.txt
pip install -e .
```

### Basic Usage

```python
from medkit.calculators import calculate_cha2ds2_vasc, calculate_news2, calculate_egfr_ckdepi

# 1. Calculate CHA2DS2-VASc score
cha2ds2_res = calculate_cha2ds2_vasc(
    age=72,
    sex="female",
    congestive_heart_failure=True,
    hypertension=True,
    stroke_tia_thromboembolism=False,
    vascular_disease=True,
    diabetes=True
)
print(f"Score: {cha2ds2_res['score']}, Annual Stroke Risk: {cha2ds2_res['stroke_risk_percent']}%")
print(f"Recommendation: {cha2ds2_res['recommendation']}")

# 2. National Early Warning Score 2 (NEWS2)
news_res = calculate_news2(
    respiratory_rate=24,
    oxygen_saturation=93,
    on_supplemental_oxygen=True,
    systolic_bp=98,
    heart_rate=115,
    consciousness="Alert",
    temperature=38.6
)
print(f"NEWS2 Score: {news_res['score']} | Risk Level: {news_res['risk_category']}")
print(f"Clinical Action: {news_res['clinical_response']}")
```

---

## 📂 Project Structure

```text
clinical-medicine-toolkit/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions automated test & lint pipeline
├── medkit/
│   ├── __init__.py
│   ├── calculators/           # Validated clinical formulas & scoring algorithms
│   │   ├── __init__.py
│   │   ├── cardiology.py      # CHA2DS2-VASc, Wells PE/DVT
│   │   ├── nephrology.py      # CKD-EPI 2021 eGFR
│   │   ├── respiratory.py     # CURB-65
│   │   └── critical_care.py   # NEWS2 (Royal College of Physicians)
│   ├── assessment/            # Educational scoring & testing engines
│   │   ├── __init__.py
│   │   └── exam_evaluator.py  # MCQ & SBA grading engine
│   └── data/
│       ├── __init__.py
│       └── lab_reference.json # Normal clinical laboratory reference intervals
├── tests/                     # Unit test suite with clinical test vectors
│   ├── test_calculators.py
│   └── test_assessment.py
├── examples/
│   └── full_clinical_demo.py  # End-to-end runnable demonstration
├── .gitignore
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧪 Running Tests

Run the test suite using `pytest`:

```bash
pytest tests/ -v
```

---

## ⚠️ Medical Disclaimer

This software is designed for academic, educational, and clinical research purposes only. It should not be used as the sole basis for clinical decision-making or direct patient care without verification by licensed healthcare practitioners.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
