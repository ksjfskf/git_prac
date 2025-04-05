

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

enc_world = []
dec_world = []
original_text = input("Enter the Character to Encrypt the data \n").lower()
shift = int(input("type the shift number \n"))
def encrypt(original_text):
        global letter_char
        for i in original_text:
            get_index = alphabet.index(i)
            add_shift_value = (get_index + shift) % 26
            letter_char = alphabet[add_shift_value]
            enc_world.append(letter_char)
            print(letter_char)
encrypt(original_text)
left_shift = int(input("type the left number \n"))
def decrypt(original_text):
    global left_letter_char
    for j in original_text:
        get_index_new = alphabet.index(j)
        add_left_shift_value = (get_index_new - left_shift) % 26
        left_letter_char = alphabet[add_left_shift_value]
        dec_world.append(left_letter_char)
        print(left_letter_char)
decrypt(original_text)
print(enc_world)
print(dec_world)





