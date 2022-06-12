from ..HTTP import HTTPClient
import json, time

DISCORD_EPOCH = 1420070400000

def _get_timestamp_ms(timestamp=None):
    return int(time.time_ns() / 1000) if timestamp is None \
    else int(timestamp * 1000)

def _breakdown_snowflake(snowflake):
    timestamp = (snowflake >> 22) + DISCORD_EPOCH
    workerid = (snowflake & 0x3E0000) >> 17
    processid = (snowflake & 0x1F000) >> 12
    increment = snowflake & 0xFFF

    return {'timestamp': timestamp, 'worker id': workerid, 'process id': processid, 'increment': increment}

class DiscordAPI:
    def __init__(self, version=None):
        if version is None:
            version = 10
        
        self.apiver = f'v{version}'
    
