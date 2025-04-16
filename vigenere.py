def generate_key(message: str, keyword: str) -> str:
    """
    Menyesuaikan panjang keyword agar sama dengan panjang pesan.
    """
    keyword = list(keyword)
    if len(message) == len(keyword):
        return "".join(keyword)
    else:
        for i in range(len(message) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)

def encrypt_vigenere(plain_text: str, keyword: str) -> str:
    """
    Mengenkripsi plain_text menggunakan Vigenère Cipher dan keyword.
    Hanya huruf alfabet yang dienkripsi.
    """
    encrypted_text = []
    key = generate_key(plain_text, keyword)

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            if plain_text[i].isupper():
                encrypted_char = chr((ord(plain_text[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(plain_text[i]) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(plain_text[i])

    return "".join(encrypted_text)

# Contoh penggunaan
message = "saya thirza asli sumatra selatan"
keyword = "bumi sriwijaya"
encrypted = encrypt_vigenere(message, keyword)
print("Pesan asli     :", message)
print("Keyword        :", keyword)
print("Hasil enkripsi :", encrypted)
