from email.mime import base
from ssl import ALERT_DESCRIPTION_UNKNOWN_CA
import data as d
import time
import os
import sys
import poke_validation as pv
from get_module import get_info

clear = 'cls' if sys.platform == 'win32' else 'clear'

name = input("Nombre de pokemon: ")
name = pv.validate(name)