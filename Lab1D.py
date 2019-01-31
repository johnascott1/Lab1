#Phrase entered by user
userPhrase = str(input("Enter a word or phrase."))
#I used the split method to convert 'userPhrase' into a list
userPhraseList = userPhrase.split(" ")
#in the following for-loop, this will hold a single item from 'UserPhraseList
camelCaseWord = ""
#this will be the user-specified phrase converted to camel notation
camelCasePhrase = ""
for word in userPhraseList:
    if word == userPhraseList[0]:
        camelCaseWord = word.lower()
    else:
        camelCaseWord = word[0].upper() + word[1:].lower()
    camelCasePhrase += camelCaseWord
print(camelCasePhrase)



