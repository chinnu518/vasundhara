class HashAlgorthim:
	   def __init__(self):
		   pass
	#pseudo code for Hash function 
     def hash (self, s):
     		h = 7
        letters = "acdegilmnoprstuw"
        for i in range(0, len(s)):
          h = (h * 37 + letters.find(s[i]))
        return h

   	 def reverse_hash(self, num):
    		h = 7
    		arr = []
    		letters = "acdegilmnoprstuw"
    		while num > h:
			    r = num%37
			    arr.append(letters[r])
        	num = num/37

		    # reverse the Array
        for i in range(0, len(arr)/2):
			    temp = arr[i]
			    arr[i] = arr[len(arr)-1-i]
			    arr[len(arr)-1-i] = temp
    	  return ''.join(arr)

#Unit TestCases:
obj = HashAlgorthim()
    
hash_val =  obj.hash("leepadg")
str = obj.reverse_hash(hash_val)
assert(str == 'leepadg')
hash_val =  obj.hash("animal")
str = obj.reverse_hash(hash_val)
assert(str == 'animal')
hash_val =  obj.hash("topper")
str = obj.reverse_hash(hash_val)
assert(str == 'topper')





