"""
aiowhois - Asyncio-based WHOIS Client for Python 3.5+

Usage:
  import aiowhois
  parsed_whois = aiowhois.query(domain_name)

"""

# Project details
__author__ = 'Bruno Medina <bruno@std.sh>'
__license__ = 'MIT'
from .__version__ import __version__

# Exceptions
from .exceptions import *

# Constants
from .constants import WhoisMethod

# Logging
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Classes
from .whois import Whois