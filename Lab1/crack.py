# Written with <3 by Julien Romero

import hashlib
from sys import argv
import sys
if (sys.version_info > (3, 0)):
    from urllib.request import urlopen
    from urllib.parse import urlencode
else:
    from urllib2 import urlopen
    from urllib import urlencode


class Crack:
    """Crack The general method used to crack the passwords"""

    def __init__(self, filename, name):
        """__init__
        Initialize the cracking session
        :param filename: The file with the encrypted passwords
        :param name: Your name
        :return: Nothing
        """
        self.name = name.lower()
        self.passwords = get_passwords(filename)

    def check_password(self, password):
        """check_password
        Checks if the password is correct
        !! This method should not be modified !!
        :param password: A string representing the password
        :return: Whether the password is correct or not
        """
        password = str(password)
        cond = False
        if (sys.version_info > (3, 0)):
            cond = hashlib.md5(bytes(password, "utf-8")).hexdigest() in \
                self.passwords
        else:
            cond = hashlib.md5(bytearray(password)).hexdigest() in \
                self.passwords
        if cond:
            args = {"name": self.name,
                    "password": password}
            args = urlencode(args, "utf-8")
            page = urlopen('http://137.194.211.71:5000/' +
                                          'submit?' + args)
            if b'True' in page.read():
                print("You found the password: " + password)
                return True
        return False

    # Most common passwords
    def crack1(self):
        """crack
        Cracks the passwords. YOUR CODE GOES HERE.
        """
        f = open("10k_most_common.txt","r")
        line = f.readline()
        line = line[:-1]
        while line:             
            line = f.readline()  
            line = line[:-1] 
            self.check_password(line)
        f.close()

        pass


    # Dictionary attack with the 10000 most common French words (in lowercase)
    def crack2(self):
        f = open("fr_50k.txt","r")
        line = f.readline()
        line = line[:-1]
        while line:             
            line = f.readline()  
            line = line[:-1] 
            line2 = line.split(" ")
            self.check_password(line2[0])
        f.close()

        pass

    # The dictionary attack, randomly adding/removing diacritics to letters
    # Failed 
    def crack3(self):
        """crack
        Cracks the passwords. YOUR CODE GOES HERE.
        """
        f = open("fr_50k.txt","r")
        line = f.readline()
        line = line[:-1]
        while line:             
            line = f.readline() 
            line = line[:-1] 
            line2 = line.split(" ")
            self.check_change_password(line2[0])
        f.close()
        # self.check_password(self.get_passwords("foo.txt"))

        pass



    # Brute force with up to 10 digits 
    def crack4(self):
        # f = open("foo.txt","r")
        # line = f.readline()
        # line = line[:-1]
        # while line:         
        #     line = f.readline() 
        #     line = line[:-1]    
        #     self.check_password(line)
        # f.close()
        # self.check_password(get_passwords("foo.txt"))
        # a = ""
        # for i in range(0,10000000000):
        #     self.check_password(str(i))
        for i in range(0,10):
            password = str(i)
            self.check_password(password)
            print(password)
        for i in range(0,10):
            for j in range(0,10):
                password = str(i)+str(j)
                self.check_password(password)
                print(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    password = str(i)+str(j)+str(k)
                    self.check_password(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        password = str(i)+str(j)+str(k)+str(l)
                        self.check_password(password)
                        # print(password)
                        # print(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        for m in range(0,10):
                            password = str(i)+str(j)+str(k)+str(l)+str(m)
                            self.check_password(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        for m in range(0,10):
                            for ii in range(0,10):
                                password = str(i)+str(j)+str(k)+str(l)+str(m)+str(ii)
                                self.check_password(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        for m in range(0,10):
                            for ii in range(0,10):
                                for jj in range(0,10):
                                    password = str(i)+str(j)+str(k)+str(l)+str(m)+str(ii)+str(jj)
                                    self.check_password(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        for m in range(0,10):
                            for ii in range(0,10):
                                for jj in range(0,10):
                                    for kk in range(0,10):
                                        password = str(i)+str(j)+str(k)+str(l)+str(m)+str(ii)+str(jj)+str(kk)
                                        self.check_password(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        for m in range(0,10):
                            for ii in range(0,10):
                                for jj in range(0,10):
                                    for kk in range(0,10):
                                        for ll in range(0,10):
                                            password = str(i)+str(j)+str(k)+str(l)+str(m)+str(ii)+str(jj)+str(kk)+str(ll)
                                            self.check_password(password)
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for l in range(0,10):
                        for m in range(0,10):
                            for ii in range(0,10):
                                for jj in range(0,10):
                                    for kk in range(0,10):
                                        for ll in range(0,10):
                                            for mm in range(0,10):
                                                password = str(i)+str(j)+str(k)+str(l)+str(m)+str(ii)+str(jj)+str(kk)+str(ll)+str(mm)
                                                self.check_password(password)
        pass

    # Brute force with up to 5 letters
    def crack5(self):

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        for i in range(0,52):
            password = str(alphabet[i])
            self.check_password(str(i))
        for i in range(0,52):
            for j in range(0,52):
                password = str(alphabet[i])+str(alphabet[j])
                self.check_password(password)
        for i in range(0,52):
            for j in range(0,52):
                for k in range(0,52):
                    password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])
                    self.check_password(password)
        for i in range(0,52):
            for j in range(0,52):
                for k in range(0,52):
                    for l in range(0,52):
                        password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[l])
                        self.check_password(password)
        for i in range(0,52):
            for j in range(0,52):
                for k in range(0,52):
                    for l in range(0,52):
                        for m in range(0,52):
                            password = str(alphabet[i])+str(alphabet[j])+str(alphabet[k])+str(alphabet[l])+str(alphabet[m])
                            self.check_password(password)

        pass




    # The river John and Jane Doe spent their honeymoon around (try all rivers)
    # Failed




    # Diceware passwords built from US states (in lowercase with hyphens in between) up to length 5
    def crack7(self):

        f = open("states.txt","r")
        line = f.readline()
        line = line[:-1]
        states = []
        while line:             #直到读取完文件
            line = f.readline()  #读取一行文件，包括换行符
            line = line[:-1] 
            states.append(str(line.lower()))
        # print(states)
        for i in states:
            password = str(i)
            self.check_password(password)
        for i in states:
            for j in states:
                password = str(i)+"-"+str(j)
                self.check_password(password)
                print(password)
        for i in states:
            for j in states:
                for k in states:
                    password = str(i)+"-"+str(j)+"-"+str(k)
                    self.check_password(password)
        for i in states:
            for j in states:
                for k in states:
                    for l in states:
                        password = str(i)+"-"+str(j)+"-"+str(k)+"-"+str(l)
                        self.check_password(password)
        for i in states:
            for j in states:
                for k in states:
                    for l in states:
                        for m in states:
                            password = str(i)+"-"+str(j)+"-"+str(k)+"-"+str(l)+"-"+str(m)
                            self.check_password(password)
        # filename = "states.txt"
        # states = get_passwords(filename)
        # for i1 in states:
        #     self.check_password(i1.lower())
        # for i1 in states:
        #     for i2 in states:
        #         self.check_password(i1.lower()+"-"+i2.lower())
        # for i1 in states:
        #     for i2 in states:
        #         for i3 in states:
        #             self.check_password(i1.lower()+"-"+i2.lower()+"-"+i3.lower())
        # for i1 in states:
        #     for i2 in states:
        #         for i3 in states:
        #             for i4 in states:
        #                 self.check_password(i1.lower()+"-"+i2.lower()+"-"+i3.lower()+"-"+i4.lower())
        # for i1 in states:
        #     for i2 in states:
        #         for i3 in states:
        #             for i4 in states:
        #                 for i5 in states:
        #                     self.check_password(i1.lower()+"-"+i2.lower()+"-"+i3.lower()+"-"+i4.lower()+"-"+i5.lower())


        f.close()

        pass



    # In October 2013, one of John Doe's password: "Thal3s", was leaked in the Adobe security breach. Guess its Google account password
    def crack8(self):

        self.check_password("Thal3s")
        for i in ['G','g','9']:
            for j in ['O','o','0']:
                for k in ['O','o','0']:
                    for l in ['G','g','9']:
                        for m in ['L','l','1']:
                            for n in ['E','e','3']:
                                password = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)
                                # print(password)
                                self.check_password(password)
            

        pass

    # Use the following informations about John Doe in order to find his master password
    # Failed


def get_passwords(filename):
    """get_passwords
    Get the passwords from a file
    :param filename: The name of the file which stores the passwords
    :return: The set of passwords
    """
    passwords = set()
    with open(filename, "r") as f:
        for line in f:
            passwords.add(line.strip())
    return passwords


if __name__ == "__main__":
    name = "chen".lower()
    # This is the correct location on the moodle
    encfile = "./" + name + ".enc"
    
    # If you run the script on your computer: uncomment and fill the following 
    # line. Do not forget to comment this line again when you submit your code
    # on the moodle.
    # encfile = "PATH TO YOUR ENC FILE"
    
    # First argument is the password file, the second your name
    crack = Crack(encfile, name)
    crack.crack1()