import linecache as ln


def Dotheline(filein,fileout):
	allthings = ln.getlines(filein)
	Cliente = 'Codigo Do Cliente: 1\t'
	for index,i in enumerate(allthings):
		print(index,end='\r       ')
		if 'Selecionando cliente:' in i:
			with open(fileout ,'+a') as f:
					Cliente = (f'Codigo Do Cliente:{i.split("Selecionando cliente:")[1]}').replace("\n",'\t')

		if 'Venda de item' in i:
			for b in range(13):

				info = f"{allthings[index+b]}"
				with open(fileout ,'+a') as f:
					f.write(info.replace('\n','\t'))
					
			with open(fileout ,'+a') as f:
					f.write(Cliente)
					f.write('\n')
					Cliente = 'Codigo Do Cliente: 1\t'


if __name__ == '__main__':
	filein= input("Arquivo Inicial: ")
	fileout= f'{input("Nome do Arquivo Final: ")}.csv'
	print('Dependendo do tamanho do Arquivo, essa operação pode demorar um pouco.')
	Dotheline(filein,fileout)
	print('Processo realizado com Sucesso. É recomendado utilizar excel para a melhor formatação')