from dataclasses import dataclass
from roadheader.playwright_Rh import PlaywrightRh


@dataclass
class Target:
    url: str = ""


@dataclass
class Ore:
    content: str


class HtmlRh(PlaywrightRh):
    def drill(self, target):
        self.page.goto(target.url)
        return [Ore(self.page.inner_text("body"))]

    def convey(self, ores):
        for ore in ores:
            print(ore.content)


rh = HtmlRh()
rh.process(Target("http://baidu.com"))

