import logging

from concurrent.futures import ProcessPoolExecutor, as_completed

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


    def get_episodes_by_url(self, url):

        logger = logging.getLogger('infoLogger')
        log_msg = f'{url}'
        logger.info(log_msg)

        utils = Utils()
        scraper = Scraper()
        content = utils.get_url_content(url)
        soup = scraper.get_soup(content)
        current_page_episodes = scraper.get_episodes(soup)
        
        log_msg = f'Done: {url}'
        logger.info(log_msg)

        return current_page_episodes


    def get_episodes_by_urls(self, urls):
        with ProcessPoolExecutor(max_workers=4) as executor:
            subcategory_episodes = []
            futures = [ executor.submit(self.get_episodes_by_url, url) for url in urls ]
            for completed_futures in as_completed(futures):
                subcategory_episodes.extend(completed_futures.result())
        return subcategory_episodes


    def get_episodes(self, program, max_pages):
        episodes = []
        urls = []
        for page_index in range(1, max_pages + 1):
            url = self.base_path + '/' + self.__get_url_path(program, page_index)
            urls.append(url)

        episodes = self.get_episodes_by_urls(urls)

        return episodes