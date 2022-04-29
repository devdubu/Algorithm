import re

string = "Hey! What's up bro?-._"
new_string = re.sub(r"[^a-zA-Z0-9.!\-_]","",string)
print(new_string)