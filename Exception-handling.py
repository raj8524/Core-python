try:
    f = open('sample.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception    # raising custom exception
    var=bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:    #this is executed when try block doesnt raise exception
    print(f.read())
    f.close()
finally:    # will be executed in any situations
    print("Executing Finally...")

print('End of program')