import requests
import time
import random

# Kalimat-kalimat yang ingin dioutputkan secara acak
sentences = [
    'Hello and have a great day!',
    'hello udfam...',
    'Good morning all........',
    'Hi Ud twitter fam, are you there......... !',
    'i like collect Unstoppabledomains.',
    'This project has a very bright future.',
]

# ID saluran Discord
channel_id = input('Masukkan channel ID: ')

# Jeda waktu antara pengiriman pesan (dalam detik)
waktu = int(input('Masukkan waktu jeda (dalam detik): '))
hapusx = int(input('Masukkan waktu hapus (dalam detik): '))
# Header otentikasi (token bot Discord)
auth_token = input('Masukkan Authorization token bot: ')
headers = {
    'Authorization': auth_token,
    'Content-Type': 'application/json'
}

while True:
    # Pesan yang akan dikirim
    message = random.choice(sentences)

    # Payload JSON
    payload = {
        'content': message
    }

    # Mengirim pesan menggunakan requests
    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)

    # Mengecek apakah pesan berhasil dikirim atau tidak
    if response.status_code == 200:
        print('Pesan berhasil dikirim!')
        
        # Mendapatkan ID pesan yang baru saja dikirim
        message_id = response.json()['id']
        
        # Menghapus pesan setelah 20 detik
        time.sleep(hapusx)
        delete_response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)

        # Mengecek apakah pesan berhasil dihapus atau tidak
        if delete_response.status_code == 204:
            print('Pesan berhasil dihapus!')
        else:
            print('Pesan gagal dihapus!')
    else:
        print('Pesan gagal dikirim!')

    # Jeda waktu antara pengiriman pesan
    time.sleep(waktu)
