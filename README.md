# batch-processing-agent
Lightweight python agent to retrieve and execute batch tasks

## Easy setup (Debian-based Linux)

Set environment variables for batch-processing server SERVER_HOST and SERVER_PORT
```sh
export SERVER_HOST=192.168.0.1
export SERVER_PORT=1026
```

Run setup script to install required packages
```sh
cd $HOME
sudo curl -s https://raw.githubusercontent.com/haxdai/batch-processing-agent/master/agentsetup.sh | bash -s
```

Run install script to install agent as a cron job executed every minute. **This command should be executed as the user who will be responsible for the execution of batch processes**.

```sh
cd $HOME/batch-processing-agent
sh agentinstall.sh
```
