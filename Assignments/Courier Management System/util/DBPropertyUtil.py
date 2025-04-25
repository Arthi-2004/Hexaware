# util/DBPropertyUtil.py
import configparser

def get_db_properties():
    config = configparser.ConfigParser()
    config.read('db_config.ini')  # Read the configuration file

    db_properties = {
        'driver': config['DatabaseConfig']['Driver'],
        'server': config['DatabaseConfig']['Server'],
        'database': config['DatabaseConfig']['Database'],
        'trusted_connection': config['DatabaseConfig']['Trusted_Connection']
    }

    return db_properties

