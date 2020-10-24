#!\bin\bash\

docker-compose up -d --build
docker run -p 15431:80 -e "PGADMIN_DEFAULT_EMAIL=root" -e "PGADMIN_DEFAULT_PASSWORD=root" -d dpage/pgadmin4:4.18 --name "rpk_pgadmin"
echo "Mongo port 47017, L:root P:root"
echo "postgres port 15432, L:root P:root"
echo "pgadmin port 15431, L:root P:root"