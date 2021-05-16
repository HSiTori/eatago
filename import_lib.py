import pywebio
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import hold
from pywebio.session import info as session_info
import asyncio
import time
from datetime import datetime

# menu.py
import requests
import json
from functools import partial


# all .py import
from setting import *
from whoAreYou import *
from menu import *

# tqdm
from tqdm import *
