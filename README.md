<h1 align="center">Forja</h1>
<h3 align="center">Biblioteca para implementação de algoritmos de machine learning e deep learning</h3>

## Dependências

As dependências do projeto são:
1. numpy
2. numba (comentado pois ainda está em processo de refatoração)

Há alguns exemplos que dependem de algumas bibliotecas. Veja a lista abaixo dos exemplos e suas dependências:

1. mnist (tensorflow)

* Windows

Para instalar o tensorflow utilize o anaconda. 

``` 
conda create --name forja python=3.8
```

* Macos

No mac m1 utilize o arquivo environment.yml para instalar as dependências corretas.

```
conda env create --file=./environment.yml --name=forja
```