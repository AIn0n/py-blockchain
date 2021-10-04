from blockchain import Block, BlockChain, BlockNode
import rsa

class Transaction:
	def __init__(self, sellerPk, buyerPk, homeNum) -> None:
		# simple transaction construction
		pass


	def sign(self, sk) -> None:
		# create rsa signature in transaction
		pass

	def verify(self) -> bool:
		# verify signature
		pass
	def __repr__(self) -> str:
		# ez printing
		pass

def checkMarket(bc :BlockChain) -> dict:
	# verify and check data in blockchain
	pass

def mineBlock(bc :BlockChain, data :tuple) -> None:
	# mine block with some proper proof-of-work-like alghoritm
	pass

agents = [rsa.newkeys(512) for n in range(5)]

(ownerPk, ownerSk) = rsa.newkeys(512)
genesisData = []
for num, keyPair in enumerate(agents):
	tx = Transaction(ownerPk, keyPair[0], num)
	tx.sign(ownerSk)
	genesisData.append(tx)

bc = BlockChain(tuple(genesisData))
tx = Transaction(agents[0][0], agents[1][0], 0)
tx.sign(agents[0][1])
for k, v in checkMarket(bc).items():
	print(f'house number = {k}, receiver = {v}')
mineBlock(bc, tuple([tx]))
print('transaction mined!')
for k, v in checkMarket(bc).items():
	print(f'house number = {k}, receiver = {v}')