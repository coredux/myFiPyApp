__author__ = 'sr'



def accumulate():
   tally = 0
   while 1:
        next = yield
        if next is not None:
            print("next = %d " % next )
        else:
            return tally
        tally += next

def printGen():
    while True:
        next = yield
        if next is not None:
           print("printGen(): next = %d " % next )
        else:
            return

def gather_tallies(tallies):
    while 1:
        # 每次收到外层的值时，都直接向accumulate()传入值，直到传入None时，执行generator到结束，返回加和
        tally = yield from accumulate()
        yield from printGen()
        print("tally = %d " % tally )
        tallies.append(tally)


if __name__ == "__main__":

    tallies = []
    acc = gather_tallies(tallies)

    acc.send(None) # Ensure the accumulator is ready to accept values

    for i in range(4):
        print("sending :%d" % i )
        acc.send(i)
    print("sending None")
    acc.send(None) # Finish the first tally


    print( tallies )

    for i in range(5):
        print("sending :%d" % i )
        acc.send(i)
    print("sending None")
    acc.send(None) # Finish the second tally

    print( tallies )

