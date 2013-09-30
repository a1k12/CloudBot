from util import hook
import hashlib

# basic text tools

@hook.command
def upper(inp):
    """upper <string> -- Convert string to uppercase."""
    return inp.upper()

@hook.command
def lower(inp):
    """lower <string> -- Convert string to lowercase."""
    return inp.lower()

@hook.command
def titlecase(inp):
    """title <string> -- Convert string to title case."""
    return inp.title()


# encoding

@hook.command
def rot13(inp):
    """rot13 <string> -- Encode <string> with rot13."""
    return inp.encode('rot13')

# length

@hook.command
def length(inp):
    """length <string> -- gets the length of <string>"""
    return "The length of that string is {} characters.".format(len(inp))

# hashing

@hook.command
def hash(inp):
    """hash <string> -- Returns hashes of <string>."""
    return ', '.join(x + ": " + getattr(hashlib, x)(inp).hexdigest()
                     for x in ['md5', 'sha1', 'sha256'])