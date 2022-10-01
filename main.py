from PIL import Image
from numpy import asarray
ALPHABITIC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def img_to_matrix(img_path):
    img = Image.open(img_path)
    return asarray(img)

def encrypt(info):
    k = len(info)
    alpha_letters_shifted = rightRotate(ALPHABITIC , k)
    print(alpha_letters_shifted)
    letter_to_nums = []

    for i in range(len(info)):
        letter_to_nums.append(alpha_letters_shifted.index(info[i]))
    print(letter_to_nums)

    return letter_to_nums


def rightRotate(lists, num):
    output_list = []
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list

encrypt("abc")
