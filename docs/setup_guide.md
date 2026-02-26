# Python OOP 실습 환경 설치 가이드

> Windows 11 + VSCode 1.107 기준

---

## Step 1: Miniconda 설치 및 가상환경 생성

Miniconda를 설치하면 Python이 함께 포함되므로, Python을 별도로 설치할 필요가 없습니다.

1. [anaconda.com/download](https://www.anaconda.com/download) 에서 **Miniconda Windows 64-bit** 설치 파일을 다운로드합니다.
2. 설치를 진행합니다 (기본 옵션 유지).
3. **Anaconda Prompt** (시작 메뉴에서 검색)를 열고 가상환경을 생성합니다:

```bash
conda create -n OOP python=3.9 -y
```

4. 가상환경을 활성화합니다:

```bash
conda activate OOP
```

프롬프트 앞에 `(OOP)`가 표시되면 성공입니다.

---

## Step 2: VSCode 설치 및 확장 프로그램

1. [code.visualstudio.com](https://code.visualstudio.com/) 에서 **VSCode** 를 다운로드하여 설치합니다.
2. VSCode를 실행한 후, 왼쪽 사이드바의 **확장(Extensions)** 아이콘(네모 4개 모양)을 클릭합니다.
3. 다음 확장 프로그램을 검색하여 설치합니다:
   - **Python** (Microsoft) — Python 언어 지원
   - **Pylance** (Microsoft) — 코드 자동완성 및 타입 검사

---

## Step 3: VSCode에서 conda 인터프리터 선택

1. VSCode에서 `Ctrl + Shift + P`를 눌러 명령 팔레트를 엽니다.
2. **"Python: Select Interpreter"** 를 입력하고 선택합니다.
3. 목록에서 `Python 3.9.x ('OOP': conda)` 항목을 선택합니다.
4. 하단 상태 표시줄에 선택한 인터프리터가 표시되는지 확인합니다.

> 목록에 보이지 않으면 "Enter interpreter path"를 선택하고 conda 환경 경로를 직접 입력합니다:
> `C:\Users\<사용자명>\miniconda3\envs\OOP\python.exe`

---

## Step 4: 교재 저장소 clone 및 의존성 설치

1. VSCode에서 터미널을 엽니다 (`Ctrl + ~`).
2. 작업 디렉토리로 이동한 후 저장소를 clone합니다:

```bash
git clone https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition.git
```

3. conda 가상환경이 활성화된 상태에서 필수 패키지를 설치합니다:

```bash
conda activate OOP
conda install beautifulsoup4 pytest pillow -y
python -m pip install tox
```

---

## Step 5: 환경 검증

테스트 스크립트를 실행하여 환경이 올바르게 구성되었는지 확인합니다:

```bash
# 직접 실행
python tests/test_setup.py

# 또는 pytest로 실행
pytest tests/test_setup.py -v
```

모든 항목이 **PASS**로 표시되면 환경 구성이 완료된 것입니다.

---

## 문제 해결

| 증상 | 해결 방법 |
|------|-----------|
| `python`이 인식되지 않음 | Anaconda Prompt에서 `conda activate OOP` 후 실행 |
| `conda`가 인식되지 않음 | Anaconda Prompt 사용 또는 시스템 PATH에 conda 경로 추가 |
| VSCode에서 인터프리터가 안 보임 | VSCode 재시작 후 다시 시도 |
| `import pytest` 실패 | `conda activate OOP` 후 `conda install pytest -y` |
