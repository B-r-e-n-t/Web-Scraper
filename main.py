# from bs4 import BeautifulSoup
# import requests
#
# try:
#     source = requests.get('https://boardgamegeek.com/browse/boardgame')
#     source.raise_for_status()
#
#     soup = BeautifulSoup(source.text, 'html.parser')
#
#     board_games = soup.find('table', class_='collection_table').find_all('tr', id='row_')
#
#     for board_game in board_games:
#
#         names = board_game.find('td', class_='collection_objectname')
#
#         for i in range(1, 100):
#             name_of_games = names.find('div', id=f'results_objectname{i}')
#             name_of_game = name_of_games.find('a', class_='primary').text
#             print(name_of_game)
#
#         rank = board_game.find('td', class_='collection_rank').text
#
#         # year = board_game.find('span', class_='smallerfont').text.strip('()')
#
#         score = board_game.find('td', class_='collection_bggrating').text
#
#
# except Exception as e:
#     print(e)






from bs4 import BeautifulSoup
import requests, openpyxl

try:
    source = requests.get('https://boardgamegeek.com/browse/boardgame')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    board_games = soup.find('table', class_='collection_table').find_all('tr', id=lambda x: x and x.startswith('row_'))

    for board_game in board_games:
        name_cell = board_game.find('td', class_='collection_objectname')
        if name_cell:
            name_of_game = name_cell.find('a').text if name_cell.find('a') else 'No title found'

        rank = board_game.find('td', class_='collection_rank').text.strip()
        score = board_game.find('td', class_='collection_bggrating').text.strip()

        print(f'{rank}) {name_of_game} {score}')
        # Uncomment if you need year and score
        # year = board_game.find('span', class_='smallerfont').text.strip('()')
        # score = board_game.find('td', class_='collection_bggrating').text

except Exception as e:
    print(e)
