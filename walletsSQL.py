from app import db


class Wallet(db.Model):
    __tablename__ = 'wallets'

    address = db.Column(db.String(256), primary_key=True)
    email = db.Column(db.String(256))
    pk = db.Column(db.String(256))
    blockchain = db.Column(db.String(256))


db.create_all()


def insert_bitcoin_wallet(email, private_key, address):
    try:
        table_row = Wallet(address=address, email=email, pk=private_key, blockchain="bitcoin")
        db.session.add(table_row)
        db.session.commit()
        print("Wallet Bitcoin added into database" + address)
        return True
    except Exception as e:
        print("Problem inserting bitcoin wallet into db: " + str(e))
        return False


def insert_ethereum_wallet(email, address, key):
    try:
        table_row = Wallet(address=address, email=email, pk=key, blockchain="ethereum")
        db.session.add(table_row)
        db.session.commit()
        print("Wallet Bitcoin added into database")
        return True
    except Exception as e:
        print("Problem inserting ethereum wallet into db: " + str(e))
        return False
