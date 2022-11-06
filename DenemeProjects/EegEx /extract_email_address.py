# regex is powerful and vast topic
# you can do match, search, replace, extract etc...
import re

# extract email addresses from text
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text, re.I))

