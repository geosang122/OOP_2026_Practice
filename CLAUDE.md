# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Python OOP educational practice repository based on **"Python Object-Oriented Programming, 4th Edition"** (Packt Publishing).
Textbook source: https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition

## Environment Setup

- **Conda environment**: `OOP`
- **Python**: 3.9
- **Key dependencies**: pytest, beautifulsoup4 (bs4), Pillow (PIL), tox

```bash
conda activate OOP
```

## Commands

```bash
# Run all tests
pytest -v

# Run environment verification
pytest tests/test_setup.py -v
# or
python tests/test_setup.py

# Run tests for a specific chapter
pytest ch_XX/tests/ -v
```

## Architecture

Chapter-based layout — each chapter has its own `src/` and `tests/` directories:

```
OOP_2026_Practice/
├── CLAUDE.md
├── README.md
├── docs/              # 설치 가이드 등 문서
├── tests/             # 환경 검증 테스트 (프로젝트 전체)
├── ch_01/
│   ├── src/           # Chapter 1 실습 코드
│   └── tests/         # Chapter 1 테스트
├── ch_02/
│   ├── src/
│   └── tests/
└── ...
```

## Conventions

- **Language**: Korean comments and docstrings are used throughout the codebase
- When writing new code or tests, follow the existing Korean documentation style
- Test files use standard pytest conventions (`test_*.py`)
