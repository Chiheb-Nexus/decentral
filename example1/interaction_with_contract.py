import json
from web3 import Web3, RPCProvider
from web3.contract import ConciseContract
import time

RPC_IP = '127.0.0.1'
RPC_PORT = '8545'

# read the contract informations then convert them into a Python dict
with open('contract_informations.json', 'r') as f:
	data = json.loads(f.read())

ABI = data.get('abi')
CONTARCT_ADDRESS = data.get('contract_address')

w3 = Web3(RPCProvider(RPC_IP, RPC_PORT))

# Read the contract in ConciseContract mode which is a Read only access
contract_instance = w3.eth.contract(ABI, CONTARCT_ADDRESS, ContractFactoryClass=ConciseContract)
print(contract_instance.getString())
print(contract_instance.hello())
tx_hash = contract_instance.setString('Love Ethereum DAPPS!', transact={'from': w3.eth.accounts[0]})
print('Setting new string Done with transaction hash: {0}'.format(tx_hash))
time.sleep(10)
print(contract_instance.getString())
print(contract_instance.hello())

