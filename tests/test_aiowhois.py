import pytest
from aiowhois.exceptions import *

@pytest.fixture
def whois():
  from aiowhois import Whois
  return Whois()

@pytest.mark.asyncio
async def test_invalid_domain(whois):
  with pytest.raises(InvalidDomainName):
    res = await whois.query("invalid domain")