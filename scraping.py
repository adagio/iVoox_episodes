from modules.program import Program
from modules.program_scraper import ProgramScraper
from modules.storage import Storage

program_url_name = 'web-reactiva-programacion-desarrollo-web'
program_url_id = '1454279'

program = Program(program_url_id, program_url_name)
programScraper = ProgramScraper()
episodes = programScraper.get_episodes(program=program, max_pages=4)

Storage.save_pickle(
    data=episodes,
    filename='storage/wr.pkl'
)

saved_episodes = Storage.load_pickle('storage/wr.pkl')

