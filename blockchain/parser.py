import struct
import logging

logger = logging.getLogger(__name__)

def parse_block(block_data):
    """
    Simple Parser that extracts the block number and the transactions from a block.
    In this prototype, we assume that the block has the following simplified structure:
    - 4 Byte: Block number (integer)
    - Rest: Simple transaction list, where each transaction is structured as follows:
        - 34 Byte: Bitcoin address (ASCII, 34 characters)
        - 8 Byte: Amount (double, 8 bytes, big endian)

    Of course, this does not correspond to the real format of the Bitcoin blockchain,
    but it serves as an example of how one could proceed.

    """
    offset = 0
    # Read the block number (4 Byte, big endian)
    if len(block_data) < 4:
        logger.error("Blockdaten zu kurz, um eine Blocknummer zu enthalten.")
        return None

    block_number = struct.unpack(">I", block_data[offset:offset+4])[0]
    offset += 4

    transactions = []
    while offset + 42 <= len(block_data):
        # Read 34 Byte address (as string) and 8 Byte amount (double)
        address_bytes = block_data[offset:offset+34]
        address = address_bytes.decode('ascii', errors='ignore')
        offset += 34
        
        amount = struct.unpack(">d", block_data[offset:offset+8])[0]
        offset += 8

        transactions.append({
            "address": address.strip(),
            "amount": amount
        })
    
    return {
        "block_number": block_number,
        "transactions": transactions
    }
