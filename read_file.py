def main():
    ## WRITING FILE
    #f= open("guru99.txt","r")
    #f= open("temp/myfile_big_2.txt","w+")
    #for i in range(10):
    #     f.write("This is line %d\r\n" % (i+1))
    #f.close()

    #Open the file back and read the contents
    #f=open("guru99.txt", "r")
    f= open("temp/myfile_big_2.txt","r")
    if f.mode == 'r':
        contents =f.read()
        print(contents)
    #or, readlines reads the individual line into a list
    #    fl =f.readlines()
    #    for x in fl:
    #        print(x)
if __name__== "__main__":
  main()