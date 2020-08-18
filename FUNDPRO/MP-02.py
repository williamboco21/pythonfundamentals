def change_word(ow, s, tr):
   print(ow.replace(s, tr))

original_word = input("Enter the word: ")
sub = input("Enter the substring: ")
to_replace = input("Enter the string to replace the substring: ")
print("")

change_word(original_word, sub, to_replace)
