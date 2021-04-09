def Machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1]+keys[0:-1]

    encrptDict = dict(zip(keys, value))
    decrptDict = dict(zip(value, keys))

    message = input("Please Enter Your Secret Message: ")
    mode = input("Please Enter Encode(E) or Decode(D): ")

    if mode.upper() == 'E':
        newMessage = ''.join([encrptDict[letter]
                             for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decrptDict[letter]
                             for letter in message.lower()])
    else:
        print("Please Enter a Correct Choice")

    return newMessage


print(Machine())
