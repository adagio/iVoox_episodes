import requests

class Utils:

    def get_url_content(self, url):
        """
            Extrae el contenido de unas URL específicas
        """
        res = requests.get(url)
        # Levanta el error solo si algo fue mal (errores 400)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('Problem! %s' % (exc))

        text = res.text

        return text