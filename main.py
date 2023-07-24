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
        self.pass_list = list()
        for i in range(int(self.data.length)):
            self.pass_list.append(random.choice(self.Chars))
            if i == 0:
                pass
            elif self.pass_list[i] == self.pass_list[i-1]:
                self.pass_list[i] = random.choice(self.Chars)



if __name__ == "__main__":
    password = random_pass()
    password.parseinfo()
    password.create_pass()
    print(f"Your secure password {''.join(password.pass_list)}")



