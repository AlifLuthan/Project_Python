import paramiko
import sys

#cla
username  = sys.argv[1]
password  = sys.argv[2]
port      = sys.argv[3]

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('youIPv4', username=hostname, password=password , port=port)
stdin, stdout, stderr = client.exec_command('whoami')
for line in stdout:
    file_path = 'result.txt'
    sys.stdout = open(file_path, "w")
    print(line.strip("\n"))
