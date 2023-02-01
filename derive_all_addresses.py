from blspy import AugSchemeMPL
from chia.consensus.coinbase import create_puzzlehash_for_pk
from chia.util.bech32m import encode_puzzle_hash
from chia.util.keychain import mnemonic_to_seed

from chia.wallet.derive_keys import (
    master_sk_to_wallet_sk_intermediate,
    master_sk_to_wallet_sk_unhardened_intermediate,
    _derive_path,
    _derive_path_unhardened,
)

#Parameters
mnemonic = 'your mnemonic words here'
prefix = 'xch'
derivation_amount = 500

seed = mnemonic_to_seed(mnemonic, '')
key = AugSchemeMPL.key_gen(seed)

intermediate_n = master_sk_to_wallet_sk_intermediate(key)
intermediate_o = master_sk_to_wallet_sk_unhardened_intermediate(key)

non_observer_addresses = [None] * derivation_amount
observer_addresses = [None] * derivation_amount

for i, address in enumerate(non_observer_addresses):
    non_observer_addresses[i] = encode_puzzle_hash(
        create_puzzlehash_for_pk(_derive_path(intermediate_n, [i]).get_g1()),
        prefix
    )

for i, address in enumerate(observer_addresses):
    observer_addresses[i] = encode_puzzle_hash(
        #Observer addresses are also known as unhardened addresses.
        create_puzzlehash_for_pk(_derive_path_unhardened(intermediate_o, [i]).get_g1()),
        prefix
    )

#Classic/Non-Observer Addresses
for i, address in enumerate(non_observer_addresses):
    print(f"Non-Observer Address #{i + 1}: #{address}") 

print('')

#Modern/Observer Addresses/Unhardened
for i, address in enumerate(observer_addresses):
    print(f"Observer Address #{i + 1}: #{address}")