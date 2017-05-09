#!/bin/bash
AGENT_DIR="$HOME/batch-processing-agent"
#Install python
dpkg -s python > /dev/null 2>&1
if [ ! $? -eq 0 ]; then
	apt-get install -y python
fi

#Install git
dpkg -s git > /dev/null 2>&1
if [ ! $? -eq 0 ]; then
	apt-get update > /dev/null 2>&1 \
	&& apt-get install -y git
fi

#Clone repository if needed
if [ ! -d "$AGENT_DIR" ]; then
  cd $HOME && git clone https://github.com/haxdai/batch-processing-agent.git
fi

#Setup agent
if [ -d "$AGENT_DIR" ]; then
  crontab -l  | grep '/batch-processing-agent/agent.py' -q > /dev/null 2>&1
  if [ ! $? -eq 0 ]; then
    echo "Adding crontab Job for agent"
    (echo "*/1 * * * * python $HOME/batch-processing-agent/agent.py") | crontab -
  else
    echo "Job exists, nothing to do"
  fi
fi
