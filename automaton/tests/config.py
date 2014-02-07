import argparse
import string
import random
import unittest

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class FailedTestException(Exception):
    pass

class ConfigurationMixin(object):
    def parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('url')
        parser.add_argument('email')
        parser.add_argument('--beta', action='store_true')
        parser.add_argument('wp_login')
        parser.add_argument('wp_password')
        args = parser.parse_args()
        return args

    def _inject(self, args):
        self.base_url = args.url
        email_comps = args.email.split("@")
        alias = email_comps[0]+"+"+id_generator()+"@"+email_comps[1]
        self.email = alias
        self.beta = args.beta
        if self.beta:
            self.wp_login = args.wp_login
            self.wp_pass = args.wp_password

    def inject(self):
        args = self.parse()
        self._inject(args)
        self.test_inject()

    def test_inject(self):
        if isinstance(self, unittest.TestCase):
            self.debug()
        else:
            raise SystemError()
