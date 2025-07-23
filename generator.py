import random
import string


def random_name(length: int) -> str:
    return ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(length)])
