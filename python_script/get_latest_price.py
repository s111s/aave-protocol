# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:06:54 2020

@author: Samos
"""

# AAVE BTC/USD Kovan: 0x2445F2466898565374167859Ae5e3a231e48BB41
# AAVE ETH/USD Kovan: 0xD21912D8762078598283B14cbA40Cb4bFCb87581
# AAVE DAI/USD Kovan: 0x35840b10A53226396b9c5bb0151404Cd305A8637
# AAVE LINK/USD Kovan: 0x326C977E6efc84E512bB9C30f76E30c160eD06FB
# AAVE LEND/ETH Kovan: 0xdCE38940264DfbC01aD1486c21764948e511947e
# AAVE MKR/ETH Kovan: 0x14D7714eC44F44ECD0098B39e642b246fB2c38D0
# AAVE USDC/ETH Kovan: 0x672c1C0d1130912D83664011E7960a42E8cA05D5
# AAVE USDT/ETH Kovan: 0xCC833A6522721B3252e7578c5BCAF65738B75Fc3

from web3 import Web3
web3 = Web3(Web3.HTTPProvider('<INFURA_KOVAN_RPC_URL or YOUR_KOVAN_RPC_URL>'))
abi = '[{"constant":false,"inputs":[{"name":"_requestId","type":"bytes32"},{"name":"_payment","type":"uint256"},{"name":"_expiration","type":"uint256"}],"name":"cancelRequest","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"authorizedRequesters","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"jobIds","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"latestAnswer","outputs":[{"name":"","type":"int256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minimumResponses","outputs":[{"name":"","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"oracles","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferLINK","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"latestRound","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clRequestId","type":"bytes32"},{"name":"_response","type":"int256"}],"name":"chainlinkCallback","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_paymentAmount","type":"uint128"},{"name":"_minimumResponses","type":"uint128"},{"name":"_oracles","type":"address[]"},{"name":"_jobIds","type":"bytes32[]"}],"name":"updateRequestDetails","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"latestTimestamp","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"destroy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_roundId","type":"uint256"}],"name":"getAnswer","outputs":[{"name":"","type":"int256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_roundId","type":"uint256"}],"name":"getTimestamp","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paymentAmount","outputs":[{"name":"","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"requestRateUpdate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_requester","type":"address"},{"name":"_allowed","type":"bool"}],"name":"setAuthorization","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_link","type":"address"},{"name":"_paymentAmount","type":"uint128"},{"name":"_minimumResponses","type":"uint128"},{"name":"_oracles","type":"address[]"},{"name":"_jobIds","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"response","type":"int256"},{"indexed":true,"name":"answerId","type":"uint256"},{"indexed":true,"name":"sender","type":"address"}],"name":"ResponseReceived","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"}],"name":"OwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"id","type":"bytes32"}],"name":"ChainlinkRequested","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"id","type":"bytes32"}],"name":"ChainlinkFulfilled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"id","type":"bytes32"}],"name":"ChainlinkCancelled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"current","type":"int256"},{"indexed":true,"name":"roundId","type":"uint256"},{"indexed":false,"name":"timestamp","type":"uint256"}],"name":"AnswerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"roundId","type":"uint256"},{"indexed":true,"name":"startedBy","type":"address"}],"name":"NewRound","type":"event"}]'
addr = '0x35840b10A53226396b9c5bb0151404Cd305A8637'
contract = web3.eth.contract(address=addr, abi=abi)

latestAnswer = contract.functions.latestAnswer().call()
lastestTimestamp = contract.functions.latestTimestamp().call()
latestRound = contract.functions.latestRound().call()

pricefeed = {
    0: {'pair': 'BTC/USD','address': '0x2445F2466898565374167859Ae5e3a231e48BB41'},
    1: {'pair': 'ETH/USD','address': '0xD21912D8762078598283B14cbA40Cb4bFCb87581'},
    2: {'pair': 'DAI/USD','address': '0x35840b10A53226396b9c5bb0151404Cd305A8637'},
    3: {'pair': 'LINK/USD','address': '0x326C977E6efc84E512bB9C30f76E30c160eD06FB'},
    4: {'pair': 'LEND/ETH','address': '0xdCE38940264DfbC01aD1486c21764948e511947e'},
    5: {'pair': 'MKR/ETH','address': '0x14D7714eC44F44ECD0098B39e642b246fB2c38D0'},
    6: {'pair': 'USDC/ETH','address': '0x672c1C0d1130912D83664011E7960a42E8cA05D5'},
    7: {'pair': 'USDT/ETH','address': '0xCC833A6522721B3252e7578c5BCAF65738B75Fc3'}
}

for i in range(8):
    addr = pricefeed[i]['address'];
    contract = web3.eth.contract(address=addr, abi=abi)
    latestAnswer = contract.functions.latestAnswer().call()
    print('Pair: ' + pricefeed[i]['pair'] + ', Price: ' + str(latestAnswer));