from modules.utils import Utils
from modules.scraper import Scraper


class ProgramScraper:

    protocol = 'https'
    domain = 'www.ivoox.com'
    base_path = protocol + '://' +  domain

    url_path_mask = 'podcast-{url_name}_sq_f{url_id}_{url_page_index}.html'
    
    def __get_url_path(self, program, page_index):
        url_path = self.url_path_mask.format(
            url_name=program.url_name,
            url_id=program.url_id,
            url_page_index=page_index
        )
        return url_path

    def get_episodes(self, program, max_pages):
        episodes = []

        utils = Utils()
        scraper = Scraper()

        for page_index in range(1, max_pages + 1):
            url = self.base_path + '/' + self.__get_url_path(program, page_index)
            content = utils.get_url_content(url)
            soup = scraper.get_soup(content)
            current_page_episodes = scraper.get_episodes(soup)
            episodes.extend(current_page_episodes)
        return episodes
