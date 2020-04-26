import json

from markopolo import Markopolo

with open("README.md", "r") as fh:
    filecontent = fh.read()

mo = Markopolo(filecontent)
parsed_content = mo.parse()
print(json.dumps(parsed_content, indent=4))
