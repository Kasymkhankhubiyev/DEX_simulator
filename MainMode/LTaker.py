from typing import NamedTuple


class History(NamedTuple):
    wallet_balance_usd: float
    wallet_balance_quote: float
    wallet_balance_base: float
    transaction_type: int
    transuction_cost: float


class LTaker:
    def __init__(self, wallet_data, quote_price_usd, base_price_usd) -> None:
        self.wallet = wallet_data # must be assets
        self.initial_balance_usd = quote_price_usd * wallet_data[list(wallet_data.keys())[0]] + base_price_usd * wallet_data[list(wallet_data.keys())[1]]
        self.history = [History(wallet_balance_base=wallet_data[list(wallet_data.keys())[0]],
                                wallet_balance_quote=wallet_data[list(wallet_data.keys())[1]],
                                transaction_type=0,
                                transuction_cost=0,
                                wallet_balance_usd = quote_price_usd * wallet_data[list(wallet_data.keys())[0]] + base_price_usd * wallet_data[list(wallet_data.keys())[1]])
                                ]
        self.pnl = None

    def send_order(self) -> None:
        pass

    def get_pnl(self)-> 'list[History]':
        return self.history

    def get_wallet(self) -> dict:
        pass

    def get_asset_num(self, asset_name: str) -> float:
        return self.wallet[asset_name]

    def make_transaction(self, asset_name, exchange_tocken, amount, 
                    transaction_type, transaction_cost,
                    asset_price_usd, base_price_usd) -> bool:
        """
        """
        if transaction_type == 1:
            asset_amount = self.wallet[asset_name]
            if asset_amount >= amount:
                self.wallet[asset_name] = asset_amount - amount
                self.wallet[exchange_tocken] += transaction_cost
                self.history.append(History(wallet_balance_base=self.wallet[exchange_tocken],
                                wallet_balance_quote=self.wallet[asset_name],
                                transaction_type=transaction_type,
                                transuction_cost=transaction_cost,
                                wallet_balance_usd=asset_price_usd*self.wallet[asset_name] + base_price_usd * self.wallet[exchange_tocken]))
                
                return True
            else:
                return False
        elif transaction_type == -1:
            cash_available = self.wallet[exchange_tocken]
            if cash_available >= transaction_cost:
                self.wallet[asset_name] += amount
                self.wallet[exchange_tocken] -= transaction_cost
                self.history.append(History(wallet_balance_base=self.wallet[exchange_tocken],
                                wallet_balance_quote=self.wallet[asset_name],
                                transaction_type=transaction_type,
                                transuction_cost=transaction_cost,
                                wallet_balance_usd=asset_price_usd*self.wallet[asset_name] + base_price_usd * self.wallet[exchange_tocken]))
                return True
            else:
                return False
            

    def __str__(self) -> str:
        output_str =  f"wallet balance: \n"
        output_str += f"{list(self.wallet.keys())[0]}: {self.wallet[list(self.wallet.keys())[0]]}\n" 
        output_str += f"{list(self.wallet.keys())[-1]}: {self.wallet[list(self.wallet.keys())[-1]]}\n"

        return output_str
