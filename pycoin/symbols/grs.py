from pycoin.coins.groestlcoin.hash import groestlHash
from pycoin.coins.groestlcoin.parse import GRSParseAPI
from pycoin.coins.groestlcoin.uiclass import GroestlcoinUI
from pycoin.coins.groestlcoin.Block import Block as GrsBlock
from pycoin.coins.groestlcoin.Tx import Tx as GrsTx
from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    symbol="GRS", network_name="Groestlcoin", subnet_name="mainnet", tx=GrsTx, block=GrsBlock,
    wif_prefix_hex="80", sec_prefix="GRSSEC:", address_prefix_hex="24", pay_to_script_prefix_hex="05",
    bip32_prv_prefix_hex="0488ade4", bip32_pub_prefix_hex="0488B21E", bech32_hrp="grs",
    magic_header_hex="F9BEB4D9", default_port=1331,
    ui_class=GroestlcoinUI,
    parse_api_class=GRSParseAPI,
    dns_bootstrap=[
        "groestlcoin.org", "electrum1.groestlcoin.org", "electrum2.groestlcoin.org",
        "jswallet.groestlcoin.org", "groestlsight.groestlcoin.org"
    ]
)

# Cause parsing to fail and tests to skip.
try:
    import groestlcoin_hash
except ImportError:
    network.Key = None
    none_parser = lambda *args, **kwargs: None
    for attr in "hierarchical_key private_key public_key address".split():
        setattr(network.parse, attr, none_parser)