#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "dnspython",
# ]
# ///
#
# This execution pattern is based on
# https://simonwillison.net/2024/Aug/21/usrbinenv-uv-run/
"""
Prints the expiration time of a domain as seen from the host this is run on.

Example Output:

    felixhummel.de (37.200.98.98): 3055 sec (about 50 min)
"""

import calendar
import time
import sys


import dns.resolver


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
                print(
                    '%s (%s): %d sec (about %.1d min)'
                    % (domain, ip, remain_sec, remain_sec / 60.0)
                )
        except dns.resolver.NoAnswer:
            print('%s: no answer' % domain)
        except dns.resolver.NXDOMAIN as e:
            print(e)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: dns_expire <domain>...', file=sys.stderr)
        raise SystemExit(1)
    domains = sys.argv[1:]
    main(domains)
