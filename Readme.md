# Solana Copy Trading Bot

This project is a Solana copy trading bot that allows users to replicate trades executed by a specified account on the Solana blockchain. The bot fetches trading data using the Bitquery API and executes corresponding trades using the `solana-py` library.

## Features

- Fetches trade data from Solana using the Bitquery API.
- Executes trades based on the fetched data.
- Interacts with the Solana blockchain using the `solana-py` library.
- Supports trading on decentralized exchanges (DEXs) on the Solana network.

## Prerequisites

- Python 3.7 or higher
- Node.js and npm (for setting up the JS version)
- Solana CLI (for interacting with the Solana blockchain)
- A Solana wallet with funds for trading

## Installation

1. **Clone the Repository**

    ```bash
        git clone https://github.com/your-username/solana-copy-trading-bot.git
        cd solana-copy-trading-bot
    ```
2. **Install the dependencies**
    ```bash
        pip install -r requirements.txt
    ```

## Running the script

To run the bot enter the following command

    ```bash
        python3 main.py
    ```

## Contributions

Currently the project does not execute any trade, but if you want a complete bot that executes trade you can look up to use SDKs like solana-py or web3-py.

You can also share a good trade execution code by opening a PR.