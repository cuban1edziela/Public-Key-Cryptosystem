

def messageLength(message, length):
    messageLength, remainder = divmod(len(message), length)
    if(remainder != 0):
        messageLength += 1
        return messageLength
    return messageLength