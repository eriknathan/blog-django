#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

echo "🟡 Iniciando o Postgres"
wait_psql.sh
echo "🟡 Realizando Collectstatic"
collectstatic.sh
echo "🟡 Realizando Migrate"
migrate.sh
echo "✅ Iniciando aplicação"
runserver.sh