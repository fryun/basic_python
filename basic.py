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
    #memory references
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
    b.append(50)
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
    c = print_equality
    print_equality(c, print_equality, "Test 14")
    
    c(a,b, "Test 15")
    

    def single_list(some_list:list):
        result_list = []
        for ls in some_list:
            if type(ls) != list:
                result_list.append(ls)
            else:
                result_list.extend(single_list(ls))
        return result_list
    
    a = [1,2,3,[4,5,6,[7,8,9,[10,11]]]]
    b = single_list(a)
    print_equality(a,b, "Test 16")


    print ("======================== Test 17 init =========================")
    c = "di set di global scope"
    def simple():
        a = 10
        b = 15
        def inner_simple():
            nonlocal a
            global b
            print ("value a (before)(nonlocal):", a)
            print ("value b (before)(global):", b)
            print ("value c:", c)
            print()

            b.append(50000)
            a += 100
            print ("value a (after)(nonlocal):", a)
            print("value b (after)(global):", b)

        inner_simple()

    simple()
    print_equality(a,b, "Test 17")
    
    
    # *args *kwargs
    def simple(a, b, *args, kw, kw2="KW2", **kwargs):
        print ("======================== Test 18 =========================")
        print (a, b, args, kw, kw2, kwargs)
        print ()
    simple (10, 500, 5000, 50000, kw=700, kw3="saya", kw4="kamu")
    
    
    #wajib pake kwargs
    def simple (*, a, b):
        print ("======================== Test 19 =========================")
        print (a, b)
        print ()
    simple (a="Test", b=50000)
    # simple ("Test", 50000) #bakal error
    
    
    print ("======================== Test 20 =========================")
    def simple(a, b):
    # def simple(a, b, c=None):
        print (a, b)
        # if c:
        #     print(c)
            
    some_var01 = simple(10, 20)
    some_var02 = simple(100, 200)
    # enhance_simple = simple(1000, 2000, 5000)
    print ()

    
    print ("======================== Test 21 =========================")
    from datetime import datetime
    import time
    
    print ("OK")    
    def simple_log (message, time=None):
        if not time:
            time=datetime.now()
        print (time, ":", message)
    
    test01 = simple_log(10)
    time.sleep(5)
    test02 = simple_log(50)
    print ()

    def simple_log (message, time=datetime.now()):
        print (time, ":", message)
        
    print ("NOT OK")
    test01 = simple_log(10)
    time.sleep(5)
    test02 = simple_log(50)
    print ()
    
    
    print ("======================== Test 22 =========================")
    list001, list01, list002, list02 = [], [], [], []
    
    def add_item(item, item_list:list=[]):
        item_list.append(item)
        return item_list
    
    print ("OK")
    list001 = add_item(1, list001)
    add_item(2, list001)
    print (list001)
    
    list002 = add_item(10, list002)
    add_item(20,list002)
    print (list002)
    print ()
    
    print ("NOT OK")
    list01 = add_item(1)
    add_item(2, list01)
    print(list01)
    
    list02 = add_item(10)
    add_item(20,list02)
    
    print(list02)
    