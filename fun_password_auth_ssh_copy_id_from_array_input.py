def password_auth_ssh_copy_id_from_array_input( sshpassword , input_file, svcacc, sshpubkey ):

    from fun_parse_ini import parse_ini
    #copy public ssh keys to systems in /etc/ansible/hosts
    import subprocess
    input_array = parse_ini(input_file)

    for system in input_array:
        # we define the bash command this was vs directly on subprocess because subprocess cannot
        # handle

        print 'attempting to copy ssh key to %s' % system
        # white space inside quotes. 
        bashcmd = 'sshpass -p %s ssh-copy-id -i %s %s@%s' % ( sshpassword, sshpubkey, svcacc, system )
        # intiating the copy of ssh keys to systems in the inventory
        subprocess.call(['bash','-c', bashcmd])
