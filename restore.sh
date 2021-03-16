docker cp latest.dump italgold_db_1:/usr/src/app
docker exec italgold_db_1 psql -U postgres -d postgres -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'italgold' AND pid <> pg_backend_pid();"
docker exec italgold_db_1 dropdb --if-exists -U postgres italgold
docker exec italgold_db_1 createdb -U postgres italgold
docker exec italgold_db_1 pg_restore --verbose --no-acl --no-privileges --no-owner -U postgres -d italgold latest.dump
