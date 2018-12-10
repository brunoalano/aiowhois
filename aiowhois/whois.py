"""
Asyncio-based WHOIS Protocol Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This class implements the current implementations of RFC WHOIS,
including the legacy WHOIS in port `43`, and the HTTP based solution
described as `RDAP`.

Usage:
  import aiowhois
  resolv = aiowhois.Whois()
  data = await resolv.query(my_domain)

"""
import asyncio
import aiodns
import tldextract
from enum import Enum
from typing import List, Any

from .exceptions import *
from .constants import WhoisMethod


class Whois(object):
  def __init__(self, timeout: Any = 5,
               allowed_methods: List[WhoisMethod] = [WhoisMethod.LEGACY, WhoisMethod.RDAP],
               resolver: aiodns.DNSResolver = None,
               loop: asyncio.BaseEventLoop = None,
               proxy: str = None,
               proxy_auth: str = None,
               proxy_list: List[str] = None):
    self.timeout = timeout
    self.allowed_methods = allowed_methods
    self.loop = loop or asyncio.get_event_loop()
    self.resolver = resolver or aiodns.DNSResolver(loop=self.loop)
    self.proxy = proxy
    self.proxy_auth = proxy_auth
    self.proxy_list = proxy_list or []

  async def query(self, domain_name: str) -> dict:
    # extract domain data
    domain_data = tldextract.extract(domain_name)
    if not domain_data.suffix:
      raise InvalidDomainName()

    # not implemented yet!
    pass