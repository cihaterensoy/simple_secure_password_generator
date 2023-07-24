import random
import argparse


class random_pass():
    Chars = "abcdefgğhiıjklmnoöpqrsştuüvwxyzABCDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ1234567890.-!@#$%^&*()"
    def parseinfo(self):
        # kullanıcıdan parametre almamızı sağlar
        parse_o = argparse.ArgumentParser()
        # dest = argümanı nesnenin hangi özelliğine atayacağımızı söyler
        parse_o.add_argument("-l","--length",dest="length",help="please enter the length")
        self.data = parse_o.parse_args()
        # alınan parametrelerin herbirini bir değere atıyoruz
        return self.data

    def create_pass(self):
        pass_list = list()
        for i in range(12):
            pass_list.append(random.choice(self.Chars))

            if pass_list[i] == pass_list[i-1]:
                pass
        print(pass_list)


if __name__ == "__main__":
    password = random_pass()
    password.parseinfo()
    password.create_pass()



