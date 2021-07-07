from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from scalecodec.type_registry import load_type_registry_file
import time

substrate = SubstrateInterface(
    url='wss://ws.mof.sora.org',
    ss58_format=69,
    type_registry_preset='default',
    type_registry=load_type_registry_file('custom_types.json'),

)

keypair = Keypair.create_from_mnemonic('<your 12 word passphrase here>')

call = substrate.compose_call(
    call_module='LiquidityProxy',
    call_function='swap',
    call_params={
        'dex_id': '0',
        'input_asset_id': '0x0200050000000000000000000000000000000000000000000000000000000000',
        'output_asset_id': '0x0200000000000000000000000000000000000000000000000000000000000000',
        'swap_amount': {'WithDesiredInput': {'desired_amount_in': '13370000000000000000000', 'min_amount_out': '0'}},
        'selected_source_types': ["XYKPool","MulticollateralBondingCurvePool"],
        'filter_mode': 'AllowSelected'
    }
)

while True:

    try:
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)

    
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=False)
        print("Extrinsic '{}' sent".format(receipt.extrinsic_hash))
        # print("Extrinsic '{}' sent and included in block '{}'".format(receipt.extrinsic_hash, receipt.block_hash))

    except Exception as e:
        print("Failed to send: {}".format(e))

    time.sleep(100)


