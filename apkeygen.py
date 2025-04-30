import hashlib
import random
import os


def get_md5_hash(input_str: str) -> bytes:
    return hashlib.md5(input_str.encode('utf-8')).digest()


def generate_unlimited_serial_number():
    text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    array = [
        4, 29, 7, 0, 15, 3, 33, 17, 13, 5, 12, 0, 19, 29, 11, 23, 9, 35, 17, 1,
        12, 33, 4, 13, 0, 30, 11, 32, 17, 10
    ]

    random_seed = str(random.randint(0, 99999))
    md5_hash = get_md5_hash(random_seed)

    serial_parts = []
    for j in range(30):
        num = md5_hash[j] if j <= 15 else md5_hash[30 - j] + j
        index = (array[j] + num) % len(text)
        serial_parts.append(text[index])
        if (j + 1) % 5 == 0 and j != 29:
            serial_parts.append('-')

    return ''.join(serial_parts)


def print_colored_serial_box(serial):
    green = "\033[92m"
    reset = "\033[0m"
    box_width = len(serial) + 4
    print(f"{green}{'╔' + '═' * box_width + '╗'}")
    print(f"║  {serial}  ║")
    print(f"{'╚' + '═' * box_width + '╝'}{reset}")


if __name__ == "__main__":
    os.system('')
    print("AntiPlagiarism.NET Keygen")
    print("==========================================")
    print("By: r3df3d  →  https://github.com/r3df3d\n")

    serial = generate_unlimited_serial_number()
    print_colored_serial_box(serial)