import json

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

import bitcoinwallet
import ethereumwallet
import walletsSQL

app = Flask(__name__)
api = Api(app)

app.secret_key = "Secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@wallet-db:3031/walletservice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class GetWallets(Resource):
    def get(self, email):
        wallets = walletsSQL.get_wallets_by_email(email)
        result = []
        for wallet in wallets:
            result.append({"address": wallet.address, "pk": wallet.pk, "name": wallet.name})
        return result


class CreateWallet(Resource):
    def put(self, blockchain):
        global json_to_return, private_key, address
        email = request.form['email']
        name = request.form['name']
        if blockchain == 'bitcoin':
            # Create Bitcoin Wallet
            new_wallet = bitcoinwallet.create_wallet()
            private_key = new_wallet[0]
            address = new_wallet[1]
            # Insert the wallet into the DB
            walletsSQL.insert_bitcoin_wallet(email, private_key, address, name)
            print('Wild BITCOIN WALLET appeared!')

        if blockchain == 'ethereum':
            # Create Ethereum Wallet
            new_wallet = ethereumwallet.create_wallet()
            private_key = new_wallet[0]
            address = new_wallet[1]
            # Insert the wallet into the DB
            walletsSQL.insert_ethereum_wallet(email, private_key, address, name)
            print('Wild ETHEREUM WALLET appeared!')

        json_to_return = {'private_key': private_key, 'address': address, 'name': name, 'email': email}
        return json_to_return, 201


api.add_resource(CreateWallet, '/api/wallet/createwallet/<string:blockchain>')
api.add_resource(GetWallets, '/api/wallet/<string:email>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
