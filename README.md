# Simulated Order Matching Engine

### The Simulated Order Matching Engine is a Python-based system that provides a simulated environment for understanding and illustrating the process of order matching in financial markets. It is designed to replicate the core functionality of a real order matching engine, allowing users to explore and experiment with order matching algorithms and market dynamics.

## Key Features:
- Simulated order matching: Replicates the order matching process in financial markets, allowing users to observe how buy and sell orders are matched based on price and quantity.
- Customisable market scenarios: Enables users to define various market scenarios with different order types, quantities, and prices to study and analyse the behaviour of the order matching engine.
- Real-time feedback: Provides real-time feedback on order execution, trade matching, and order book updates, allowing users to visualise the dynamics of the simulated market.
- Educational tool: Serves as an educational tool for traders, developers, and enthusiasts to gain practical insights into the order matching process and develop a better understanding of trading systems.

This repository contains the source code for the Simulated Order Matching Engine. It includes the core order matching algorithms, order book management, and a user-friendly interface for interacting with the simulated market. The code is well-documented and includes sample scenarios to help users get started quickly.

Whether you're a beginner looking to learn about order matching or an experienced trader seeking to experiment with different trading strategies, the Simulated Order Matching Engine provides a valuable tool for studying and visualizing the inner workings of order matching in financial markets.

*Note: This simulated order matching engine is intended for educational and illustrative purposes only and should not be used for live trading or production environments.*

## Step-by-step instructions to run the Simulated Order Matching Engine:

1. Open a terminal.
1. Navigate to the directory where you want to clone the Git repository.
1. Clone the repository by running the following command:
1. Copy
`git clone <repository_url>`
Replace <repository_url> with the actual URL of the Git repository.
1. Change into the cloned repository's directory:
`cd order-matching-engine`
1. Create a virtual environment (optional but recommended)

    - Run:
`python -m venv venv`
    - If you have conda installed, run:
`conda create --name venv`
    - Activate the virtual environment:
    - For venv, run:
        - On macOS/Linux:
`source venv/bin/activate`
        - On Windows:
`.\venv\Scripts\activate`
        - For conda, run:
`conda activate venv`
1. Install the required dependencies:
`pip install -r requirements.txt`
1. Open two separate terminals.
1. In Terminal 1, run the order_server.py file:
`python order_server.py`
This will start the server for order processing.
1. In Terminal 2, run the order_client.py file:
`python order_client.py`
This will start the client interface for interacting with the simulated order matching engine.

Now, you can use the order_client.py interface to send buy and sell orders to the order matching engine. The order_server.py will process the orders and perform order matching within the simulated environment.

Please ensure that you have Python 3.x installed and that the required dependencies are successfully installed in the virtual environment or globally.

*Note: If you encounter any issues during the installation or execution process, double-check that you have followed all the steps correctly and that your system meets the necessary requirements.*