import uuid


def generate_email():
    return f"qa_diplom_{uuid.uuid4().hex}@yandex.ru"