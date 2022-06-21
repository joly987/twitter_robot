from PyDictionary import PyDictionary
dictionary=PyDictionary()

word = "faith"
definition = dictionary.meaning(word)

print (word + ": " + definition["Noun"][0])
