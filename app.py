from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

import bitcoinwallet
import ethereumwallet
import walletsSQL

app = Flask(__name__)
api = Api(app)

app.secret_key = "Secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3031/walletservice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class CreateWallet(Resource):
    def get(self, blockchain):
        return 'Hello World'

    def put(self, blockchain):
        global json_to_return
        email = request.form['email']
        if blockchain == 'bitcoin':
            # Create Bitcoin Wallet
            new_wallet = bitcoinwallet.create_wallet()

            # Insert the wallet into the DB
            walletsSQL.insert_bitcoin_wallet(email, new_wallet[0], new_wallet[2])

            json_to_return = {'private_key': new_wallet[0], 'address': new_wallet[0]}
            print('Wild BITCOIN WALLET appeared!')

        if blockchain == 'ethereum':
            # Create Ethereum Wallet
            new_wallet = ethereumwallet.create_wallet()
            address = new_wallet[0]
            key = new_wallet[1]
            # Insert the wallet into the DB
            walletsSQL.insert_ethereum_wallet(email, address, key)

            json_to_return = {'private_key': key, 'address': address}
            print('Wild ETHEREUM WALLET appeared!')

        print(json_to_return)
        return json_to_return


api.add_resource(CreateWallet, '/createwallet/<string:blockchain>')

if __name__ == '__main__':
    app.run(port=3030, debug=True)
