# batch-processing-agent
Lightweight python agent to retrieve and execute batch tasks

## Easy setup (Debian-based Linux)

Set environment variables SERVER_HOST and SERVER_PORT
```sh
export SERVER_HOST=192.168.0.1
export SERVER_PORT=1026
```

Run install script
```sh
curl -s https://raw.githubusercontent.com/haxdai/batch-processing-agent/master/agentsetup.sh | bash -s
```

Installation script installs required packages for Debian-based Linux distributions and sets a cron job to execute the python agent every minute.
