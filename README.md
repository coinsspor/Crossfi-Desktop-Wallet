![image](https://github.com/coinsspor/Crossfi-Desktop-Wallet/assets/38142283/4353504c-bc52-4b3e-b633-4fec91b0ce85)

**"Crossfi Desktop Wallet"**. This desktop application facilitates MPX transfers and delegation transactions on the Crossfi network, as well as XFI transfers on the EVM network. Users can quickly generate new wallet addresses or log in with existing wallets. Now, let’s briefly review what the files in your project do:

**main.py:** This is the main entry point of the application. It initiates the application and loads the main screen.

**mainscreen.py:** Defines the main user interface (GUI). This screen offers users various options, such as creating a new wallet, logging in with an existing wallet, and performing transfer operations.

**delegate.py:** Performs delegation transactions on the Crossfi network. It enables the user to send tokens to the validator they wish to delegate to.

**evmtransfer.py:** Manages XFI token transfers on the EVM network. This script provides the functionality needed for transfer operations on Ethereum-like networks.

**login_prvtkey.py:** Allows users to log into their existing wallets using their private keys. This file may also include security measures.

**newwallet.py:** Creates a new wallet. This script presents the user with the new wallet’s private key and address by generating them.

**transfer.py:** Manages transfer operations for MPX and other tokens. It enables users to perform token transfers on the Crossfi network.

**walletaction.py:** Manages wallet operations and interacts with the user interface. This script presents various wallet functions (such as transfers, displaying wallet information) to the user.

We have created a list of all the dependencies necessary for our project to function. These dependencies will be included in our GitHub repo as a requirements.txt file. With this file, other users cloning our project will be able to easily install all the required packages with a single command:

`pip install -r requirements.txt`

This list will greatly simplify the setup process for your project and allow anyone who wants to start using the project to quickly install it. If you need to make corrections to this list of dependencies or have additional requirements specific to your project, do not hesitate to update this list. If you need help on how to add your dependencies to the requirements.txt file, please let me know. I am always happy to help.

In our project, we have used the Mospy library. This library offers functions that allow us to easily perform various operations on the Cosmos network. Thanks to the tools provided by the library, our project's development process has become more efficient and effective.

I would like to thank ctrl-Felix and his team for developing the Mospy library and sharing this resource with the community. The functionalities provided by the library have made our project more comprehensive and useful.

I recommend our users to visit the Mospy GitHub page to learn more about the Mospy library and how they can use it in their own projects.

