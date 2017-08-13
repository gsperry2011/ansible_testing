import subprocess

# ansible inventory .ini file
filename = '/etc/ansible/hosts'
# the public cert that will be placed into authorized_keys
sshpubkey = '/root/.ssh/id_rsa.pub'
# remote system local account
svcacc = 'root'
# password  for remote system local account
sshpassword = ''

#open our .ini file for reading
f = open(filename, 'r')
    
content = f.readlines()
output = []
output2 = []
    
    
for line in content:

#filter out commented lines and group headers from input file
    if not (line.lstrip().startswith("#") or line.lstrip().startswith("[")):
        output.append(line)
            
#removing \n characters from input
for object in output:
    newlines = object.split('\n')
    #newlines[0] is to select the string from the list that returns from the split. The split
    #is (data, blank) or (blank, blank) which is dealt which below
    output2.append(newlines[0])
                
#removes all blank entries from final list (these are left from removing new lines above)
output2 = filter(None, output2)
            
#at this point output2 is a list of hostnames or ip addresses and ready for use.

#copy public ssh keys to systems in /etc/ansible/hosts
for system in output2:
    # we define the bash command this was vs directly on subprocess because subprocess cannot handle
    # white space inside quotes. 
    bashcmd = 'sshpass -p %s ssh-copy-id -i %s %s@%s' % ( sshpassword, sshpubkey, svcacc, system )
    # intiating the copy of ssh keys to systems in the inventory
    subprocess.call(['bash','-c', bashcmd])

    
