# Vet Sys

## Repositório utilizado para o BackEnd da aplicação Vet Sys. Sistema de Gerenciamento de Clínicas Veterinárias.

### Vídeo de apresentação

<https://www.youtube.com/watch?v=82jaOxmkc_Y>

### Para desenvolver

I)  Clone o repositório.
```console
$ git clone https://github.com/ollyvergithub/PosGraduacaoTccVetSysBackEnd.git
```

II)  Crie um Virtualenv com Python.
```console
$ python -m venv venv
```

III.  Ative o Virtualenv.
```console
$ source venv/bin/activate
```

IV.  Instale as dependências.
```console
$ pip install -r requirements/local.txt
```

V.  Crie o Banco de Dados PostgreSQL.
```console
$ createdb vet_sys -U postgres
```

V.  Rode as Migrações.
```console
$ python manage.py migrate
```

V.  Rode os Testes.
```console
$ pytest
```



