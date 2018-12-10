# aiowhois

[![image](https://img.shields.io/pypi/v/aiowhois.svg)](https://pypi.python.org/pypi/aiowhois)
[![image](https://img.shields.io/pypi/l/aiowhois.svg)](https://pypi.python.org/pypi/aiowhois)
[![image](https://img.shields.io/codecov/c/github/brunoalano/aiowhois/master.svg)](https://codecov.io/gh/brunoalano/aiowhois/branch/master)
[![aiowhois Build status](https://travis-ci.org/brunoalano/aiowhois.svg)](https://travis-ci.org/brunoalano/aiowhois)

Asyncio-based WHOIS supporting **legacy** and **RDAP** protocols.

```python
>>> import aiowhois

>>> resolv = aiowhois.Whois(timeout=10)
>>> parsed_whois = await resolv.query(my_domain)
```

## Why aiowhois?

TODO
