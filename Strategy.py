from tigeropen.common.consts import Language
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.trade.trade_client import TradeClient
import ssl

huanqiu_id = 'U3313628'
tiger_id = '20151317'
biaozhun_id = '3204391'
moni_id = '20210612232234285'

def get_client_config():
    """ 获取client_config
    https://www.itiger.com/openapi/info 开发者信息获取
    """
    client_config = TigerOpenClientConfig(sandbox_debug=False)
    client_config.private_key = read_private_key(r'/Users/mjheng/rsa_private_key.pem')
    client_config.tiger_id = tiger_id
    client_config.account = huanqiu_id
    client_config.language = Language.en_US
    return client_config


client_config = get_client_config()
trade_client = TradeClient(client_config)
asset = trade_client.get_assets(segment = False,market_value=True)
accountprofile = trade_client.get_managed_accounts()
position = trade_client.get_positions()
# print(asset[0].market_values['USD'])
print(position[0])