from API import *

class Snowflake:
    def __init__(self, timestamp=None):
        self.timestamp = _get_timestamp_ms(timestamp)
        self.snowflake = (self.timestamp - DISCORD_EPOCH) << 22
    
    def getTimestamp(self):
        return self.timestamp
    
    def getSnowflake(self):
        return self.snowflake
    
class Timestamp:
    def __init__(self, snowflake=None):
        self.snowflake = DISCORD_EPOCH
        self.timestamp = _breakdown_snowflake(self.snowflake)['timestamp']
    
    def getTimestamp(self):
        return self.timestamp
    
    def getSnowflake(self):
        return self.snowflake
