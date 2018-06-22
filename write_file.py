def main():
    #https://www.guru99.com/reading-and-writing-files-in-python.html
    f= open("myfile_big.txt","w+")
    for i in range(5000010):
         mobile_number = "958"+str(i) 
         f.write("%s\n" % mobile_number)
    f.close()
if __name__== "__main__":
  main()