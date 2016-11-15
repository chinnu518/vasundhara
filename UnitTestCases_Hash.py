#Unit TestCases:

import Hash as hash

obj = hash.HashAlgorthim()
    
hash_val =  obj.hash("leepadg")
str = obj.reverse_hash(hash_val)
assert(str == 'leepadg')
hash_val =  obj.hash("animal")
str = obj.reverse_hash(hash_val)
assert(str == 'animal')
hash_val =  obj.hash("topper")
str = obj.reverse_hash(hash_val)
assert(str == 'topper')





