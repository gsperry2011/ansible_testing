
filename = '/etc/ansible/hosts'

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
            
print output2

