# Desafio Python
Vaga para Desenvolvedor JR ou PL


### Passo a passo para execução da aplicação

>> Pré-requisitos:
>
>> Docker e docker-compose
>
>>[Instalar docker](https://docs.docker.com/engine/install/ubuntu/)


**1º - Clonar Projeto**
```
    # credenciais https
    $ git clone https://github.com/majurr/desafio.git

```

**2º - Instalar o configurar o git flow [se desejar fazer alterações]**
```
    # para instalar no manjaro
    $ sudo pacman -S git-flow-completion-git

    # passos para configurar git-flow no repositório de trabalho.
    
    1. verifique se a branch atual é dev e existe no repositório remoto por meio do comando "git branch -a".
    
    2º Se precisar mudar de branch repita o comando "git checkout dev".

    3º digite o comando "git flow init" e vai ser necessário confirmar uma série de comandos.
    
    4º confirme se a primeira branch é "main" e pressione "enter" até finalizar as confirmações.
```

>Para saber como usar git-flow [clique aqui](https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04)


**3º - Construir containers**
```
     <!-- Linux - use o make para interpretar o conteúdo do Makefile na raiz do projeto -->

    # construir imagens e containers
    $ make run

    # verificar status dos containers
    $ make st

    # verificar se a api está executando normalmente
    $ make log-api

    # acessar o bash do container fastAPI
    $ make bash

    # para mais comandos acesso o arquivo Makefile

    <!-- Windows -->

    # construir imagens
    : docker-compose build --no-cache

    # levantar containers
    : docker-compose up -d

    # para mais comandos acesse a documentação
```

** Agora acesse o navegador http://127.0.0.1:8000/api/users/**