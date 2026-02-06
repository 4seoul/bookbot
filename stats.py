import json, sys

def sort_on(items):
    return items["num"]

def get_num_words():

   with open(sys.argv[1]) as f: 
      file_contents = f.read() # Reads the content of the file and saves it to a new variable
      temp = file_contents.lower() # Creates a temp copy of the file_contents variable, with all chars set as lower case

      temp.split() #Splitting the temp copy into a list

      mydict={}

      for length in temp: # For loop iterating over each item in the temp list and counting each time an item appears
         try:
            mydict[length]+=1
         except:
            mydict[ length]=1
      
      json.dumps(mydict)

      if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

      
      print("""============ BOOKBOT ============
      Analyzing book found at books/frankenstein.txt...""")

      print("""----------- Word Count ----------
      Found""",len(temp.split()),"""total words""") # splits temp into a list of words and gets the total length of the list

      print("""--------- Character Count -------""")
      for x, y in sorted(mydict.items(), reverse=True, key=lambda item: item[1]): #Loops through the key, value pairs in the dict, which is each character : how many times it appears
         if x.isalpha() == True:
            print(f"{x}: {y}")
