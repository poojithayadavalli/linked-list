class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

def display(head):
    l=[]
    while head:
        l.append(str(head.data))
        head=head.next
    print("->".join(l))

def linkedList(head,node):
    if head==None:
        node.next=head
        head=node
    elif head.data>=node.data:
        node.next=head
        head=node
    else:
        temp=head
        while temp and temp.next and temp.next.data<node.data:
            temp=temp.next
        node.next=temp.next
        temp.next=node
    return head

llist=list(map(int,input().split()))
head=None
for i in range(len(llist)):
    node=Node(llist[i])
    head=linkedList(head,node)
display(head)
            
