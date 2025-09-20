cat << 'EOF'
CREATE OR EXECUTE INTO LOCAL POSTGRES INSTANCE USING DOCKER

DATABASE INFORMATION
====================
username: postgres
password: password
port:     5432:5432

BASIC CHEAT SHEET
=================
UPDATE schema.table SET column = value WHERE condition; -- Update data in a table
INSERT INTO schema.table (...) VALUES (...);  -- Insert data into a table
DELETE FROM schema.table WHERE condition;     -- Delete data from a table
ALTER TABLE schema.table ADD column datatype; -- Add a column to a table
ALTER TABLE schema.table DROP COLUMN column;  -- Remove a column from a table
DROP TABLE schema.table;                      -- Delete a table
SELECT * FROM schema.table;      -- Select all rows & columns from a table
CREATE SCHEMA name;              -- Create a schema
DROP SCHEMA name;                -- Delete a schema
CREATE TABLE schema.table (...); -- Create a table in a schema
\c dbname                        -- Connect to a database
\dt schema.*                     -- List all tables in a schema
\d schema.table                  -- Describe a table in a schema
\i filename                      -- Execute commands from a file
\q                               -- Quit psql
\l                               -- List all databases
\dn                              -- List all schemas
\dt                              -- List all tables
\di                              -- List all indexes
\df                              -- List all functions
\dv                              -- List all views
\du                              -- List all roles/users
\! command                       -- Execute a shell command
\timing                          -- Toggle timing of SQL commands
\echo text                       -- Print text to the output
\o filename                      -- Send output to a file

OTHER NOTES
===========
- Checkout the Postgres docs here: https://www.postgresql.org/docs/
- The default schema in Postgres is "public"

EOF

# create pg instance if one does not exist
if [ $(docker container list | grep "pgDB" | wc -l) -eq 0 ]; then
  echo "Creating new Postgres Docker Container..."
  docker run --name "pgDB-$(date +%s)" -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
  echo "Created container, waiting 5 seconds before psql into it..."
  sleep 5
  echo
fi

# psql into pg instance
docker exec -it $(docker container list | awk '{print $1}' | grep -v "CONTAINER") psql -U postgres

