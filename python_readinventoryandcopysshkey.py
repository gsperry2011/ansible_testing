from fun_parse_ini import parse_ini

input_file = 'test.ini'
sshpassword = ""
sshpubkey = "/root/.ssh/id_rsa.pub"
svcacc = "root"


#copy public ssh keys to systems in /etc/ansible/hosts
import subprocess
input_array = parse_ini(input_file)

for system in input_array:
    # we define the bash command this was vs directly on subprocess because subprocess cannot handle
    # white space inside quotes. 
    bashcmd = 'sshpass -p %s ssh-copy-id -i %s %s@%s' % ( sshpassword, sshpubkey, svcacc, system )

    # intiating the copy of ssh keys to systems in the inventory
    subprocess.call(['bash','-c', bashcmd])
