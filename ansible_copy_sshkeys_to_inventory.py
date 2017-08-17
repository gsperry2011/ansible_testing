#run this script and pass your ssh password to copy the specified ssh keys to all systems in the
#ansible inventory

from fun_password_auth_ssh_copy_id_from_array_input import password_auth_ssh_copy_id_from_array_input
import sys

svcacc='root'
sshpassword=sys.argv[1]
sshpubkey='/root/.ssh/id_rsa.pub'
input_file='/etc/ansible/hosts'


password_auth_ssh_copy_id_from_array_input(sshpassword, input_file, svcacc, sshpubkey)
