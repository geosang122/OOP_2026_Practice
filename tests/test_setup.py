"""
환경 검증 테스트 스크립트

사용법:
    python tests/test_setup.py          # 직접 실행
    pytest tests/test_setup.py -v       # pytest로 실행
"""

import sys


def test_python_version():
    """Python 버전이 3.9 이상인지 확인"""
    assert sys.version_info >= (3, 9), (
        f"Python 3.9 이상이 필요합니다. 현재 버전: {sys.version}"
    )


def test_import_pytest():
    """pytest 패키지 import 확인"""
    import pytest  # noqa: F401


def test_import_bs4():
    """beautifulsoup4 (bs4) 패키지 import 확인"""
    import bs4  # noqa: F401


def test_import_pillow():
    """Pillow (PIL) 패키지 import 확인"""
    from PIL import Image  # noqa: F401


def test_oop_basics():
    """간단한 OOP 클래스 생성 및 동작 확인"""

    class Greeter:
        def __init__(self, name: str):
            self.name = name

        def greet(self) -> str:
            return f"Hello, {self.name}!"

    obj = Greeter("OOP")
    assert obj.name == "OOP"
    assert obj.greet() == "Hello, OOP!"
    assert isinstance(obj, Greeter)


# --- 직접 실행 시 결과 출력 ---

_TESTS = [
    ("Python 버전 (>= 3.9)", test_python_version),
    ("import pytest", test_import_pytest),
    ("import bs4", test_import_bs4),
    ("import PIL (Pillow)", test_import_pillow),
    ("OOP 클래스 기본 동작", test_oop_basics),
]


def main():
    print("=" * 50)
    print(" 환경 검증 테스트")
    print("=" * 50)
    print(f"Python: {sys.version}")
    print("-" * 50)

    passed = 0
    failed = 0

    for name, func in _TESTS:
        try:
            func()
            print(f"  [PASS] {name}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {name}")
            print(f"         -> {e}")
            failed += 1

    print("-" * 50)
    print(f"결과: {passed} passed, {failed} failed")
    if failed == 0:
        print("환경 구성이 완료되었습니다!")
    else:
        print("위 FAIL 항목을 확인하고 설치 가이드를 참고하세요.")
    print("=" * 50)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
