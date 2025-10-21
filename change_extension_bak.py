import os

for filename in os.listdir('.'):
	if filename.endswith('.txt'):
		#os.rename(filename, filename + '.bak')

		filename_bak = filename + ".bak"

		# Leer el contenido del archivo .txt
		with open(filename, 'r', encoding='utf-8') as f:
			contenido = f.read()

		# Crear el archivo .bak con el mismo contenido
		with open(filename_bak, 'w', encoding='utf-8') as f:
			f.write(contenido)