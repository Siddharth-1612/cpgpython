def main():
    t=()
    print("it is an empty tuple: ",t)
    t=(0,)
    print("it is a one item tuple: ",t)
    t=(0,'nvgpf',5.3)
    print("3 item tuple",t)
    t=('abc',('efea','feif'))
    print(t[1][0])
    print("nested tuple: ",t)
    t=tuple('AMAZE')
    print("each item in the tuple:",t)
    print(t[1])
    print(t[1:3])
    print(len(t))
main()