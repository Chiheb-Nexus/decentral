# Initiez-vous avec les Dapps d'Ethereum

**Création d'environnement de travail:**
Dans cet example de Dapps d'Ethereum on va utiliser: [Python](https://www.python.org/), [Geth](https://geth.ethereum.org/downloads/), [web3.py](https://github.com/ethereum/web3.py) et [web3.js](https://github.com/ethereum/web3.js/).

- Installation de `Python`:
Il suffit d'installer le binaire de ce [lien](https://www.python.org/) et ajouter Python à votre viariable d'environnement si vous utiliser Windows. Sinon, généralement, Python est installé par défaut sur votre machine si vous utilisez Gnu\Linux, OS X et *BSD.

- Installation de `Geth`:
Il suffit d'installer Geth de ce [lien](https://geth.ethereum.org/downloads/) puis l'ajouter à votre viariable d'environnement.
Si vous utiliser une distribution basée sur Debian, faites ceci:
```bash
sudo nano ~/.bashrc
```
Puis à la fin du document, il suffi d'ajouter:
```bash
export PATH=$PATH:le_lien_du_dossier_Geth_dans_votre_système
```
Puis enregistrer et relancer une autre instance du terminal bash et vérifier:
```bash
geth version
```
Vous allez voir une résultat similaire à cella:
```bash
Geth
Version: 1.7.3-stable
Git Commit: 4bb3c89d44e372e6a9ab85a8be0c9345265c763a
Architecture: amd64
Protocol Versions: [63 62]
Network Id: 1
Go Version: go1.9.2
Operating System: linux
GOPATH=/home/chiheb/go
GOROOT=/usr/local/go
```

- Installation de `web3py`:
Nous allons utiliser `pip` le package manager de Python:
Tout d'abord vérifez si web3 est dans les dépôts de `pip`
```bash
pip search web3
```
Vous allez avoir une résultat similaire à :
```bash
rebecca (0.1)      - rebecca web3 framework.
web3 (4.0.0b6)     - Web3.py
web3utils (0.1.3)  - Convenience tools for web3.py
```
Ce qui nous intéresse est: `web3(4.0.0b6)` qui est la dernière version de `web3` présente dans les dépôts à ce jour (vous pouvez avoir une autre version tout dépend s'il y a une nouvelle version ou non). 
Donc, pour l'installer:

```bash
pip install web3
```
- Installation de `web3.js`:
Vous pouvez l'installer avec [npm](https://www.npmjs.com/package/web3) ou bien utiliser le framework [truffle](http://truffleframework.com/).

- Bonus:
Il existe aussi d'autres environnement de travail, tel l'utilisation des frameworks: [parity](https://www.parity.io/) ou [truffle](http://truffleframework.com/)

*NB*: Dans cet example on va utiliser `Python, Geth et web3.py`. Si, vous opter pour un autre environnement de travail, pensez à `Node.js, Geth et web3.js` ou bien `truffle et Geth` ou bien `Parity et web3.js`.

**Run the beast!:** 

L'exemple va se décomposer en trois parties:
- Création d'une chaîne privée du blockhain d'Ethereum
- Création, compilation et déploiement d'un Smart Contract
- Interaction avec le Smart Contract d'Ethereum

**1- Création d'une chaîne privée du blockchain d'Ethereum:**

Tout d'abord, on va créer un nouveau compte d'Ethereum:
```bash
geth account new
```

Vous allez avoir un message comme celui là:
```bash
Your new account is locked with a password. Please give a password. Do not forget this password.
Passphrase:
```
Entrez votre mot de passe, puis confirmez la et **assurez vous de ne pas l'oublier ! **

Vous allez avoir une réponse similaire à cella:
```bash
Your new account is locked with a password. Please give a password. Do not forget this password.
Passphrase: 
Repeat passphrase: 
Address: {53a4579eb6d5e48642fd2b4909fe3f762b1608b0}
```
Donc, notre nouveau compte a cette adresse d'ethereum: `0x53a4579eb6d5e48642fd2b4909fe3f762b1608b0` en Hexadécimal ou d'une manière simplifiée: `53a4579eb6d5e48642fd2b4909fe3f762b1608b0`.

Puis, on va créer notre propre chaîne privée du blockchain d'Ethereum. Nous aurons besoin de créer un `Genesis Block` dans la nouvelle blockchain. Voici un example de `Genesis Block`:

**customGenesisBlock.json**
```json
{
    "config": {
        "chainId": 13,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "1",
    "gasLimit": "2100000",
    "alloc": {
        "53a4579eb6d5e48642fd2b4909fe3f762b1608b0": { "balance": "1000000000000000000" }
    }
}
```
NB: Changer l'adresse d'Ethereum avec la votre et vous aurez un solde initial de `1000000000000000000 wei = 1 ether.`

Puis, placer vous dans le dossier où vous avez le fichier `customGenesisBlock.json` et créer la nouvelle blockchain avec le nouveau Genesis Block comme suit:

```bash
geth init custonGenesisBlock.json
```

Vous aurez une réponse comme suit:
```bash
INFO [01-20|15:47:08] Allocated cache and file handles         database=/home/user/.ethereum/geth/chaindata cache=16 handles=16
INFO [01-20|15:47:08] Writing custom genesis block 
INFO [01-20|15:47:08] Successfully wrote genesis state         database=chaindata                             hash=8718d6…f30d2a
INFO [01-20|15:47:08] Allocated cache and file handles         database=/home/user/.ethereum/geth/lightchaindata cache=16 handles=16
INFO [01-20|15:47:08] Writing custom genesis block 
INFO [01-20|15:47:08] Successfully wrote genesis state         database=lightchaindata                             hash=8718d6…f30d2a
```
PS: Si vous lisez bien le message du retour, les fichiers de configuration de notre compte Ethereum et les informations de la nouvelle blockchain privée sont enregistrées dans ce dossier: `/home/user/.ethereum`

Maintenant, on va miner quelques blocks dans notre nouvelle blockchain:

```bash
geth --rpc --rpcapi="db,eth,net,web3,personal" --maxpeers 0 --nodiscover --networkid 23 --unlock 53a4579eb6d5e48642fd2b4909fe3f762b1608b0 --mine
```

Vous allez avoir une réponse comme suit (vous devez entrer le mot de passe de votre compte Ethereum que vous avez créez tout au début de ce tutoriel):

```bash
INFO [01-20|16:13:55] Starting peer-to-peer node               instance=Geth/v1.7.3-stable-4bb3c89d/linux-amd64/go1.9.2
INFO [01-20|16:13:55] Allocated cache and file handles         database=/home/user.ethereum/geth/chaindata cache=128 handles=1024
INFO [01-20|16:13:55] Initialised chain configuration          config="{ChainID: 13 Homestead: 0 DAO: <nil> DAOSupport: false EIP150: <nil> EIP155: 0 EIP158: 0 Byzantium: <nil> Engine: unknown}"
INFO [01-20|16:13:55] Disk storage enabled for ethash caches   dir=/home/user/.ethereum/geth/ethash count=3
INFO [01-20|16:13:55] Disk storage enabled for ethash DAGs     dir=/home/user/.ethash               count=2
INFO [01-20|16:13:55] Initialising Ethereum protocol           versions="[63 62]" network=23
INFO [01-20|16:13:55] Loaded most recent local header          number=0 hash=8718d6…f30d2a td=1
INFO [01-20|16:13:55] Loaded most recent local full block      number=0 hash=8718d6…f30d2a td=1
INFO [01-20|16:13:55] Loaded most recent local fast block      number=0 hash=8718d6…f30d2a td=1
INFO [01-20|16:13:55] Loaded local transaction journal         transactions=0 dropped=0
INFO [01-20|16:13:55] Regenerated local transaction journal    transactions=0 accounts=0
INFO [01-20|16:13:55] Starting P2P networking 
INFO [01-20|16:13:55] RLPx listener up                         self="enode://d5e393f4a76bc6ad2aee398759bee8390701dca144c19d53ff355b96f93f531d0f1d0ea7972456617e071a0ec7fa52a5162ae17c19db48bf7f1ae2d648583b1b@[::]:30303?discport=0"
INFO [01-20|16:13:55] IPC endpoint opened: /home/user/.ethereum/geth.ipc 
INFO [01-20|16:13:55] HTTP endpoint opened: http://127.0.0.1:8545 
Unlocking account 53a4579eb6d5e48642fd2b4909fe3f762b1608b0 | Attempt 1/3
Passphrase: 
INFO [01-20|16:14:01] Unlocked account                         address=0x53A4579EB6D5e48642FD2b4909FE3f762b1608b0
INFO [01-20|16:14:01] Transaction pool price threshold updated price=18000000000
INFO [01-20|16:14:01] Starting mining operation 
INFO [01-20|16:14:01] Commit new mining work                   number=1 txs=0 uncles=0 elapsed=269.032µs
INFO [01-20|16:14:08] Generating ethash verification cache     epoch=1 percentage=2 elapsed=3.645s
INFO [01-20|16:14:13] Generating ethash verification cache     epoch=1 percentage=6 elapsed=8.842s
INFO [01-20|16:14:17] Generating ethash verification cache     epoch=1 percentage=12 elapsed=12.612s
INFO [01-20|16:14:21] Generating ethash verification cache     epoch=1 percentage=17 elapsed=17.032s
INFO [01-20|16:14:25] Generating ethash verification cache     epoch=1 percentage=23 elapsed=20.123s
INFO [01-20|16:14:29] Generating ethash verification cache     epoch=1 percentage=28 elapsed=24.786s
INFO [01-20|16:14:33] Generating ethash verification cache     epoch=1 percentage=33 elapsed=28.439s
INFO [01-20|16:14:37] Generating ethash verification cache     epoch=1 percentage=38 elapsed=32.869s
INFO [01-20|16:14:41] Generating ethash verification cache     epoch=1 percentage=40 elapsed=36.289s
```
Patientez un peu pour la génération des fichiers `ethash` et des fichiers `DAG`.

Vous allez avoir une réponse similaire à ceci:

```bash
INFO [01-20|16:27:45] 🔨 mined potential block                  number=4 hash=ba3f06…06469f
INFO [01-20|16:27:45] Commit new mining work                   number=5 txs=0 uncles=0 elapsed=212.925µs
INFO [01-20|16:27:48] Generating DAG in progress               epoch=1 percentage=7  elapsed=1m51.546s
INFO [01-20|16:27:51] Successfully sealed new block            number=5 hash=481bed…4aa188
INFO [01-20|16:27:51] 🔨 mined potential block                  number=5 hash=481bed…4aa188
INFO [01-20|16:27:51] Commit new mining work                   number=6 txs=0 uncles=0 elapsed=150.865µs
INFO [01-20|16:27:51] Successfully sealed new block            number=6 hash=5fba0d…66ea21
INFO [01-20|16:27:51] 🔗 block reached canonical chain          number=1 hash=76ad07…a73f55
INFO [01-20|16:27:51] 🔨 mined potential block                  number=6 hash=5fba0d…66ea21
INFO [01-20|16:27:51] Commit new mining work                   number=7 txs=0 uncles=0 elapsed=142.448µs

```
Ce qui signifie que vous avez miner quelques blocs et que ces blocks ont été validés et enregistrés dans notre blockchain privée.

Maintenant, quittons la console de minage en appuyant sur `CTRL+C` et entrons dans le développement de notre premier smart contract.

**2- Création, compilation et déploiement d'un Ethereum Smart Contract:**

Tout d'abord nous aurons besoin du compilateur `solc` qui va compiler notre Smart Contract, d'un noeud/Mineur de notre blockchain privée et des `ethers` qui seront le carburant de notre blockchain.

- Installation du compilateur `solc`:
Sur `Ubuntu` et théoriquement sur toutes les distributions basées sur `Ubuntu` il suffit de faire comme suit:
```bash
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc
```
Si vous utilisez une autre OS que Ubuntu, suivez les démarches sur ce lien de [documentation](http://solidity.readthedocs.io/en/develop/installing-solidity.html).

Puis, on va installer un wrapper sur Python qui va se charger de communiquer avec `solc` directement depuis la machine virtuelle de Python:

```bash
pip search solc
```
On aura:
```bash
isolcss (1.1.2)     - CSS isolator
py-solc (2.1.0)     - Python wrapper around the solc binary
pysolcache (1.0.1)  - pysolcache APIs
solcast (0.2.1)     - Client library for the Solcast API
```

On va installer `py-solc(2.1.0)` qui est la dernière version à ce jour:

```bash
pip install py-solc
```

- Un simple Smart Contract:

```solidity
pragma solidity ^0.4.0;

contract Hello {
	string public hello='Hello world!';

	function hello() public {
		hello;
	}

	function setString(string _myString) public {
		hello = _myString;
	}

	function getString() public returns (string) {
		return hello;
	}
}
```

- Notre script Python qui va compiler, déployer et interagir avec le smart contract

**compile_deploy.py**
```python
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
while w3.eth.getTransactionReceipt(tx_receipt) is None:
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

```

**interaction_with_contract.py**
```python
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

# Interaction with the contract
print(contract_instance.getString())
print(contract_instance.hello())
# Modify the hello variable in the smart contract
tx_hash = contract_instance.setString('Love Ethereum DAPPS!', transact={'from': w3.eth.accounts[0]})
print('Setting new string Done with transaction hash: {0}'.format(tx_hash))
# Wait untill the new transaction will be mined
time.sleep(10)
print(contract_instance.getString())
print(contract_instance.hello())
```

Ceci dit, exécuter `compile_deploy.py` en ouvrant Geth avec cette commande:

```bash
geth --rpc --rpcapi="db,eth,net,web3,personal" --maxpeers 0 --nodiscover --networkid 23 --unlock 53a4579eb6d5e48642fd2b4909fe3f762b1608b0 --mine
```

Puis:
 

```bash
python compile_deploy.py
```

On aura une réponse similaire à ceci:

```bash
Contract is compiled
RPC connection to the blockchain node opened at: http://127.0.0.1:8545
Contract created
Contract deployed:
transaction hash: 0x690a8aa45ed29ff121b1573699320fd3328cdccac8b0cbbeb1f4208050001b3b
from account: 0x53A4579EB6D5e48642FD2b4909FE3f762b1608b0 / Gas used: 410000
Waiting the transaction: 0x690a8aa45ed29ff121b1573699320fd3328cdccac8b0cbbeb1f4208050001b3b to be mined
Waiting the transaction: 0x690a8aa45ed29ff121b1573699320fd3328cdccac8b0cbbeb1f4208050001b3b to be mined
Contract information saved in: contract_informations.json

```

Et on va remarquer que dans la console où `Geth` exécute les tâches de minage, on trouvera une information simaile à ceci:

```bash
INFO [01-20|20:02:56] 🔨 mined potential block                  number=907 hash=f0d47b…218789
INFO [01-20|20:02:56] Commit new mining work                   number=908 txs=0 uncles=0 elapsed=164.527µs
INFO [01-20|20:02:56] Submitted transaction                    fullhash=0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 recipient=0x3206E08918715a6F0368337ca477ee0D0cB4b72F
INFO [01-20|20:03:00] Successfully sealed new block            number=908 hash=687c2a…187462
INFO [01-20|20:03:00] 🔗 block reached canonical chain          number=903 hash=c5957e…5723a6
INFO [01-20|20:03:00] 🔨 mined potential block                  number=908 hash=6
```
Ceci dit, notre contract à été bien déployé et il sera miné dans le prochain bloc si le gas utilisé dans la transaction est assez suffisant pour la miner dans les plus bref délais.

Puis, si on exécute `interaction_with_contract.py`:

```bash
python interaction_with_contract.py
```
On aura comme résultat:

```bash
Hello world!
Hello world!
Setting new string Done with transaction hash: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764
Waiting the transaction: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 to be mined
Waiting the transaction: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 to be mined
Waiting the transaction: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 to be mined
Waiting the transaction: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 to be mined
Waiting the transaction: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 to be mined
Waiting the transaction: 0xa5c100ea33545aa0de973ec6cff75782c59d6cfbf7d92483bccba0c1bdd9d764 to be mined
Love Ethereum DAPPS!
Love Ethereum DAPPS!

```

Donc, au final, on a crée un `Smart Contract` avec le langage de programmation des smart contract d'Ethereum nommé `Solidity`. On a pu créer notre propre blockchain privée avec `Geth`. On a pu compiler et deployer le smart contract avec `solc` qui est le compilateur de solidity qu'Ethereum propose et on pu interagir avec les composants qu'Ethereum propose avec le wrapper de `solc` qui est `py-solc`, un wrapper de `web3.js` nommé `web3.py` et on a, au final, interagit avec le smart contract lui même avec les fonctions définis dans son code.

À la prochaine pour un prochain tutoriel et pour plus de perspectives de développement.

**Pour plus d'informations:**

- [ethereum.org](https://www.ethereum.org/) 
- [web3.py - Github](https://github.com/ethereum/web3.py) et [web3.py - Documentation](http://web3py.readthedocs.io/en/stable/quickstart.html)
- [web3.js - Github](https://github.com/ethereum/web3.js/) et [web3.js - Documentation](https://web3js.readthedocs.io/en/latest/)
- [Truffle - Smart Contract framework](http://truffleframework.com/)
- [Geth](https://geth.ethereum.org/downloads/)
- [parity.io](https://www.parity.io/)






