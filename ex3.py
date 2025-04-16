nome_completo = input("Digite seu nome completo: ")

#sobrenome = nome_completo.split()[-1]
#este comando acima só funciona caso a pessoa insira seu nome e somente 1 sobrenome, abaixo, deixarei o código para considerar todo o sobrenome após a escrita de somente 1 nome (sem nomes compostos) :

sobrenome = nome_completo.split()[1:] #[1:] tudo depois do primeiro nome/"texto"

print(sobrenome)