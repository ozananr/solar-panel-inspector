# Solar Panel Inspector

End-to-end computer vision system for detecting defective solar cells in electroluminescence (EL) images of photovoltaic modules.

> **Status:** Work in progress

## Overview

Solar Panel Inspector takes an EL image of a solar panel, splits it into individual cells using classical computer vision, predicts a defect probability for each cell with a deep learning model, and returns an inspection report with a defect heatmap.

## Planned features

- Panel preprocessing pipeline (grid detection, perspective correction, cell extraction)
- Cell-level defect classification with a fine-tuned CNN exported to ONNX
- Asynchronous inspection jobs with status tracking
- Inspection reports with defect heatmaps
- JWT authentication and inspection history
- Containerized deployment with CI/CD

## Tech stack

- **API:** FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Alembic
- **Computer vision & ML:** OpenCV, PyTorch, ONNX Runtime
- **Tooling:** uv, Ruff, mypy, pytest, pre-commit
- **Infrastructure:** Docker, GitHub Actions, cloud deployment

## Getting started

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- Git

### Installation

```bash
git clone git@github.com:ozananr/solar-panel-inspector.git
cd solar-panel-inspector
uv sync
uv run pre-commit install
```

## Dataset

This project uses the [ELPV dataset](https://github.com/zae-bayern/elpv-dataset) by Buerhop-Lutz et al., licensed under CC BY-NC-SA 4.0. The dataset is not included in this repository.

## License

The source code is licensed under the MIT License. See [LICENSE](LICENSE). The dataset is subject to its own license.
