from bitcoin import *


def create_wallet():
    # Create Private Key
    private_key = random_key()

    # Create Public Key from Private Key
    public_key = privtopub(private_key)

    # Create Bitcoin Address from Public Key
    address = pubtoaddr(public_key)

    return [private_key, public_key, address]