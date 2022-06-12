from Enums import PremiumTypes, UserTypes
from Types import Snowflake, timestamp
from dataclasses import dataclass
import * from API

@dataclass
class DiscordUser:
    id: Snowflake              #
    username: str              #
    discriminator: str         #
    avatar: str                #
    bot: bool                  #
    system: bool               #
    mfa_enabled: bool          #
    banner: str                #
    accent_color: int          #
    locale: str                #
    verified: bool             #
    email: str                 #
    flags: UserTypes           #
    premium_type: PremiumTypes #
    public_flags: UserTypes    #
