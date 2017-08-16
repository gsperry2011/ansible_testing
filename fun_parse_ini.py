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


                for system in array_including_blank_entries:

                    ini_file_output.append(system)


    return ini_file_output
