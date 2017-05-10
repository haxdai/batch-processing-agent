#!/bin/bash
AGENT_DIR="$HOME/batch-processing-agent"

if [ -f /etc/lsb-release ] || [ -f /etc/debian_version ]; then
  echo "Installing dependencies in debian-based machine..."

	#Install python
	dpkg -s python > /dev/null 2>&1
	if [ ! $? -eq 0 ]; then
		echo "Installing python..."
		apt-get install -y python
	fi

	#Install git
	dpkg -s git > /dev/null 2>&1
	if [ ! $? -eq 0 ]; then
		echo "Installing git..."
		apt-get update > /dev/null 2>&1 \
		&& apt-get install -y git
	fi
elif [ -f /etc/centos-release ]; then
  echo "Installing dependencies in CentOS machine..."

	#Install git
	rpm -q git > /dev/null 2>&1
	if [ ! $? -eq 0 ]; then
		echo "Installing git..."
		yum -y install git-all
	fi
fi
