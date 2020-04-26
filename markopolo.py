import json
from io import StringIO


class Markopolo(object):
    def __init__(self, filecontent):
        self.filecontent = filecontent
        self.final = []

    def paragraphs(self, separator="\n"):
        if separator[-1:] != "\n":
            separator += "\n"
        paragraph = []
        fileobj = StringIO(self.filecontent)

        for line in fileobj:
            # import pdb

            # pdb.set_trace()
            if line == separator:
                if paragraph:
                    yield "".join(paragraph)
                    paragraph = []
            else:
                paragraph.append(line)
        if paragraph:
            yield "".join(paragraph)

    def cleantitle(self, title):
        if "=" in title:
            return title.strip().replace("=", "").strip()

        if "-" in title:
            return title.strip().replace("-", "").strip()

        if "~" in title:
            return title.strip().replace("~", "").strip()

        if "#" in title:
            return title.strip().replace("#", "").strip()

    def process(self):
        result = {"title": None, "content": []}

        for paragraph in self.paragraphs():
            if (
                paragraph.strip().startswith("====")
                or paragraph.strip().endswith("====")
                or paragraph.strip().startswith("-----")
                or paragraph.strip().endswith("-----")
                or paragraph.strip().startswith("~~~~~~")
                or paragraph.strip().endswith("~~~~~~")
                or paragraph.strip().startswith("# ")
                or paragraph.strip().startswith("## ")
            ):
                if result["title"]:
                    self.final.append(result)

                    result = {"title": None, "content": []}

                result["title"] = self.cleantitle(paragraph)

            elif paragraph.startswith(".. "):
                result["content"].append({"codeblock": paragraph})
            elif paragraph.startswith("    "):
                result["content"].append({"codeblock": paragraph})
            else:
                result["content"].append({"paragraph": paragraph})

        # Finally result is not inserted into final
        self.final.append(result)

    def parse(self):
        self.process()
        return self.final
