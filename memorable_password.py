def secure_password(password, replacements):


    secure_password = password
    for char, replacement in replacements:
        secure_password = secure_password.replace(char, replacement)

    return secure_password
    
if __name__ == "__main__":
    original_password = input("Enter your password: ")

    replacements_rule = (('a', '@'), ('s', '$'), ('o', '0'), ('i', '!'), ('I', '1'), ('and', '&'))

    secured_password = secure_password(original_password, replacements_rule)
    
    print(f"your original password is: {original_password}")
    print(f"your secured password is: {secured_password}")