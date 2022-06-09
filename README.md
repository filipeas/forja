<h1 align="center">Forja</h1>
<h3 align="center">Biblioteca para implementação de algoritmos de deep learning</h3>

## Dependências

Bibliotecas necessárias:

1. matplotlib
2. numpy
3. sklearn
4. pandas
5. cvxopt
6. scipy
7. progressbar33
8. terminaltables
9. gym

As dependências do projeto são:
1. numpy
2. numba (comentado pois ainda está em processo de refatoração)

Há alguns exemplos que dependem de algumas bibliotecas. Veja a lista abaixo dos exemplos e suas dependências:

1. mnist 

Dependências: 
* tensorflow
* numpy

### Windows e linux

Para instalar o tensorflow utilize o anaconda. 

``` 
conda create --name forja python=3.8
```

### Macos

No mac m1 utilize o arquivo environment.yml para instalar as dependências corretas.

```
conda env create --file=./environment.yml --name=forja
```

2. mnist_conv

Dependências:
* tensorflow
* matplotlib

Utilize o conda para instalar o matplotlib com o comando ``` conda install -c conda-forge matplotlib ```.