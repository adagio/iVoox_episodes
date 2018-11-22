from ruamel.yaml import YAML
from modules.enums import ContentMode
from modules.enums import ValueType



class Formulas:


    def update_enums(self, yaml_formulas):

        for i, (key, ordered_formula) in enumerate(yaml_formulas.items()):
            
            if ( yaml_formulas[key]['content_mode'] == "text" ):
                yaml_formulas[key]['content_mode'] = ContentMode.text
            elif ( yaml_formulas[key]['content_mode'] == 'content_attribute' ):
               yaml_formulas[key]['content_mode'] = ContentMode.content_attribute
            elif ( yaml_formulas[key]['content_mode'] == 'href_attribute' ):
                yaml_formulas[key]['content_mode'] = ContentMode.href_attribute

            if ( yaml_formulas[key]['value_type'] == 'text' ):
                yaml_formulas[key]['value_type'] = ValueType.text
            elif ( yaml_formulas[key]['value_type'] == "number" ):
                yaml_formulas[key]['value_type'] = ValueType.number

        return yaml_formulas


    def load_formulas(self):
        stream = open("modules/formulas.yaml", 'r')
        yaml = YAML()
        yaml_formulas = yaml.load(stream)

        yaml_formulas = self.update_enums(yaml_formulas)

        return yaml_formulas
