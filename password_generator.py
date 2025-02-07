import string
import random



if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = string.ascii_letters

    plen = int(input("Enter password length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    random.shuffle(s)
    
    print("Your password is: ")
    # print("".join(s[0:plen]))
    print("".join(random.sample(s, plen)))