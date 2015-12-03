__author__ = 'sr'

# 协程练习
# consumer为消费者
# produce负责生产产品
# 消费者最多进行maxTimes次消费操作

# note: this is a generator
def consumer():
    cnt = 0
    maxTimes = 8
    print("consumer initialized")
    while cnt < maxTimes:
        numProduct = yield # waiting for producing

        if not numProduct:
            print("no products")
        else:
            print('consumer: now the number of products is %d' % numProduct )
        cnt += 1
        
    return

def produce( consGen ):
    consGen.send( None )
    numProduct = 0
    print("producer initialized")
    while numProduct < 15:
        try:
            consGen.send( numProduct )
        except:
            print("the consumer is tired....= =")
            break

        # producing
        numProduct += 1
        print('producing: now the number of products is %d' % numProduct )

    print("ending")


    consGen.close()

if __name__ == "__main__":
    cg = consumer()
    produce( cg )
