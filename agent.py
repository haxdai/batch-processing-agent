# -*- coding: utf-8
import os, time, socket, ssl, re, subprocess, datetime, tempfile, platform, pprint
"""Versión del agente para unix, en python 2.7"""
#@author: Sergio Martínez @SuperSerch
login = os.getlogin()
pid = os.getpid()
uid = os.getuid()
hostname = socket.gethostname()
sys = platform.system()

def getHeader(data):
    "Gets a tuple of seqnumber, type and bytes and cmd"
    p = re.compile('^(\d*)\\|(\d*)\\|(\d*)\\|')
    m = p.match(data)
    return m.groups() + (data[m.end():],)

def executeCmd(cmd):
    "gets a tuple of resultcode, stdout, stderr of a cmd run"
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = result.communicate()
    rc = result.returncode
    return (rc, output, err)

def executeScript(script):
    "gets a tuple of resultcode, stdout, stderr of a script run"
    directory_name = tempfile.mkdtemp()
    script_name = directory_name + "/script.sh"
    with open(script_name, "w") as logfile:
        logfile.write(script)
    result = subprocess.Popen(["/bin/sh", script_name], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = result.communicate()
    rc = result.returncode
    os.remove(script_name)
    os.removedirs(directory_name)
    return (rc, output, err)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
packet = hostname + "\n" + sys + "\n" + login + "\n" + str(pid) + "\n"
HOST, PORT = os.environ['SERVER_HOST'], int(os.environ['SERVER_PORT'])
wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ECDHE-RSA-AES128-SHA")
wrappedSocket.connect((HOST, PORT))
wrappedSocket.send(packet)
res = wrappedSocket.recv(4096)
pprint.pprint(res) #Información recibida
seqid = res.find("\n")
data = getHeader(res)
proc = ()
start = datetime.datetime.now().isoformat()
if data[1]=="1":
    proc = executeCmd(data[3])
if data[1]=="2":
    proc = executeScript(data[3])
if data[1]=="0":
    proc = (0,"No operation executed","")
end = datetime.datetime.now().isoformat()
message = data[0] + "\n" + str(proc[0]) + "\n" + start + "\n" + end + "\n" + str(len(proc[1])) + "\n" + proc[1] + "\n" + str(len(proc[2])) + "\n" + proc[2] + "\n"
wrappedSocket.send(message)
res = wrappedSocket.recv(4096)
res = res + wrappedSocket.recv(4096)
wrappedSocket.close()
pprint.pprint(res) #Información recibida
