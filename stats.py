import json, sys



def sort_on(items):
    return items["num"]

def get_num_words():

   with open(sys.argv) as f: 
      file_contents = f.read()
      temp = file_contents.lower()

      temp.split()

      mydict={}

      
      for length in temp:
         try:
            mydict[length]+=1
         except:
            mydict[ length]=1
      
      json.dumps(mydict)

      
      print("""============ BOOKBOT ============
      Analyzing book found at books/frankenstein.txt...""")
            
      print("""----------- Word Count ----------
      Found""",len(temp.split()),"""total words""")

      print("""--------- Character Count -------""")
      for x, y in sorted(mydict.items(), reverse=True, key=lambda item: item[1]):
         if x.isalpha() == True:
            print(x, ":",y)

      
      
      




