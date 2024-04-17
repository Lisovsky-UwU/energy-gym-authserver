import hashlib


PASS_SECRET = 'seKs8whzkKyKnkvVzNe9RVCTxIskXSE6Le5'


def generate_hash(payload: str) -> str:
    return hashlib.sha256(payload.encode()).hexdigest()


def generate_hid(student_card: int, password: str) -> str:
    return generate_hash(
        f'{PASS_SECRET}{student_card}{password}{PASS_SECRET}'
    )
