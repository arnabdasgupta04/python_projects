userid=input('What is your userid ?')
password=input('What is your password ?')
hidden_pwrd= '*' * len(password)
print(f'Hi {userid} , your password {hidden_pwrd} is {len(password)} letters long .')