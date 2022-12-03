from typing import List
from pyteal import *
import base64
import hashlib

def approval(
    owner_address: Expr,
    beneficiary_address: Expr,
    hashed_secret: Expr,
    unlock_at_round: Expr,):

    return Return(
        And(
            # check fee
            Txn.fee() <= Global.min_txn_fee() * Int(2),
            # check payment parameters
            Txn.type_enum() == TxnType.Payment,
            Txn.close_remainder_to() == Global.zero_address(),
            Txn.rekey_to() == Global.zero_address(),
            # check recipient
            Or(
                # beneficiary unlocks with secret key
                And(
                    Txn.receiver() == beneficiary_address,
                    Sha256(Arg(0)) == hashed_secret,
                ),
                # expiration time passes and funds return to owner
                And(
                    Txn.receiver() == owner_address,
                    Txn.first_valid() >= unlock_at_round,
                ),
            ),
        ),
    )


def create(args: List[str]) -> str:
    # from pyteal_helpers.hash import sha256b64

    owner_address = Addr(args[0])
    beneficiary_address = Addr(args[1])
    hashed_secret = Bytes("base64", sha256b64(args[2]))
    unlock_at_round = Int(int(args[3]))

    return approval(
        owner_address,
        beneficiary_address,
        hashed_secret,
        unlock_at_round,
    )
def sha256b64(s: str) -> str:
    return base64.b64encode(hashlib.sha256(str(s).encode("utf-8")).digest()).decode("utf-8")

# if __name__ == "__main__":
#     app = create(["V7UA4EK7YT3GDY7GPXC4EDB6Z2ETUEKMU52F2PQTUA3C7VSGNIOJEJCR3Y",\
#         "PNATILPEKI5NCL6N5SAHFBQR76SERK3ZB6TBSU2K3RZU3QAZB5VBIR6AIU", "password",\
#             "3"])
#     print(app)