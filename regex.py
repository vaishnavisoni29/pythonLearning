import re

text = "Hello, world!"
pattern = "Hello"

result = re.match(pattern, text)
if result:
    print("Match found:", result.group())
else:
    print("No match")
