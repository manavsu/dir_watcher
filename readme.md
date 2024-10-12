# Dir Watcher

A distributed file system tracker, that sends up changes to the cloud via gRPC.

## Build

Use `build.sh` to create all executables.

```bash
bash build.sh
```

## Executables

**Executables will be in the `dist` folder.**

### db_init

Run this first to intialize the database.

```
./db_init
```

### dir_watcher_server

The gRPC server that recieves all updates and stores them in a database. Allows allow for databases searches. Next start the server.

```
./dir_watcher_server
```

### dir_watcher_client

The client that keeps track all changes in a directory and uploads them to the server via gRPC. Run this in a seperate window while the server is running. Running the client will create `.vcs` folder which contains an `index.json ` with hashes and `uuid.txt` with the uuid of the dir.

```
./dir_watcher_client
```

### db_dump

Can be used to dump contents of the database.

```
./db_dump
```

### search_client

Can be used to call the gRPC API to search through the database. Make sure you are in the same location as when you ran the client in order to grab the uuid. Alternatively the target uuid can be passes in as an argument.

```
./search_client blue.py
```

```

Path: ./build/search/PYZ-00.pyz, Hash: 2bda360b3233946d32d5e90268b55451b2507eb9, Update Time: 2024-10-11 21:18:17.663374
Path: ./build/search/PYZ-00.toc, Hash: d65bae8c16ceba483dd32173bc11a396b5de8878, Update Time: 2024-10-11 21:18:17.672030
Path: ./build/search/search.pkg, Hash: 56db9d39344ebee00d5ac0703f6826a5cc54f69a, Update Time: 2024-10-11 21:18:17.695974
Path: ./build/search/PKG-00.toc, Hash: e6f2128bce65a6e6528084fc4d34833f7c849dc3, Update Time: 2024-10-11 21:18:17.704801
Path: ./build/search/EXE-00.toc, Hash: 9b13639e486c07e3e5998d6caeb451c92b54588e, Update Time: 2024-10-11 21:18:17.713397
...
```

## Client Features

* uuids to track unique clients
* local dir to save changes
* upload updates to a server via gRPC

## TODO

* [ ] Track a history of changes
* [ ] Better  Search
* [ ] Add .pyi to grpc
* [ ] Add documentation
* [ ] Add auto package generation for proto output

## Things to take into account

* [ ] Max file size
* [ ] Runtimes on large directories
