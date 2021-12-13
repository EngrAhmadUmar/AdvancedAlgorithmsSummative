textinput = 'Plain text'
key = 2

# Here we will be creating our encryption function which will take in two parameters our key and text
def encryption(text, key):
    # Initializing the variable where we will store encrypted message
    encrypted_message = ""

    # Creating our variable that will help us track our location in our 
    # String and to help us make sure we are still less than the key.
    start = 0

    # Here we loop through the key and while are still inbound our key, 
    # We loop through the text in steps of our key and add characters to our result variable
    while start < key:
        for j in range(start, len(text), key):
            # Formulating our result with characters gotten in steps of our key.
            encrypted_message += text[j]
            # Incrementing our start variable so we go to the next index.*-+-
        start += 1
    # Returning our result
    return encrypted_message
encrypted = encryption(textinput, key)

# Here we will be creating our decryption function which will take in two parameters our key and encrypted text
def decryption(encrypted, key):
    # Creating the variables needed for the decryption
    start = 0
    decrypted_message = ''

    # Checking for edge cases when the length of text and the key is even
    if len(encrypted) % 2 == 0 and key % 2 == 0:
        # We create the partition of the text to start from by dividing the length of the word by the key
        partition = len(encrypted) // key

        # We loop while our start value is less than our partition
        while start < partition:
            # loop through the length of the word starting at start and take partition steps every time
            for i in range(start, len(encrypted), partition):
                # Concatenating our characters to our result variable
                decrypted_message += encrypted[i]
            # Incrementing our start variable so we go to the next index.
            start += 1

    # Checking for edge cases when the length of text key is even and length of key is odd.
    if len(encrypted) % 2 == 0 and key % 2 != 0:
        # We create the partition of the text to start from by dividing the length of the word by the key
        partition = len(encrypted) // key

        # While a in less than the partition
        while start < partition:
            partition += 1
            # Adding the characters to our result variable
            decrypted_message += encrypted[start]
            # Here we beginning looping through our words starting at start
            for i in range(start, len(encrypted)):
                # Getting our next index to add to our result
                c = i + partition
                decrypted_message += encrypted[c]
                # Getting the next index to add to the answer
                decrypted_message += encrypted[c + key]
                # Stopping our loop
                break

            # Resetting our partition index
            partition = len(encrypted) // key
            # Incrementing our start variable so we go to the next index.
            start += 1
        # Concatenating the last character of our partition to our result variable
        decrypted_message += encrypted[partition]

    # Returning decrypted_message
    return decrypted_message
decrypted = decryption(encrypted, key)

print("Plain text: " + textinput)
print("Key being used: " + str(key))
print("Text after encryption: " + encrypted)
print("Text after decryption: " + decrypted)
