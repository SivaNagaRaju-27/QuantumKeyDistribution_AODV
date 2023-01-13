import blowfish_algo as blowfish
import base64



def encrypt_msg(msg):
    cipher = blowfish.Cipher(b'3523497845738')
    msg = str.encode(msg)
    cipher_text = b"".join(cipher.encrypt_ecb_cts(msg))
    cipher_text = base64.b64encode(cipher_text)
    return cipher_text.decode('utf-8')

def decrypt_msg(msg):
    cipher = blowfish.Cipher(b'3523497845738')
    msg = str.encode(msg)
    cipher_text = base64.b64decode(msg)
    plain_text = b"".join(cipher.decrypt_ecb_cts(cipher_text))
    return plain_text.decode('utf-8')
