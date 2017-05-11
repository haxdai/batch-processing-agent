# batch-processing-agent
Lightweight python agent to retrieve and execute batch tasks

## Easy setup
Run setup script to install required packages
```sh
cd $HOME
sudo curl -s https://raw.githubusercontent.com/haxdai/batch-processing-agent/master/agentsetup.sh | bash -s
```

Clone agent repository
```sh
git clone https://github.com/haxdai/batch-processing-agent.git
```

Make agent.sh executable
```sh
cd $HOME/batch-processing-agent
chmod +x agent.sh
```

Edit agent.sh to set _SERVER_HOST_ and _SERVR_PORT_ environment variables properly, then run install script to add cron job set to execute agent every minute. **This command should be executed as the user who will be responsible for the execution of batch processes**.

```sh
cd $HOME/batch-processing-agent
sh agentinstall.sh
```
