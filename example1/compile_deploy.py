import json
from web3 import Web3, RPCProvider
from solc import compile_source
import time

RPC_IP = '127.0.0.1'
RPC_PORT = '8545'
GAS = 410000

# Read the Smart Contract's file data
with open('hello.sol', 'r') as f:
	data = f.read()

# Compiling the Smart Contract
contract_compiled = compile_source(data)
print('Contract is compiled')

# Contract interface
contract_interface = contract_compiled.get('<stdin>:Hello')

# Open connection to the RPC server
w3 = Web3(RPCProvider(RPC_IP, RPC_PORT))
print('RPC connection to the blockchain node opened at: http://{0}:{1}'.format(RPC_IP, RPC_PORT))

# Create the contract
contract = w3.eth.contract(abi=contract_interface.get('abi'), bytecode=contract_interface.get('bin'))
print('Contract created')

# Get the transaction Hash of the deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': GAS})
print('''Contract deployed:
transaction hash: {0}
from account: {1} / Gas used: {2}'''.format(tx_hash, w3.eth.accounts[0], GAS))

# Wait untill the transaction will be mined! otherwise tx_receipt will be None
while w3.eth.getTransactionReceipt(tx_hash) is None:
	print('Waiting the transaction: {0} to be mined'.format(tx_hash))
	time.sleep(1)


# Get the contract transaction informations
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
# Get the contract address after mining it
contract_address = tx_receipt.get('contractAddress')

# Name of the file in which we'll have contract ABI and contract address
contract_informations_name = 'contract_informations.json'

with open(contract_informations_name, 'w') as f:
	f.write(json.dumps({
		'abi': contract_interface.get('abi'),
		'contract_address': contract_address
		}))
print('Contract information saved in: {0}'.format(contract_informations_name))

