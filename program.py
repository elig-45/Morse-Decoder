userInput = input("Votre date de naissance :")
age = 2019 - int(userInput)
print("Vous avez " + str(age) + " ans.")

userNumber = "rien"
userNumber = input("Entrez un nombre :")
if int(userNumber) != 0 :
	print("Ce nombre est différent de 0.")
else:
	print("Votre nombre est égal à 0.")

file1 = open("text/test.txt", "r")
file1Content = file1.read()
print(file1Content + "\n\n")
file2 = open("text/test2.txt", "r")
file2Content = file2.read()
print(file2Content + "\n\n")

file1 = open("text/test2.txt", "w")
file1.write(file2Content)

file2 = open("text/test.txt", "w")
file2.write(file1Content)

file2ContentCopy = file2Content

file2Content = file1Content
file1Content = file2ContentCopy

print(file1Content + "\n\n" + file2Content)

#def morseDecode(text):
#	code...