import random

class GemRandom:
    def gen_rand_str(length: int, with_special_sybols: bool) -> str:
        with_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
        without_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        if with_special_sybols:
            return ''.join(random.choice(with_symbols) for i in range(length))
        else:
            return ''.join(random.choice(without_symbols) for i in range(length))