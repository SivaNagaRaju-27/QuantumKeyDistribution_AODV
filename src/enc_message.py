from Crypto.Cipher import AES
import hashlib


class message_encryption:
	def __init__(self):
		self.password=input('Enter a 16 bit password: ').encode()
		self.key=hashlib.sha256(self.password).digest()
		
	
	def mes_encrypt(self,org_file):
		org_file = org_file + ' '*((16-len(org_file)%16)%16)
		mode=AES.MODE_CBC
		IV='This is an IV456'
		cipher = AES.new(self.key, mode ,IV)
		encrypted_message = cipher.encrypt(org_file)	
		return encrypted_message

e_msg = message_encryption()
print(e_msg.mes_encrypt('/home/wrogn/Desktop/AODV/Src/dec_message.py'))

