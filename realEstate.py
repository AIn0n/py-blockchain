from blockchain import BlockChain
import rsa

class Transaction:
	def __init__(self, sellerPk, buyerPk, homeNum) -> None:
		self.seller = sellerPk
		self.receiver = buyerPk
		self.num = homeNum
		self.signature = None

	def sign(self, sk) -> None:
		encoded = f'{self.seller}{self.receiver}{self.num}'.encode()
		self.signature = rsa.sign(encoded, sk, 'SHA-1')
	
	def verify(self) -> bool:
		encoded = f'{self.seller}{self.receiver}{self.num}'.encode()
		return rsa.verify(encoded, self.signature, self.seller)

	def __repr__(self) -> str:
	    return f'from {self.seller} to {self.receiver}\nhouse number = {self.num}\n'

numbersAndKeys = [rsa.newkeys(512) for n in range(5)]

(ownerPk, ownerSk) = rsa.newkeys(512)
genesisData = []
for num, keyPair in enumerate(numbersAndKeys):
	tx = Transaction(ownerPk, keyPair[0], num)
	tx.sign(ownerSk)
	genesisData.append(tx)

bc = BlockChain(tuple(genesisData))
print(bc)