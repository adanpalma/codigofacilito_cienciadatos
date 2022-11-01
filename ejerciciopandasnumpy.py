import  pandas as pd
import numpy as np

usuarios = pd.read_csv('users.csv')
print(usuarios)

#ejercicio 1
#Mostrar en consola el nombre de todos los usuarios cuya edad se encuentre en el rango de 10 a 20 y 40 a 70.
age = 'age'
print('*Mostrar en consola el nombre de todos los usuarios cuya edad se encuentre en el rango de 10 a 20 y 40 a 70.')
print(usuarios[((usuarios[age] >= 10) & (usuarios[age]<=20)) | ((usuarios[age] >= 40) & (usuarios[age]<=70))][['name','age']],"\n\n")


print("*Mostrar en consola todos los usuarios con correo electrónico.")
print("print(usuarios.dropna(axis=0,subset=['email']))")
print(usuarios.dropna(axis=0,subset=['email']),"\n\n")

print("*print(usuarios[~pd.isnull(usuarios['email'])])")
print(usuarios[~pd.isnull(usuarios['email'])],"\n\n")


print("*Mostrar en pantalla el nombre y correo electrónico del usuario más joven en Canadá.")
print("usuarios[usuarios['country']== 'Canada'].sort_values(['age']).head(1)")
print(usuarios[usuarios['country']== 'Canada'].sort_values(['age']).head(1),"\n\n")



print("*Mostrar en pantalla el nombre y correo electrónico del usuario más viejo en Canada.")
print("usuarios[usuarios['country']== 'Canada'].sort_values(['age']).tail(1)")
print(usuarios[usuarios['country']== 'Canada'].sort_values(['age']).tail(1),"\n\n")



print("*Listar en consola los 3 países con menor cantidad de usuarios.")
print("usuarios.groupby('country')['country'].count().sort_values().head(3)")
print(usuarios.groupby('country')['country'].count().sort_values().head(3),"\n\n")


print("*Obtener el país con mayor cantidad de usuarios cuya edad sea mayor a 50.")
print("usuarios[usuarios['age'] > 50].groupby('country')['country'].count().sort_values().tail(1)")
print(usuarios[usuarios['age'] > 50].groupby('country')['country'].count().sort_values().tail(1),"\n\n")


print("*Obtener el país con mayor promedio de edad.")
print("usuarios.groupby('country')['age'].mean().sort_values().tail(1)")
print(usuarios.groupby('country')['age'].mean().sort_values().tail(1),"\n\n")

print("*Mostrar en consola el país con más hombres.")
print("usuarios[usuarios['gender'] == 'male'].groupby('country')['country'].count().sort_values().tail(1))")
print(usuarios[usuarios['gender'] == 'male'].groupby('country')['country'].count().sort_values().tail(1),"\n\n")


print("*Mostrar en consola el nombre, username y edad de todos los usuarios cuya edad ed mayor a 10 y no sean del país México, Brasil y Canadá.")
print("usuarios[(usuarios['age']>10) & ~(usuarios['country'].isin(['Mexico','Brasil','Canada']))][['name','username','age']]")
print(usuarios[(usuarios['age']>10) & ~(usuarios['country'].isin(['Mexico','Brasil','Canada']))][['name','username','age']],"\n\n")



print("*Mostrar en consola el código postal de todos los usuarios de México.")
print("usuarios[usuarios['country'] == 'Mexico']['postcode']")
print(usuarios[usuarios['country'] == 'Mexico']['postcode'],"\n\n")


print("*Obtener la edad que más se repite en el DataFrame.")
print("usuarios['age'].mode()")
print(usuarios['age'].mode(),"\n\n")
print("(usuarios['age'].value_counts().index[0])")
print((usuarios['age'].value_counts().index[0]),"\n\n")


print("*Obtener la edad que menos se repite en el DataFrame.")
print("(usuarios['age'].value_counts().index[-1])")
print((usuarios['age'].value_counts().index[-1]))

