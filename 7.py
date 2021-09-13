vowels=['a','e','i','o','u']
vowel_count,number_count,consonant_count,upper_case,lower_case=0,0,0,0,0
f=(open('file.txt','r')).readlines()
for sentence in f:
    for char in sentence:
        if char.isalnum():
            if char.lower() in vowels:
                vowel_count+=1
            elif char.isdigit():
                number_count+=1
            elif char.lower() not in vowels and char.isdigit()==False:
                consonant_count+=1
            if char.isupper():
                upper_case+=1
            elif char.islower() and char.isdigit()==False:
                lower_case+=1
print ("Number of Vowels : ",vowel_count,"\nNumber of Consonants : ",consonant_count,"\nNumber of Uppercase Characters : ",upper_case,"\nNumber of Lowercase Character : ",lower_case,"\nNumber of Digits : ",number_count)