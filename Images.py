from PIL import Image

matrix = Image.open('word_matrix.png')
pattern = Image.open ('mask.png')

print (matrix.size)


pattern = pattern.resize((1015, 559))
print(pattern.size)

#word#
x = 0
y = 30
w = 900
h = 475
#----#


#En total 152 letras y para formar la frase necesitamos 8

pattern.putalpha(200)
matrix.paste(pattern,(0,0), pattern)
matrix.show()
