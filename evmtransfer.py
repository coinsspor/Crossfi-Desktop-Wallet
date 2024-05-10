from web3 import Web3, exceptions

def evm_transfer(private_key, to_address, amount_xfi):
    crossfi_rpc_url = 'https://rpc.testnet.ms/'
    web3 = Web3(Web3.HTTPProvider(crossfi_rpc_url))

    if not web3.is_connected():
        return "Connection failed. Check the URL."

    account = web3.eth.account.from_key(private_key)
    nonce = web3.eth.get_transaction_count(account.address)

    # Yeterli bakiye kontrolü
    balance = web3.eth.get_balance(account.address)
    amount = web3.to_wei(amount_xfi, 'ether')
    if balance < amount:
        return "Insufficient balance to perform the transaction."

    try:
        # Gaz fiyatını ve gaz limitini otomatik ayarla
        gas_price = web3.eth.gas_price
        estimated_gas = web3.eth.estimate_gas({
            'from': account.address,
            'to': to_address,
            'value': amount
        })

        tx = {
            'chainId': 4157,
            'nonce': nonce,
            'to': to_address,
            'value': amount,
            'gas': estimated_gas,
            'gasPrice': gas_price
        }

        # İşlemi imzala ve gönder
        signed_tx = account.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return f"Transaction successful: {web3.to_hex(tx_hash)}"
    except exceptions.TransactionNotFound as e:
        return f"Transaction failed: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
