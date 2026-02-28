# Object-Oriented Programming 2026 (3168)

Python Object-Oriented Programming 수업 실습 저장소

## 교재

[Python Object-Oriented Programming, 4th Edition (Packt)](https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition)

## 환경 설정

설치 가이드를 참고하세요:

| OS | 한국어 | English |
|----|--------|---------|
| Windows | [설치 가이드](docs/setup_guide.md) | [Setup Guide](docs/setup_guide_en.md) |
| macOS | [설치 가이드](docs/setup_guide_macos.md) | [Setup Guide](docs/setup_guide_macos_en.md) |

### 빠른 시작

```bash
conda create -n OOP python=3.9 -y
conda activate OOP
conda install beautifulsoup4 pytest pillow ipykernel -y
pip install tox
python -m ipykernel install --user --name OOP --display-name "Python 3 (OOP)"
```

### 환경 검증

```bash
python tests/test_setup.py
```

## 프로젝트 구조

```
OOP_2026_Practice/
├── docs/              # 설치 가이드 등 문서
├── tests/             # 환경 검증 테스트
├── ch_01/             # Chapter 1 실습
│   ├── src/           # 실습 노트북 및 소스 코드
│   └── tests/
├── ch_02/             # Chapter 2 실습
│   ├── src/
│   └── tests/
└── ...
```
