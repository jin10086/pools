from .hashnest import getdata as runhashnest
from .oxbtc import getdata as run0xbtc
from .miningzoo import getdata as runminingzoo
from .pool_bitcoin import getdata as runpool_bitcoin

runlist = [runhashnest, run0xbtc, runminingzoo, runpool_bitcoin]
