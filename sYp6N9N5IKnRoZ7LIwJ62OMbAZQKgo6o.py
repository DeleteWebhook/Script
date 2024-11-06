import requests, time, os, sys
from concurrent.futures import ThreadPoolExecutor

chars = "-\033[1;34m>"

os.system('cls' if os.name == 'nt' else 'clear')

banner = f"""
\033[0;36m
                      ██╗    ██╗██╗       █████╗ ███╗   ██╗███████╗██╗████████╗      ██╗    ██╗██╗  
                     ██╔╝   ██╔╝╚██╗     ██╔══██╗████╗  ██║██╔════╝██║╚══██╔══╝     ██╔╝   ██╔╝╚██╗ 
                    ██╔╝   ██╔╝  ╚██╗    ███████║██╔██╗ ██║███████╗██║   ██║       ██╔╝   ██╔╝  ╚██╗
                    ╚██╗  ██╔╝   ██╔╝    ██╔══██║██║╚██╗██║╚════██║██║   ██║       ╚██╗  ██╔╝   ██╔╝
                     ╚██╗██╔╝   ██╔╝     ██║  ██║██║ ╚████║███████║██║   ██║        ╚██╗██╔╝   ██╔╝ 
                      ╚═╝╚═╝    ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝   ╚═╝         ╚═╝╚═╝    ╚═╝           
 
\033[1;34m                         ╭─────────────────────────────────────────────────────────────────╮
\033[1;34m                         │\033[1;32m > Author   \033[1;37m:    \033[0;33mAnSit                               \033[1;34m            │          
\033[1;34m                         │\033[1;35m > Feature  \033[1;37m:    \033[0;33mBuff Follow Tiktok                  \033[1;34m            │           
\033[1;34m                         │\033[0;35m > Discord  \033[1;37m:    \033[0;33mhttps://discord.com/W-azure         \033[1;34m            │                 
\033[1;34m                         │\033[1;34m > Telegram \033[1;37m:    \033[0;33mhttps://t.me/ansitdev               \033[1;34m            │    
\033[1;34m                         │\033[0;96m > Facebook \033[1;37m:    \033[0;33mhttps://www.facebook.com/AnSit.Developers   \033[1;34m    │                   
\033[1;34m                         ╰─────────────────────────────────────────────────────────────────╯\n\n
"""
print(banner)

def buff_follow(username):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    while True:
        access = requests.get('https://tikfollowers.com/free-tiktok-followers', headers=headers)
        try:
            session = access.cookies['ci_session']
            headers.update({'cookie': f'ci_session={session}'})
            token = access.text.split("csrf_token = '")[1].split("'")[0]
            data = '{"type":"follow","q":"@'+username+'","google_token":"t","token":"'+token+'"}'
            search = requests.post('https://tikfollowers.com/api/free', headers=headers, data=data).json()
            if search.get('success'):
                data_follow = search['data']
                data = '{"google_token":"t","token":"'+token+'","data":"'+data_follow+'","type":"follow"}'
                send_follow = requests.post('https://tikfollowers.com/api/free/send', headers=headers, data=data).json()
                if send_follow.get('o') == 'Success!' and send_follow.get('success') and send_follow.get('type') == 'success':
                    print(f'{chars} Tăng Follow Tik Tok Thành Công cho tài khoản \033[1;33m@@{username}\033[1;37m\033[1m')
                elif send_follow.get('o') == 'Oops...' and not send_follow.get('success') and send_follow.get('type') == 'info':
                    try:
                        thoigian = send_follow['message'].split('You need to wait for a new transaction. : ')[1].split('.')[0]
                        phut = thoigian.split(' Minutes')[0]
                        giay = int(phut) * 60
                        for i in range(giay, 0, -1):
                            print(f'{chars} \033[1;32mVui Lòng Chờ \033[1;37m\033[1m{i} \033[1;32mGiây cho \033[1;33m@{username}\033[1;37m\033[1m...', end='\r')
                            time.sleep(1)
                        continue
                    except:
                        print(f'{chars} \033[1;31m\033[1m\033[1mLỗi Không Xác Định cho tài khoản \033[1;33m@{username}\033[1;37m\033[1m')
                        continue
        except:
            print(f'{chars} Lỗi Không Xác Định cho tài khoản \033[1;33m@{username}\033[1;37m\033[1m')
            continue

if __name__ == '__main__':
    usernames = input(f'\033[1;34m ->\033[1;32m Nhap Cac Username Tiktok \033[1;37m\033[1m( \033[1;32m\033[1mKhong co @ \033[1;37m\033[1m) \033[1;32mMoi User Cach Nhau Bang 1 Dau Phay \033[1;37m\033[1m(\033[1;32m\033[1muser1\033[1;37m\033[1m, \033[1;32m\033[1muser2\033[1;37m\033[1m) : \033[1;33m ').split(',')
    with ThreadPoolExecutor(max_workers=len(usernames)) as executor:
        for username in usernames:
            executor.submit(buff_follow, username.strip())
