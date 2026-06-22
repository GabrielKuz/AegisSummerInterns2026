from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).encryptor
decrypted_padded_data =decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
plaintext_decrypted = unpadder.update(decrypted_padded_data) + unpadder.finalize()

print(f"Decrypted Plaintext: {plaintext_decrypted.decode()}")