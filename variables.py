
def print_var_ref(a,b,c,d,name=None):
    print (f"======================== {name} ==============================") 
    print ("id a:", id(a), "|| type :", type(a), "|| val :", a)
    print ("id b:", id(b), "|| type :", type(b), "|| val :", b)
    print ("id c:", id(c), "|| type :", type(c), "|| val :", c)
    print ("id d:", id(d), "|| type :", type(d), "|| val :", d)
    print ()    

def print_equality(a,b,name): 
    """to test the equality of variables"""
    print (f"======================== {name} ==============================") 
    print (f"value a : {a}")
    print (f"value b : {b}")
    print ("id a :", id(a), "|| type a :", type(a))
    print ("id b :", id(b), "|| type b :", type(b))
    print ("a == b :", a == b)
    print ("a is b :", a is b)
    print ()    


if __name__ == '__main__':    
    #variable a memory references
    a = 10
    b = "hello world!"
    c = [a, b]
    d = {
        'a' : a,
        'b' : b,
        'c' : c,
         }
    print_var_ref(a,b,c,d, name="Test memory references")
    
    
    # variable equality
    a = 10
    b = 10.0
    print_equality(a,b,"Test 1")
    
    
    '''
    Mutable object
    list, dict, set, byte array
    '''
    #list
    a = [1,2,3,4]
    b = [1,2,3,4]
    print_equality(a,b,"Test 2")
    
    
    a.append(5)
    b.append(5)
    print_equality(a,b,"Test 3")
    
    
    b = a
    print_equality(a,b,"Test 4")


    b.append(6)
    print_equality(a,b,"Test 5")
    
    #dict
    a = {'saya': 'aku',
         'kamu': 'ya kamu',
         }
    b = {'saya': 'aku',
         'kamu': 'ya kamu',
         }
    print_equality(a,b, "Test 6")   
    
    
    b = a
    print_equality(a,b, "Test 7")
    
    
    b.update({'dia': 'siapa dia'})
    print_equality(a,b, "Test 8")
    
    
    b['kita'] = 'selamanya'
    print_equality(a,b, 'Test 9')
    
    
    #variable equality across class and function
    a = [1,2,3,4]
    class simple:
        def __init__(self, inpt:list):
            self.var_in_class = inpt
        def append_sesuatu(self):
            self.var_in_class.append('tambahin value')
    
    
    b = simple(a)
    print_equality(a, b.var_in_class, "Test 10")
    
    
    b.append_sesuatu()
    print_equality(a, b.var_in_class, "Test 11")


    '''
        Immutable object
        int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes
    '''
    a = "hello world!"
    b = a + " hai"
    print_equality(a, b, "Test 12")
    
    
    a = 10
    b = a + 5.0
    print_equality(a, b, "Test 13")
    
    
    # #Everything is an object
    # print ("id print_equality :", id(print_equality), "|| type a :", type(print_equality))
    # c = print_equality
    # print_equality(c, print_equality, "Test")
    
    # c(a,b, "Test")