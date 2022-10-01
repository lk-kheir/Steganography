from PIL import Image
from numpy import asarray


alpha = list("abcdefghijklmnopqrstuvwxyz")


def shift_letters(text, n, mode='encrypt'):
    if n > 26:
        n %= 26
    new_text = ""
    for c in text:
        if c.isalpha():
            c = alpha[(alpha.index(c) + n) % 26] if mode == 'encrypt' else alpha[(alpha.index(c) - n) % 26]
        new_text += c
    return list(new_text)


def img_to_matrix(img_path):
    img = Image.open(img_path)
    return asarray(img)


def encrypt(info):
    k = len(info)
    alpha_letters_shifted = shift_letters(info, k)
    nums = []
    for i in range(k):
        nums.append(alpha.index(alpha_letters_shifted[i]))

    return nums

