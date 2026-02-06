#!/bin/bash

echo "Esperando a que SQL Server despierte..."
while ! nc -z db 1433; do
  sleep 1
done
echo "SQL Server está listo."

echo "Inicializando Base de Datos y Semillas..."
flask resetdb

echo "Lanzando MoSame Backend..."
exec flask run --host=0.0.0.0 --port=5000 --debug