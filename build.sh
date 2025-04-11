#!/usr/bin/env bash

# Ativa o modo de erro: o script para se qualquer comando falhar
set -o errexit

# Instala as dependências do projeto
pip install -r requirements.txt

# Realiza as migrações
python manage.py migrate

# Coleta os arquivos estáticos
python manage.py collectstatic --no-input
