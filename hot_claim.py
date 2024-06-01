import requests
import threading
import time
def process_data(auth, device_id, telegram_id):
    headers = {
        'Accept': '/',
		'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': auth,
        'Connection': 'keep-alive',
		'Content-Length': '167',
        'Content-Type': 'application/json',
        'DeviceId': device_id,
		'Host': 'api0.herewallet.app',
		'Is-Sbt': 'false',
		'Network': 'mainnet',
        'Platform': 'telegram',
        'Referer': 'https://tgapp.herewallet.app/',
		'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'Sec-Ch-Ua-Mobile': '?0',
		'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Telegram-Data': telegram_id,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'game_state': {
			'balance': 584981,
			'boost': 10,
			'firespace': 0,
			'inviter': None,
			'last_claim': 1709808927165672200,
            'refferals': 0,
			'storage': 20,
            'village': None,            
        },
    }

    response = requests.post('https://api0.herewallet.app/api/v1/user/hot/claim', headers=headers, json=json_data)
    print(response.text)

with open('datahot.txt', 'r') as file:
            for line in file:
                auth, device_id, telegram_id = line.strip().split('|')
                threading.Thread(target=process_data, args=(auth, device_id, telegram_id)).start()
            time.sleep(5)
