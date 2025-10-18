if [ $(docker container list | grep "pgDB" | wc -l) -eq 0 ]; then
	echo "Creating Postgres Docker Container..."
	docker run --name "pgDB-$(date +%s)" -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
	echo "Container Created, Waiting..."
	sleep 5
fi

echo "The password is... password"

docker exec -it $(docker container list | awk '{print $1}' | grep -v "CONTAINER") psql -U postgres
