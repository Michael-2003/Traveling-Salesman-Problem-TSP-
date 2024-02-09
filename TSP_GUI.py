from tkinter import*
root= Tk()

from sys import maxsize
v = 4

root.geometry("700x500")

root.configure(bg='white') 


def travelling_salesman_function(graph, s):
    vertex = []
    l=0
    for i in range(v):
        if i != s:
            vertex.append(i)

    kk=0
    min_path = maxsize
    while True:
        current_cost = 0
        k = s
        l+=1
        for i in range(len(vertex)):
            current_cost += graph[k][vertex[i]]
            k = vertex[i]
        
        current_cost += graph[k][s]

        kk=kk+30
        
        frame1=Label(root,text=f'{l} Route: {current_cost}',background="white",font="100")
        frame1.place(x=0,y=100+kk)

        
        min_path = min(min_path, current_cost)
        
        if not next_perm(vertex):
            break
       
    frame2=Label(root,text=f'Best Route Distance : {min_path}',background="white",font="100")
    frame2.place(x=0,y=100+kk+kk)

    return min_path

def next_perm(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True


s = 0

graph=[]
graphf=[]


entry=Entry(root,width=50,bg="#ADD8E6",fg="black")
entry.pack()




def addlist():
    u=entry.get()
    graphf.append(list(u))
    print(graphf)

    for j in graphf:
        f=""
        j.append(",")
        l=[]  
        for i in j:
                if i=="," :
                    l.append(f)
                    f=""
                else:
                    f=f+i
        for p in l:
            if p=="":
                x=FALSE
            else:
                x=TRUE
        if x:
            ll=[]
            for h in l:
                ll.append(int(h))
            graph.append(ll)
    labellabel=Label(root,text=graph,bg="white")
    labellabel.place(x=1,y=80)
    print(graph)
    entry.delete(0,END)



def addlast():
    res = travelling_salesman_function(graph,s)
    print(res)



additem=Button(root,text="Add",command=addlist,bg="white").pack()

additem=Button(root,text="Show",command=addlast,bg="white").pack()




root.mainloop()
