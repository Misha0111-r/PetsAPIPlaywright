class BasePage:
    def __init__(self, page):
        self.page = page

    def open_page(self, link):
        self.page.goto(link)

    def get_pet_id_from_page(self):
        return self.page.url[-5:]
