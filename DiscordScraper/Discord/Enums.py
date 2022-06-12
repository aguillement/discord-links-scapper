from enum import Enum

class MessageTypes(Enum):
    GUILD_TEXT = 0            #
    DM = 1                    #
    GUILD_VOICE = 2           #
    GROUP_DM = 3              #
    GUILD_CATEGORY = 4        #
    GUILD_NEWS = 5            #
    GUILD_NEWS_THREAD = 10    #
    GUILD_PUBLIC_THREAD = 11  #
    GUILD_PRIVATE_THREAD = 12 #
    GUILD_STAGE_VOICE = 13    #
    GUILD_DIRECTORY = 14      #
    GUILD_FORUM = 15          # in development

class UserTypes(Enum):
    STAFF = 1 << 0                   #
    PARTNER = 1 << 1                 #
    HYPESQUAD = 1 << 2               #
    BUG_HUNTER_L1 = 1 << 3           #
    HYPESQUAD_BRAVERY = 1 << 6       #
    HYPESQUAD_BRILLIANCE = 1 << 7    #
    HYPESQUAD_BALANCE = 1 << 8       #
    PREMIUM_EARLY_SUPPORTER = 1 << 9 #
    TEAM_PSEUDO_USER = 1 << 10       #
    BUG_HUNTER_L2 = 1 << 14          #
    VERIFIED_BOT = 1 << 16           #
    VERIFIED_DEVELOPER = 1 << 17     #
    CERTIFIED_MODERATOR = 1 << 18    #
    BOT_HTTP_INTERACTIONS = 1 << 19  #

class PremiumTypes(Enum):
    NONE = 0          #
    NITRO_CLASSIC = 1 #
    NITRO = 2         #