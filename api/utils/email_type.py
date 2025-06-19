import re

def email_type(value):
  if re.match(r"[^@]+@[^@]+\.[^@]+", value):
    return value
  else:
    raise ValueError("Invalid Email Address.")