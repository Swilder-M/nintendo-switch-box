import os

from nintendo import NintendoClient
from utils import convert_play_duration, update_gist, truncate_strings

session_token = os.environ.get('NINTENDO_SESSION_TOKEN')
github_token = os.environ.get('GH_TOKEN')
gist_id = os.environ.get('GIST_ID')

if __name__ == '__main__':
    if not session_token:
        print('Please set the session token to the environment')
        exit(1)

    client = NintendoClient(session_token=session_token)
    play_histories = client.get_play_histories()
    show_records = []
    for i in play_histories['playHistories']:
        record = {
            'title': i['titleName'],
            'played_minutes': i['totalPlayedMinutes'],
            'played_minutes_str': convert_play_duration(i['totalPlayedMinutes']),
            'played_days': i['totalPlayedDays'],
        }
        if record['played_minutes'] == 0:
            continue

        title_en = client.get_game_title(i['titleId'], region='US').get('name')
        if title_en:
            record['title'] = title_en
        record['title'] = record['title'].replace('™', '').strip()

        show_records.append(record)
    show_records.sort(key=lambda x: x['played_minutes'], reverse=True)
    if len(show_records) == 0:
        print('No play history found.')
        exit(0)

    gist_content = ''
    for record in show_records[:20]:
        line = [
            truncate_strings(record['title'], 26).ljust(26),
            record['played_minutes_str'].rjust(16),
            str(record['played_days']).rjust(4) + ' days'
        ]
        line = ' '.join(line)
        gist_content += line + '\n'
    update_gist(gist_id, github_token, gist_content.strip())
