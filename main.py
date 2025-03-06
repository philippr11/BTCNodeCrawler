import os
import logging
from blockchain.iterator import iterate_block_files
from blockchain.parser import parse_block

# Konfiguration - you can define the path to your block data here
BLOCK_FOLDER = "/pfad/zu/deinen/blockdaten"  # later on on the Node #TODO: change this to the actual path

# Simple logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    for file_name, block_data in iterate_block_files(BLOCK_FOLDER):
        logger.info(f"Verarbeite Blockdatei: {file_name}")
        block_info = parse_block(block_data)
        if block_info:
            logger.info(f"Block {block_info['block_number']} hat {len(block_info['transactions'])} Transaktionen.")
            # in here we can add the code to process the transactions to the database for example
            for tx in block_info["transactions"]:
                logger.info(f"Adresse: {tx['address']} - Betrag: {tx['amount']}")
        else:
            logger.warning("Fehler beim Parsen des Blocks.")

if __name__ == "__main__":
    main()
