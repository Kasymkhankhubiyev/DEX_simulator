class LTaker:
    def __init__(self, wallet_data) -> None:
        self.wallet = wallet_data # must be assets
        self.history = []
        self.pnl = None

    def send_order(self) -> None:
        pass

    def get_pnl(self)->None:
        pass

    def get_wallet(self) -> dict:
        pass

    def get_asset_num(self, asset_name: str) -> float:
        return self.wallet[asset_name]

    def make_transaction(self, asset_name, exchange_tocken, amount, 
                    transaction_type, transaction_cost) -> bool:
        """
        """
        if transaction_type == 1:
            asset_amount = self.wallet[asset_name]
            if asset_amount >= amount:
                self.wallet[asset_name] = asset_amount - amount
                self.wallet[exchange_tocken] += transaction_cost
                return True
            else:
                return False
        elif transaction_type == -1:
            cash_available = self.wallet[exchange_tocken]
            if cash_available >= transaction_cost:
                self.wallet[asset_name] += amount
                self.wallet[exchange_tocken] -= transaction_cost
                return True
            else:
                return False
            

    def __str__(self) -> str:
        output_str =  f"wallet: \n"
        output_str += f"{list(self.wallet.keys())[0]}: {self.wallet[list(self.wallet.keys())[0]]}\n" 
        output_str += f"{list(self.wallet.keys())[-1]}: {self.wallet[list(self.wallet.keys())[-1]]}\n"

        return output_str
