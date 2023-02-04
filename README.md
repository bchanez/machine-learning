# machine-learning

The goal is to play mario
https://www.smbgames.be/super-mario-bros.php

# build and run in container

```sh
cd docker
sh run.sh
```

# Stop the container

```sh
cd docker
sh stop.sh
```

# Useful command for docker

## Stop a container

```sh
docker ps
docker stop <id>
```

## Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.

```sh
docker system prune -a
```
