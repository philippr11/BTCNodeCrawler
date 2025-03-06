from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BitcoinAddress(Base):
    __tablename__ = 'bitcoin_addresses'

    id = Column(Integer, primary_key=True)
    address = Column(String(100), unique=True, nullable=False)
    balance = Column(Numeric, nullable=False, default=0)
    tx_count = Column(Integer, nullable=False, default=0)
    first_activity = Column(Integer)  # Blockhight of first Activity onchain
    last_activity = Column(Integer)   # Blockhight of last Activity onchain
    total_received = Column(Numeric, nullable=False, default=0)
    total_sent = Column(Numeric, nullable=False, default=0)
    net_volume = Column(Numeric, nullable=False, default=0)  # total_received - total_sent
    address_type = Column(String(20))  # z.B. 'P2PKH', 'P2SH', 'Bech32'
    owner = Column(String(100))        # z.B. 'Binance', 'Kraken'; NULL, if unknown

    def __repr__(self):
        return f"<BitcoinAddress(address='{self.address}', balance={self.balance})>"
