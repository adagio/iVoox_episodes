from bs4 import BeautifulSoup
from modules.formulas import Formulas
from modules.enums import ContentMode
from modules.enums import ValueType


class Scraper:


    def __init__(self):
        formulas = Formulas()
        self.yaml_formulas = formulas.load_formulas()


    def get_soup(self, text):
        soup = BeautifulSoup(text, features="lxml")
        return soup


    def __get_html_tag(self, html_block, pattern):
        return html_block.select(pattern)[0]


    def __get_value(self, html_tag, content_mode, value_type):
        if ( content_mode == ContentMode.content_attribute ):
            return html_tag.attrs['content']
        elif ( content_mode == ContentMode.text ):
            text_value = html_tag.getText().strip()
            if text_value != '':
                if ( value_type == ValueType.number ):
                    return int(text_value)
                else:
                    return text_value
            else:
                return None
        else:
            return None


    def __get_values(self, html_block):
        
        values = {}

        for i, (key, ordered_formula) in enumerate(self.yaml_formulas.items()):
            formula = dict(ordered_formula)
            html_tag = self.__get_html_tag(html_block, formula['html_pattern'])
            value = self.__get_value(
                html_tag=html_tag,
                content_mode=formula['content_mode'],
                value_type=formula['value_type']
            )
            values[key] = value

        return values


    def __build_episode_object(self, episode_html_block):
        values = self.__get_values(episode_html_block)
        return values


    def get_episodes(self, resource: BeautifulSoup):
        """
            Extrae el listado de episodeios 
            Devuelve una lista con el diccionario de elementos encontrados
        """
        episodes = []
        for episode_html_block in resource.findAll("div", {"class": ["modulo-type-episodio"]}):
            try:
                episode = self.__build_episode_object(episode_html_block)
                episodes.append(episode)
            except IndexError:
                print("No se puede capturar el contenido") 

        return episodes

