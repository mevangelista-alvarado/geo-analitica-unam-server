# -*- coding: utf-8 -*-
""" Content Secure Policy
This list will be maitened everytime a plugin, o new service is added to prescrypto
With the following format

IMG SRC for images
FONT SRC for Fonts
SCRIPT SRC for external scripts
etc.

Sometimes a portal has a lot of src on a domain use the comodin '*' to correctly adding
"""

CSP_DEFAULT_SRC = (
    "'self'",
)

CSP_SCRIPT_SRC = CSP_DEFAULT_SRC + (
    "code.jquery.com",
    "cdn.mathjax.org",
    "ajax.googleapis.com",
    "drive.google.com"
)
