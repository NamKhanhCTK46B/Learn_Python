file_name = input ("Input the Filename: ")

f_exten = file_name.split (".")

print ("The extension of the file is: " + repr(f_exten[-1]))