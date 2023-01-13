from Crypto.Cipher import AES
import hashlib

class message_decryption:
	def __init__(self):
		self.password=input('Enter password to decrypt : ')
	def decrypt_message(self,message):
		
		password=self.password.encode()
		key=hashlib.sha256(password).digest()
		mode=AES.MODE_CBC
		IV='This is an IV456'
		cipher = AES.new(key, mode ,IV)
		decrypted_message = cipher.decrypt(message)
		return decrypted_message
	

