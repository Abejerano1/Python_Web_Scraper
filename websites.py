class TestWebsite:
    url = " "
    company = " "

    def __init__(self, company, url):
        self.company = company
        self.url = url

    def fullname(self):
        return '{} {}'.format(self.company, self.url)