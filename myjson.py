import requests
import ast


def main3(val):
    for key2, val2 in val.items():
        print 
        print  "*"*20, key2, ":",  val2,  "*"*20
        main2(key2, val2)


def main2(key, val):
    if type(val) is dict:
        main3(val)

    else:
        key = str(key)
	val = str(val)
        print "%s : %s"  %(key, val)

    

def main():
    print "*"*20
    payload ={"name":"jp"}
    r = requests.post("http://localhost/testphp.php", data=payload)
    myjson = { 'a':'A', 'b':(2, 4), 'c':3.0, ('d',):{'D tuple': "mytuple", "second key":{"second value":"third value"}}  } 
    #for key, val in r.json().items():
    for key, val in myjson.items():
        #print type(key)
        #print type(val) 
        #print str(key)
	main2(key, val)



if __name__=="__main__":
    main()
