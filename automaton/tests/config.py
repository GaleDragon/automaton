import argparse
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class ConfigurationMixin(object):
    def inject(self, args):
        self.base_url = args.url
        email_comps = args.email.split("@")
        alias = email_comps[0]+"+"+id_generator()+"@"+email_comps[1]
        self.email = alias
        self.beta = args.beta
        if self.beta:
            self.wp_login = args.wp_login
            self.wp_pass = args.wp_password
