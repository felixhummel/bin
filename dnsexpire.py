#!/usr/bin/env python
# vim: set fileencoding=utf-8 filetype=python :
"""
Prints the expiration time of a domain as seen from the host this is run on.

Example Output:

    felixhummel.de (37.200.98.98): 3055 sec (about 50 min)
"""
from __future__ import print_function
import six

import calendar
import time
import sys


def _exit1(msg):
    print(msg, file=sys.stderr)
    raise SystemExit(1)


try:
    import dns.resolver
except ImportError:
    if six.PY2:
        _exit1('Please install dnspython, e.g. ``pip install --user dnspython``')
    elif six.PY3:
        _exit1('Please install dnspython3, e.g. ``pip install --user dnspython3``')
    else:
        _exit1('Please install dnspython for your Python version.')


def remain(domain):
    """
    :return: A tuple containing (ip, remaining_seconds)
    """
    x = dns.resolver.resolve(domain)
    ip = x.response.answer[0][0].address
    remaining = x.expiration - calendar.timegm(time.gmtime())
    return ip, remaining


def main(domains):
    for domain in domains:
        try:
            ip, remain_sec = remain(domain)
            if remain_sec < 60:
                print('%s (%s): %d sec' % (domain, ip, remain_sec))
            else:
                print('%s (%s): %d sec (about %.1d min)' % (domain, ip, remain_sec, remain_sec / 60.0))
        except dns.resolver.NoAnswer:
            print('%s: no answer' % domain)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        _exit1('Usage: dns_expire <domain>...')
    domains = sys.argv[1:]
    main(domains)

