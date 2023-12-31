## Settings and upgrades

To debug the installed package:

* login to you YunoHost instance
* Go into app shell
* Use `make` targets or `./compose.sh`

```bash
ssh admin@yourdomain.tld
root@yunohost:~# yunohost app shell docker_django_example
...
docker_django_example@testyunohost:/home/yunohost.app/docker_django_example$ make
help                           List all commands
build                          Update/Build docker services
up                             Start docker containers
down                           Stop all containers
restart                        Restart by call "down" and "up"
ps                             List containers
logs                           Display and follow docker logs
shell-app                      go into a interactive bash shell in App container
run-shell-app                  Build and start the App container and go into shell
shell-postgres                 go into a interactive bash shell in App container
systemd-status                 Status of the app SystemD services
systemd-restart                Status of the app SystemD services

```

How to debug a django YunoHost app, take a look into:

* https://github.com/YunoHost-Apps/docker_django_example_ynh#developer-info

## local test

For quicker developing of docker_django_example_ynh in the context of YunoHost app,
it's possible to run make targets like on YunoHost.

e.g.:
```bash
~$ git clone https://github.com/YunoHost-Apps/docker_django_example.git
~$ cd docker_django_example_ynh/
~/docker_django_example$ ./local-test-make.sh
...
+ cd local_test/home_yunohost_app
+ exec make
help                           List all commands
build                          Update/Build docker services
up                             Start docker containers
down                           Stop all containers
restart                        Restart by call "down" and "up"
ps                             List containers
logs                           Display and follow docker logs
shell-app                      go into a interactive bash shell in App container
run-shell-app                  Build and start the App container and go into shell
systemd-status                 Status of the app SystemD services
systemd-restart                Status of the app SystemD services
```

