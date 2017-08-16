#run this script and pass your ssh password to copy the specified ssh keys to all systems in the
#ansible inventory

from fun_password_auth_ssh_copy_id_from_array_input import password_auth_ssh_copy_id_from_array_input

password_auth_ssh_copy_id_from_array_input(svcacc=(sys.argv[1]), sshpassword=(sys.argv[2]), sshpubkey='/root/.ssh/id_rsa.pub')
