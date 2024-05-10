import tkinter as tk
from tkinter import messagebox
import os
from eth_keys import keys
from eth_utils import keccak
import bech32
import mainscreen
import walletaction

def generate_ethereum_keys():
    priv_key_bytes = keccak(os.urandom(32))
    priv_key = keys.PrivateKey(priv_key_bytes)
    pub_key = priv_key.public_key
    eth_address = pub_key.to_checksum_address()
    return priv_key, eth_address

def eth_to_mx_address(eth_address):
    addr_hex = eth_address.lower().replace('0x', '')
    addr_bytes = bytes.fromhex(addr_hex)
    data = bech32.convertbits(addr_bytes, 8, 5)
    if data is None:
        raise ValueError("Error in converting bits.")
    mx_address = bech32.bech32_encode('mx', data)
    return mx_address

def create_new_wallet(root):
    mainscreen.clear_content(root)
    frame = tk.Frame(root, bg='black')
    frame.pack(fill='both', expand=True)

    logo = tk.PhotoImage(file="logo.png")
    logo_label = tk.Label(frame, image=logo, bg='black')
    logo_label.image = logo
    logo_label.pack(pady=(20, 0))

    developer_info_label = tk.Label(frame, text="This application is developed by Coinsspor", font=('Arial', 10), bg='black', fg='white')
    developer_info_label.pack(pady=(0, 20))

    priv_key, eth_address = generate_ethereum_keys()
    mx_address = eth_to_mx_address(eth_address)

    # Global değişkenlere cüzdan bilgilerini ve private key'i aktar
    walletaction.mx_address = mx_address
    walletaction.evm_address = eth_address
    walletaction.private_key = priv_key.to_hex()

    # Label styles
    label_style = {'font': ('Arial', 12), 'bg': 'black', 'fg': 'white', 'anchor': 'center'}
    title_style = {**label_style, 'font': ('Arial', 12, 'bold', 'underline')}

    # Private Key
    tk.Label(frame, text="Private Key:", **{**title_style, 'fg': 'blue'}).pack(fill='x')
    tk.Label(frame, text=priv_key.to_hex(), **label_style).pack(fill='x')

    # EVM Address
    tk.Label(frame, text="EVM Address:", **{**title_style, 'fg': 'green'}).pack(fill='x')
    tk.Label(frame, text=eth_address, **label_style).pack(fill='x')

    # MX Address
    tk.Label(frame, text="MX Address:", **{**title_style, 'fg': 'orange'}).pack(fill='x')
    tk.Label(frame, text=mx_address, **label_style).pack(fill='x')

    # Buttons
    copy_button = tk.Button(frame, text="Copy Information", bg='#1E90FF', fg='white', font=('Arial', 14, 'bold'), command=lambda: copy_info(root, priv_key, eth_address, mx_address))
    copy_button.pack(fill='x', pady=10)

    back_button = tk.Button(frame, text="Back", bg='#1E90FF', fg='white', font=('Arial', 14, 'bold'), command=lambda: mainscreen.show_main_screen(root))
    back_button.pack(side='left', fill='x', expand=True, padx=20, pady=20)

   
    next_button = tk.Button(frame, text="Next", bg='#1E90FF', fg='white', font=('Arial', 14, 'bold'), command=lambda: walletaction.wallet_actions(root, eth_address, mx_address, priv_key.to_hex()))

    #next_button = tk.Button(frame, text="Next", bg='#1E90FF', fg='white', font=('Arial', 14, 'bold'), command=lambda: walletaction.wallet_actions(root))
    next_button.pack(side='right', fill='x', expand=True, padx=20, pady=20)

def copy_info(root, priv_key, eth_address, mx_address):
    info_text = f"Private Key: {priv_key.to_hex()}\nEVM Address: {eth_address}\nMX Address: {mx_address}"
    root.clipboard_clear()
    root.clipboard_append(info_text)
    messagebox.showinfo("Copied", "Wallet information copied to clipboard!")
