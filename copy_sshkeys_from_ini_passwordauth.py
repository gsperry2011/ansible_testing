#run this script and pass your ssh password to copy the specified ssh keys to all systems in the
#ansible inventory

def parse_ini(filename):

    #open our .ini file for reading
    f = open(filename, 'r')
    
    content = f.readlines()

    #what we will store our final output in
    ini_file_output = []

    for line in content:

        #filter out commented lines and group headers from input file
        if not (line.lstrip().startswith("#") or line.lstrip().startswith("[")):
            array_including_newlines = []
            array_including_newlines.append(line)

            #removing \n characters from input
            for object in array_including_newlines:
                array_including_blank_entries = []
                newlines = object.split('\n')
                #newlines[0] is to select the string from the list that returns from the split. The split
                #is (data, blank) or (blank, blank) which is dealt which below
                array_including_blank_entries.append(newlines[0])
                
                #removes all blank entries from final list (these are left from removing new lines above)
                array_including_blank_entries = filter(None, array_including_blank_entries)
                
                #at this point array_including_blank_entries is a list of hostnames or ip addresses and ready for use.
                #building our output array
                for system in array_including_blank_entries:
                    ini_file_output.append(system)

    return ini_file_output

def password_auth_ssh_copy_id_from_array_input( sshpassword , input_file, svcacc, sshpubkey ):

    #copy public ssh keys to systems in /etc/ansible/hosts
    import subprocess
    input_array = parse_ini(input_file)

    for system in input_array:

        import os
        
        #check if the system is responding
        pingcheck = os.system("ping -c 1 " + system )

        if pingcheck == 0:

            import time

            # we define the bash command this was vs directly on subprocess because subprocess cannot
            # handle

            #print 'attempting to copy ssh key to %s' % system
            # white space inside quotes. 
            bashcmd = 'sshpass -p %s ssh-copy-id -i %s %s@%s' % ( sshpassword, sshpubkey, svcacc, system )
            print bashcmd
            # intiating the copy of ssh keys to systems in the inventory
            subprocess.call(['bash','-c', bashcmd])

          
        else:
            print 'WARN: %s is not responding, skipping!' % ( system )  
        


import sys

svcacc='root'
sshpassword=sys.argv[1]
sshpubkey='~/.ssh/id_rsa.pub'
input_file='./hosts'

#show time
password_auth_ssh_copy_id_from_array_input(sshpassword, input_file, svcacc, sshpubkey)
