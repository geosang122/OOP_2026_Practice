# OOP 2026 Practice

Python Object-Oriented Programming 실습 저장소

## 교재

[Python Object-Oriented Programming, 4th Edition (Packt)](https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition)

## 구조

```
OOP_2026_Practice/
├── docs/              # 설치 가이드 등 문서
├── tests/             # 환경 검증 테스트
├── ch_01/             # Chapter 1 실습
│   ├── src/
│   └── tests/
├── ch_02/             # Chapter 2 실습
│   ├── src/
│   └── tests/
└── ...
```

## 환경 설정

[설치 가이드](docs/setup_guide.md)를 참고하세요.

```bash
conda create -n OOP python=3.9 -y
conda activate OOP
conda install beautifulsoup4 pytest pillow -y
pip install tox
```

## 환경 검증

```bash
python tests/test_setup.py
```
