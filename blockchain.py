class Block:
	def __init__(self, prevHash, data) -> None:
		# what is stored in single block?
		pass

	def genHash(self) -> None:
		# how do we generate hash?
		pass

class BlockNode:
	def __init__(self, block, parent) -> None:
		# what is going on into single tree / blockchain node
		pass

	def __repr__(self) -> str:
		# easy printing
		pass

class BlockChain:
	def __init__(self, genesisData) -> None:
		# how do we create single blockchain
		pass

	def searchByHash(self, hash :int) -> BlockNode:
		# search node by it's hash
		pass		

	def addBlock(self, block :Block) -> None:
		# add new block to blockchain
		pass
	def __repr__(self) -> str:
		# ez printing
		pass

	def getAll(self) -> list:
		# get every node from tree
		pass
	def getMaxHeightBlock(self) -> Block:
		# get block with max height
		pass

if __name__ == '__main__':
	# test some functionality
	pass