from PIL import Image
from numpy import asarray
import numpy as np


alpha = list("abcdefghijklmnopqrstuvwxyz")


def shift_letters(text, n, mode='encrypt'):
    if n > 26:
        n %= 26
    new_text = ""
    for c in text:
        c = c.lower()
        if c.isalpha():
            c = alpha[(alpha.index(c) + n) % 26] if mode == 'encrypt' else alpha[(alpha.index(c) - n) % 26]
        new_text += c
    return list(new_text)


def img_to_matrix(img_path):
    img = Image.open(img_path)
    return asarray(img)


def matrix_to_img(matrix, img_path):
    img = Image.fromarray(matrix)
    img.save(img_path)
    img.show()


def print_matrix(matrix):
    h, w, s = np.shape(matrix)
    for i in range(h):
        print()
        for j in range(w):
            print(" | ", end='')
            for k in range(s):
                print(matrix[i][j][k], end=' ')
        print(" | ")


def encrypt(info):
    k = len(info)
    alpha_letters_shifted = shift_letters(info, k)
    nums = []
    for i in range(k):
        nums.append(alpha.index(alpha_letters_shifted[i]))
    return nums


def hide(matrix, nums):
    print(nums)
    print(np.shape(matrix))
    # print_matrix(img_matrix)

    m = np.copy(matrix)
    h, w, s = np.shape(matrix)
    k = 0
    rgb = 0
    for i in range(h):
        for j in range(w):
            if k >= len(nums):
                break
            # if rgb >= 3:
            #     rgb = 0
            m[i, j, rgb] = nums[k]
            k += 1
            # rgb += 1
    # print_matrix(m)
    matrix_to_img(m, './new.png')


hide(img_to_matrix("test.png"), encrypt("".join("Helloworldatestinganewstringblablabla" for i in range(3))))
