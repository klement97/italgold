docker cp latest.dump italgold_db_1:/usr/src/app
docker exec italgold_db_1 pg_restore --verbose --clean --no-acl --no-privileges --no-owner -U postgres -d italgold latest.dump
