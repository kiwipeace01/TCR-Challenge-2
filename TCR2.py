import select, socket, sys, queue
'''
location=[]
time=[]

n=int(input())
for i in range(0,n):
    loc,dur=input().split(' ')
    dict[loc]=dur
    location.append(loc)
    time.append(dur)
'''
n=6
location=['Pochinki','School','Gatka','Georgopol','Rozhok','Mylta']
time=['10','11','20','8','15','9']



#Create 3 TCP/IP sockets,one for each truck,and binding them

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s1.setblocking(0)
s1_address=('127.0.0.1',9997)
s1.bind(s1_address)
s1.listen(5)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s2.setblocking(0)
s2_address=('127.0.0.1',9998)
s2.bind(s2_address)
s2.listen(5)

s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s3.setblocking(0)
s3_address=('127.0.0.1',9999)
s3.bind(s3_address)
s3.listen(5)

print("socket making done!")

rlist = [s1,s2,s3]
address=[0,0,0]
wlist = []
errlist=[]
message_queues = {}

file=open(r'C:\Users\Ishika Naik\Desktop\output.txt','w')

count=0
while True:
   
    readable, writable, exceptional = select.select(rlist,wlist,errlist)
    for s in readable:
        
        global status1
        global status2
        global status3
        
        #print("inside readable")
        if s==s1:
            print("Creating a new connection")
            connection, client_address = s.accept()
            message_queues[connection] = queue.Queue()
            print("New connection from Truck1:",client_address)
            #connection.setblocking(0)
            wlist.append(connection)
            address[0]=client_address
            status1='free'

        elif s==s2:
            print("creating a new connection")
            connection, client_address = s.accept()
            message_queues[connection] = queue.Queue()
            print("New connection from Truck2:",client_address)
            #connection.setblocking(0)
            wlist.append(connection)
            address[1]=client_address
            #global status2
            status2='free'

        elif s==s3:
            print("creating a new connection")
            connection, client_address = s.accept()
            message_queues[connection] = queue.Queue()
            print("New connection from Truck3:",client_address)
            #connection.setblocking(0)
            wlist.append(connection)
            address[2]=client_address
            #global status3
            status3='free'
      
    if len(writable)==3:
        for s in writable:
            
            data=(s.recv(1024)).decode('utf-8')

            print(data)

            if count==n:
                file.close()
                
            if data=='free':
                loc=location.pop(0)
                t=time.pop(0)
                info=loc+" "+t
                s.send(str.encode(info))
                
                name=s.getsockname()

                if name[1]==9997:
                    file.write("%s Truck 1\n"%loc)
                    count+=1
                elif name[1]==9998:
                    file.write("%s Truck 2\n"%loc)
                    count+=1
                elif name[1]==9999:
                    file.write("%s Truck 3\n"%loc)
                    count+=1
                    
            elif data=='busy':
                continue
    
              
    for s in exceptional:
        rlist.remove(s)
        if s in wlist:
            rlist.remove(s)
        s.close()
    


#make status global
#create client file
#File Handling






        
