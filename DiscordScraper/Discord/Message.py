from Types import Snowflake, timestamp
from dataclasses import dataclass
from Enums import MessageTypes
import * from API

@dataclass
class Overwrite:
    id: Snowflake #
    type: int     # 0 = role | 1 = member
    allow: str    #
    deny: str     #

@dataclass
class DiscordMessage:
    id: Snowflake               #
    type: MessageTypes          # 
    guild_id: Snowflake         #
    position: int               #
    permission: list<Overwrite> #
    name: str                   #
    topic: str                  #
    nsfw: bool                  #
    last_message_id: Snowflake  #
    bitrate: int                #
    user_limit: int             #
    rate_limit_per_user: int    #
    recipients: list