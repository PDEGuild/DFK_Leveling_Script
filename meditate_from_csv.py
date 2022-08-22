import logging
from web3 import Web3
import csv
import config
import sys
import time
import meditation.meditation as meditation

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-meditation")
    logger.setLevel(logging.WARNING)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://rpc.ankr.com/harmony'
    logger.info("Using RPC server " + rpc_server)

    private_key = config.private  # set private key
    account_address = '0x60ad07d0263ad20B434Be351C507f0c11dd54C14'
    gas_price_gwei = 120
    tx_timeout_seconds = 30
    w3 = Web3(Web3.HTTPProvider(rpc_server))

    active_meditations = meditation.get_active_meditations(account_address, rpc_server)
    logger.info("Pending meditation on address " + str(account_address) + ": "+str(active_meditations))

# example heroes_to_level.csv format:
#
# hero_id,level,stat_1,_stat_2,stat_3
# 78375,8,luck,agility,vitality
# 281581,8,vitality,wisdom,luck
# 


# In Part 1, we start meditation for all heroes in the csv file. 
# In Part 2, we complete meditation.

    with open('heroes_to_level.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            csv_hero_id = row['hero_id']
            csv_level = row['level']
            stat_1 = row['stat_1']
            stat_2 = row['stat_2']
            stat_3 = row['stat_3']
            level_convered_to_int = int(row['level'])  # convert string to number 
            hero_id_convered_to_int = int(row['hero_id'])  # convert string to number 

            level = level_convered_to_int
            hero_id = hero_id_convered_to_int
            required_runes = meditation.get_required_runes(level_convered_to_int, rpc_server)

            try:
                meditation.start_meditation(hero_id, meditation.stat2id(stat_1), meditation.stat2id(stat_2), meditation.stat2id(stat_3),
                                            meditation.ZERO_ADDRESS, private_key, w3.eth.getTransactionCount(account_address),
                                            gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
                hero_meditation = meditation.get_hero_meditation(hero_id, rpc_server)
                logger.info("Pending meditation "+str(hero_meditation))
                logger.info("Wait 20s to start the next hero")
                time.sleep(20)
                

            except:
                print("An exception occurred")

# In Part 2, we complete meditation by looping through the CSV a second time.

    with open('heroes_to_level.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            csv_hero_id = row['hero_id']
            csv_level = row['level']
            stat_1 = row['stat_1']
            stat_2 = row['stat_2']
            stat_3 = row['stat_3']
            level_convered_to_int = int(row['level'])  # convert string to number 
            hero_id_convered_to_int = int(row['hero_id'])  # convert string to number 

            level = level_convered_to_int
            hero_id = hero_id_convered_to_int

            try:
                meditation.complete_meditation(hero_id, private_key, w3.eth.getTransactionCount(account_address),
                                                gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
                logger.info("Completing meditation for " + csv_hero_id )
                logger.info("Wait 40s for next hero")
                time.sleep(40)

            except:
                print("An exception occurred")
