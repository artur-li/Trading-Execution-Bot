import MetaTrader5 as mt5

class FXContractsCalculator:
    def __init__(self, symbol="EURUSD", sl=30, risk=0.01):
        """
        Initialize the FXContractsCalculator with default or provided parameters.
        """
        self.symbol = symbol
        self.sl = sl
        self.risk = risk
        self.balance = self.get_account_balance()

    def get_account_balance(self):
        """
        Retrieve the account balance from MetaTrader 5.
        """
        account = mt5.account_info()
        if account is None:
            print("Failed to retrieve account information. Exiting program.")
            exit()  # Exit the program if account information retrieval fails
        balance = account.balance
        return balance


    def risk_per_pip(self):
        """
        Calculate the risk per pip based on the account balance, stop loss, and risk percentage.
        """
        risk_per_pip = self.balance * self.risk / self.sl
        return risk_per_pip

    def contracts(self):
        """
        Calculate the total number of contracts to put on based on the risk per pip, pip value, and standard lot size.
        """
        symbol_info = mt5.symbol_info(self.symbol)
        if symbol_info is None:
            print(f"Symbol {self.symbol} not found")
            return None
        pip_value = symbol_info.trade_tick_value
        standard_lot_size = symbol_info.trade_contract_size 
        contracts_to_put_on = self.risk_per_pip() / pip_value * standard_lot_size
        return contracts_to_put_on
