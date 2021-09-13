with open('file.txt', 'r') as infile:
    try:
        words = infile.read().split()
        max_len = len(max(words, key=len))
        print('Longest word: ',[word for word in words if len(word) == max_len][0])
        print('Maximum no. of character present in a line : ', len(max(open('file.txt'), key=len)))
    except:
        print("Is your file empty ? ")