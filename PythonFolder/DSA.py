'''until now written all DSA practice progs in PythonBasics.py
But now I will continue remaining DSA practice in this file'''

# print('yashika  '.isalpha())

# def PostfixToInfix(exp):
#     stack=[]
#     for i in exp:
#         if i.isalpha():
#             stack.append(i)
#         else:
#             a,b=stack.pop(),stack.pop()
#             stack.append(f"({b}{i}{a})")
#     return ''.join(stack)

# print(PostfixToInfix('ab*c+'))


# def infix_to_postfix(expression):
#   stack = []
#   postfix_expression = []

#   for token in expression[::-1]:
#     if token.isalpha():
#       postfix_expression.append(token)
#     elif token == ")":
#       stack.append(token)
#     elif token == "(":
#       while stack[-1] != ")":
#         postfix_expression.append(stack.pop())
#       stack.pop()
#     else:
#       while len(stack) > 0 and (precedence(stack[-1]) >= precedence(token)):
#         postfix_expression.append(stack.pop())
#       stack.append(token)

#   while len(stack) > 0:
#     postfix_expression.append(stack.pop())

#   return "".join(postfix_expression[::-1])

# def precedence(token):
#   if token == "+" or token == "-":
#     return 1
#   elif token == "*" or token == "/":
#     return 2
#   else:
#     return 0

# print(infix_to_postfix("(A+B)/(C-D)"))

# def removeConsecutiveDuplicates(s):
#     stack=[]
#     for i in s:
#         if not stack:
#             stack.append(i)
#         elif stack[-1]!=i:
#             stack.append(i)
#     return "".join(stack)

# s="abbccbcd"
# print(removeConsecutiveDuplicates(s))

# def removePairDuplicate(s):
#     stack = []
#     for i in s:
#         if not stack:
#             stack.append(i)
#         elif stack[-1] == i:
#             stack.pop()
#         else:
#             stack.append(i)
#     return ''.join(stack)


# s = "aaaa"
# print(removePairDuplicate(s))
# from collections import deque
# d=deque()
# d.append(10)
# d.append(20)
# d.append(30)
# d.appendleft(40)
# print(d)
# print(d.pop())
# print(d.popleft())
# print(d)
# d=deque({1:'a',2:'b',3:'c',4:'d'})
# print(d)
# d.extendleft({5,6})
# print(d)

# l=[None]*3
# print(l)
# l[0]=2
# print(l)

# l=[0 * 3]
# print(l)
# l[0]=2
# print(l)

# print(5 % 0)

# l = [1, 2, 3, 3]
# l.remove(2)
# print(l)

# print("hi")


# def removePairDuplicate(s):
#     stack = []
#     for i in s:
#         if not stack:
#             stack.append(i)
#         elif stack[-1] == i:
#             stack.pop()
#         else:
#             stack.append(i)
#     return ''.join(stack)


# s = "bccd"
# print(removePairDuplicate(s))
# print("shinchan")

# for i in ['1,2,3,4']:
#     print(i, end="  ")

# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.prev=None
#         self.next=None

# class MyDeque:
#     def __init__(self):
#         self.front=None
#         self.rear=None
#         self.sz=0

#     def erase

# print(3**2)


import math
from collections import deque


# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None


# def inorder(root):
#     if root == None:
#         return
#     if root.left != None:
#         inorder(root.left)
#     print(root.key, end=" ")
#     if root.right != None:
#         inorder(root.right)
#     return

# def preorder(root):
#     if root == None:
#         return
#     print(root.key, end=" ")
#     if root.left != None:
#         preorder(root.left)
#     if root.right != None:
#         preorder(root.right)
#     return

# def heightOFBT(root):
#     if root == None:
#         return 0
#     count1 = 0
#     count2 = 0
#     if root.left != None:
#         count1 += heightOFBT(root.left)
#     if root.right != None:
#         count2 += heightOFBT(root.right)
#     return (max(count1, count2)+1)


# def TotalNodesOFBT(root):
#     if root == None:
#         return 0
#     count = 0
#     if root.left != None:
#         count += TotalNodesOFBT(root.left)
#     if root.right != None:
#         count += TotalNodesOFBT(root.right)
#     return (count+1)

# def heightOFBT(root):
#     if root == None:
#         return 0
#     lh = heightOFBT(root.left)
#     rh = heightOFBT(root.right)
#     return (max(lh, rh)+1)

# def TotalNodesOFBT(root):
#     if root == None:
#         return 0
#     lh = TotalNodesOFBT(root.left)
#     rh = TotalNodesOFBT(root.right)
#     return (lh+rh+1)


# def levelOrderTraversal(root):
#     if root == None:
#         return
#     q = deque()
#     q.append(root)
#     while (len(q) != 0):
#         ele = q.popleft()
#         print(ele.key, end=" ")
#         if ele.left != None:
#             q.append(ele.left)
#         if ele.right != None:
#             q.append(ele.right)

# def MaxOfBT(root):
#     if root == None:
#         return float('-inf')
#     # Lmax = 0
#     # Rmax = 0
#     Lmax = MaxOfBT(root.left)
#     Rmax = MaxOfBT(root.right)
#     return max(Lmax, Rmax, root.key)


# def isIdentical(root, root1):
#     if (root == None or root1 == None) and (root != root1):
#         return False
#     elif (root == None and root1 == None):
#         return True
#     elif root.key != root1.key:
#         return False
#     elif isIdentical(root.left, root1.left) and isIdentical(root.right, root1.right):
#         return True
#     return False


# def isIdentical(root1, root2):
#     if root1 is None and root2 is None:
#         return True
#     if root1 is not None and root2 is not None:
#         if (root1.key != root2.key):
#             return 0
#         return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
#     return False


# def heightOFBT(root):
#     if root == None:
#         return 0
#     lh = heightOFBT(root.left)
#     rh = heightOFBT(root.right)
#     return (max(lh, rh)+1)

# def isBalanced(root):
#     if root == None:
#         return True
#     lst = heightOFBT(root.left)
#     rst = heightOFBT(root.right)
#     print(lst, rst)
#     if abs(lst-rst) > 1:
#         return False
#     return True

# def isIdentical(root, root1):
#     if root == None and root1 == None:
#         return True
#     if root != None and root1 != None:
#         q1 = deque()
#         q2 = deque()
#         q1.append(root)
#         q2.append(root1)
#         while (len(q1) != 0 and len(q2) != 0):
#             # print(q1, q2)
#             ele1 = q1.popleft()
#             ele2 = q2.popleft()
#             if ele1.key != ele2.key:
#                 return False
#             if ele1.left != None:
#                 q1.append(ele1.left)
#             if ele1.right != None:
#                 q1.append(ele1.right)
#             if ele2.left != None:
#                 q2.append(ele2.left)
#             if ele2.right != None:
#                 q2.append(ele2.right)
# print(q1, q2)
#     if (len(q1) == 0 and len(q2) == 0):
#         return True
#     else:
#         return False
# return False

# def MaxOfBT(root):
#     if root==None:
#         return root
#     m=float('-inf')
#     q=deque([root])
#     while q:
#         ele=q.popleft()
#         if ele.key>m:
#             m=ele.key
#         if ele.left!=None:
#             q.append(ele.left)
#         if ele.right!=None:
#             q.append(ele.right)
#     return m

# def isSumProperty(root):
#     if root==None:
#         return True
#     q=deque([root])
#     while q:
#         ele=q.popleft()
#         if ele.left==None and ele.right==None:
#             continue
#         if ele.left==None:
#             ele.left.key=Node(0)
#         if ele.right==None:
#             ele.right=Node(0)
#         if ele.key!=ele.left.key+ele.right.key:
#             return False
#         if ele.left.key!=0:
#             q.append(ele.left)
#         if ele.right.key!=0:
#             q.append(ele.right)
#     return True


# def TotalNodesOfBT(root):
#     if root==None:
#         return 0
#     q=deque([root])
#     count=0
#     while q:
#         ele=q.popleft()
#         count+=1
#         if ele.left!=None:
#             q.append(ele.left)
#         if ele.right!=None:
#             q.append(ele.right)
#     return count

# def HeightOfBT(root):
#     if root==None:
#         return 0
#     q=deque([(root,1)])
#     while q:
#         ele,depth=q.popleft()
#         if ele.left!=None:
#             q.append((ele.left,depth+1))
#         if ele.right!=None:
#             q.append((ele.right,depth+1))
#     return depth

# def printKDist(root,k):
#     if root==None:
#         return
#     q=deque([(root,1)])
#     while q:
#         ele,depth=q.popleft()
#         if k<1:
#             print("write valid dist")
#         if depth==k:
#             print(ele.key,end=" ")
#         if depth>k:
#             break
#         if ele.left!=None:
#             q.append((ele.left,depth+1))
#         if ele.right!=None:
#             q.append((ele.right,depth+1))
#     return (" ")


# root = None
# root = Node(0)
# root.left = Node(0)
# root.right = Node(0)
# root.left.left = Node(0)
# root.left.right = Node(0)
# root.left.right.left = Node(0)
# root.left.right.right = Node(0)
# root.left.right.right.left = Node(90)
# root.right.right = Node(0)

# root1 = None
# root1 = Node(0)
# root1.left = Node(0)
# root1.right = Node(0)
# root1.left.left = Node(0)
# root1.left.right = Node(0)
# root1.left.right.left = Node(0)
# root1.left.right.right = Node(0)
# root1.right.right = Node(0)
# root1.right.left = Node(0)


# root=None
# root=Node(1)
# root.left=Node(4)
# root.right=Node(3)
# root.left.left=Node(5)
# root.left.right=Node(6)
# root.left.left.left=Node(7)
# root.left.left.right=Node(8)

# inorder(root)
# preorder(root)
# print(heightOFBT(root))
# print(TotalNodesOFBT(root))
# levelOrderTraversal(root)
# print(MaxOfBT(root))
# print(isIdentical(root, root1))
# print(isBalanced(root))
# print(isSumProperty(root))
# print(MaxOfBT(root))
# print(TotalNodesOfBT(root))
# print(HeightOfBT(root))
# print(printKDist(root,10))

# a = 1, 2
# print(type(a))

# print(type(-math.inf))
# print(float('-inf'))

# q = deque()
# q.append(None)
# print(q)
# print(None == 3)

# a, b = 0, 0
# print(b)


# queue = deque((2, 0))
# s = queue.popleft()
# print(s)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# def SearchInBST(root,ele):
#     if root==None:
#         return False
#     if root.key==ele:
#         return True
#     elif ele<root.key:
#         return SearchInBST(root.left,ele)
#     elif ele>root.key:
#         return SearchInBST(root.right,ele)
#     return False

# def SearchInBST(root,ele):
#     count=1
#     while root!=None:
#         if root.key==ele:
#             print(f"element found at {count} level")
#             return True
#         elif root.key<ele:
#             root=root.right
#             count+=1
#         elif root.key>ele:
#             root=root.left
#             count+=1
#     return False


# def InsertInBST(root,ele):
#     item=Node(ele)
#     if root==None:
#         root= item
#         return root
#     elif root.key==ele:
#         return root
#     elif root.key>ele:
#         InsertInBST(root.left,ele)
#         return root
#     elif root.key<ele:
#         InsertInBST(root.right,ele)
#         return root

# def InsertInBST(root,ele):
#     item=Node(ele)
#     root1=root
#     while True:
#         if root1.key==ele:
#             print("element cannot be inserted")
#             return root
#         elif root1.key>ele:
#             if root1.left!=None:
#                 root1=root1.left
#             else:
#                 root1.left=item
#                 return root
#         elif root1.key<ele:
#             if root1.right!=None:
#                 root1=root1.right
#             else:
#                 root1.right=item
#                 return root

# def printBST(root):
#     if root==None:
#         return
#     q=deque([root])
#     while q:
#         ele=q.popleft()
#         print(ele.key,end=" ")
#         if ele.left!=None:
#             q.append(ele.left)
#         if ele.right!=None:
#             q.append(ele.right)


# def FloorInBST(root,ele):
#     root1=root
#     count=1
#     res=None
#     if root1==None:
#         return
#     while True:
#         if root1.key==ele:
#             print(f"floor of given elemnt found at {count} level")
#             return root1
#         elif root1.key<ele:
#             res=root1
#             if root1.right!=None:
#                 root1=root1.right
#                 count+=1
#             else:
#                 print(f"floor of given elemnt found at {count} level")
#                 return res
#         else:
#             if root1.left!=None:
#                 root1=root1.left
#                 count+=1
#             else:
#                 return res


# def MinInBST(root):
#     if root==None:
#         return None
#     root1=root
#     while root1.left!=None:
#         root1=root1.left
#     return root1.key

# def MinInBST(root):
#     if root.left==None:
#         return root.key
#     return (MinInBST(root.left))


# root=Node(20)
# root.left=Node(10)
# root.right=Node(40)
# root.left.left=Node(5)
# root.right.left=Node(30)
# root.right.right=Node(80)
# root.right.right.left=Node(50)
# root.right.right.right=Node(100)
# print(SearchInBST(root,300))
# printBST(InsertInBST(root,25))
# print(FloorInBST(root,80))
# print(MinInBST(root))


# print(3==2)

# def MinHeapify(self,i):
#     arr=self.arr
#     n=len(arr)
#     smallest=i
#     lt=self.lchild(i)
#     rt=self.rchild(i)
#     if lt<n and arr[lt]<arr[smallest]:
#         smallest=lt
#     if rt<n and arr[rt]<arr[smallest]:
#         smallest=rt
#     if smallest !=i:
#         arr[smallest],arr[i]=arr[i],arr[smallest]
#         self.Minheapify(smallest)


# def insert(self,x):
#     arr=self.arr
#     arr.append(x)
#     i=len(arr)-1
#     while i>0 and arr[self.parent(i)]>arr[i]:
#         p=self.parent(i)
#         arr[i],arr[p]=arr[p],arr[i]
#         i=p

# print(bin(12))
# print(type(bin(12)))

# def CountSetBits(n):
#     n1=n
#     res=0
#     while(n1!=0):
#         if n1%2==1:
#             res+=1
#         n1=n1//2
#     return res

# n=int(input("enter a no.: "))
# print("no. of set bits in given no. are:",CountSetBits(n))

# if -1.5:
#     print("hello")


# def OddOccur(l):
#     d={}
#     for i in l:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     l1=[]
#     for j in d:
#         if d[j]%2==1:
#             l1.append(j)
#     return l1

# l=[10,10,10,20,20,20]
# print(OddOccur(l))

# print(30^50)

# def PowerOfTwo(n):
#     n1=n
#     while n1:
#         if n1==2:
#             return "yes"
#         n1/=2
#     return "no"

# print(PowerOfTwo(9))

# import math
# def PowerSet(s):
#     n=len(s)
#     noss=math.pow(2,n)
#     for i in range(n):


# print(type(1<<3))

# def FirstSetBit(n):
#     n1=n
#     pos=0
#     while n1:
#         if n1%2==1:
#             pos+=1
#             return pos
#         n1=n1//2
#         pos+=1
#     return 0

# import math
# def FirstSetBit(n):
#     if n==0:
#         return 0
#     s=(n&(n-1))^n
#     return (int(math.log2(s))+1)

# def FirstSetBit(n):
#     k=1
#     s=1
#     while (s<=n):
#         if s&n!=0:
#             return k
#         s=1<<k
#         k+=1
#     return 0

# import math
# def FirstSetBit(n):
#     if n==0:
#         return 0
#     s= n&(~n+1)
#     return int(math.log2(s))+1


# print(FirstSetBit(-18))
# print(math.log2(0))


# def IsKthBitSet(n,k):
#     b=bin(n)
#     return (b[-k]=='1')

# print(IsKthBitSet(18,6))

# print(-18%2)


# def countSetBits(n):
#     n += 1
#     count = 0
#     x = 2
#     while x//2 < n:
#         quotient = n//x
#         count += quotient * x // 2
#         remainder = n % x
#         if remainder > x//2:
#             count += remainder - x//2
#         x = x*2
#     return count

# print(countSetBits(4))


# import math
# def PowerOfTwo(n):
#     if n<=0 or n==1:
#         return False
#     ans=math.log2(n)
#     return (ans==int(ans))

# print(PowerOfTwo(64))


# n=23
# even = n & 0xAAAAAAAA
# odd = n & 0x55555555
# print(even)
# print(odd)

# print(4&8)
# print(2&8)
# print(16&8)
# print(4&2)
# print(4&16)
# print(2&16)

# def LeftRotate(l,d):
#     l1=l[:d]
#     l2=l[d:]
#     l3=l2+l1
#     return l3


# from collections import deque
# def LeftRotate(l,d):
#     dq=deque(l)
#     dq.rotate(-d)
#     l=list(dq)
#     return l

# print(LeftRotate([1,2,3,4,5],2))
# print(LeftRotate([10,20,30,40],3))


# import math
# def MaxDiff(l):
#     max=-math.inf
#     a=0
#     b=0
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[j]-l[i]>max:
#                 max=l[j]-l[i]
#                 a,b=l[i],l[j]
#     print(a,b)
#     return max


# print(MaxDiff([30,10,8,2]))


# for i in range(0,1):
#     print("hello")


# import math
# def MaxSubArraySum(l):
#     n=len(l)
#     # max_sum_list=[]
#     max_sum_list=[l[0]]
#     for i in range(1,n):
#         max_sum_list.append(max(max_sum_list[i-1]+l[i],l[i]))
#     return max(max_sum_list)


# print(MaxSubArraySum([-5,1,-2,3,-1,2,-2]))
# print(MaxSubArraySum([-1,-math.inf]))
# print(MaxSubArraySum([2,3,-8,7,-1,2,3]))


# def swap(a,b):
#     a,b = b,a

# x=4
# y=5
# swap(x,y)
# x=y
# print(id(x))
# print(id(y))
# def swap(a,b):
#     global x
#     global y
#     x,y=y,x

# swap(x,y)
# print(x)
# print(y)

# def MaxCircularSubArraySum(l):
#     n=len(l)
#     s=l[0]
#     max_sum=l[0]
#     min_sum=l[0]
#     resmax=l[0]
#     resmin=l[0]
#     for i in range(1,n):
#         max_sum=max(max_sum+l[i],l[i])
#         min_sum=min(min_sum+l[i],l[i])
#         resmax=max(max_sum,resmax)
#         resmin=m

# print(MaxCircularSubArraySum([3,-4,5,6,-8,7]))


# def MajorityElements(l):
#     n=len(l)
#     a=n//2
#     d={}
#     for i in range(n):
#         if l[i] not in d:
#             d[l[i]]=1
#         else:
#             d[l[i]]+=1
#     l1=[]
#     for i in  d:
#         if d[i]>a:
#             l1.append(i)
#     if len(l1)==0:
#         print("no majority element exist",-1)
#         return
#     for i in range(n):
#         if l[i] in l1:
#             print(f"majority element {l[i]} is at index ",i)
#     return

# MajorityElements([8,7,3,8,8])


# def MinFlips(l):
#     n = len(l)
#     l1 = []
#     f = l[0]
#     no_of_groups = 1
#     for i in range(n):
#         if (l[i] ^ f != 0):
#             no_of_groups += 1
#             f = l[i]
#         l1.append(l[0])
#     print("list after min no. of flips is: ", l1)
#     return no_of_groups//2

# def MinFlips(l):
#     n = len(l)
#     f = l[0]
#     l1 = []
#     no_of_minflips = 0
#     last_ele = f
#     for i in range(n):
#         if i != 0:
#             last_ele = l[i-1]
#         if (l[i] ^ f != 0):
#             if (l[i] != last_ele):
#                 no_of_minflips += 1
#         l1.append(f)
#     print("list after min no. of flips is: ", l1)
#     return (no_of_minflips)

# def MinFlips(l):
#     n = len(l)
#     for i in range(1, n):
#         if l[i] != l[i-1]:
#             if l[i] != l[0]:
#                 print(f"from {i} to", end=" ")
#             else:
#                 print(i-1)
#     if l[n-1] != l[0]:
#         print(n-1)


# MinFlips([1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1])


# def Max_SubArray_Of_K_eles(l, k):
#     n = len(l)
#     max_sum = -math.inf
#     for i in range(n-k+1):
#         curr_sum = 0
#         k1 = 0
#         while (k1 < k):
#             curr_sum += l[i+k1]
#             k1 += 1
#         max_sum = max(max_sum, curr_sum)
#     return max_sum

# def Max_SubArray_Of_K_eles(l, k):
#     n = len(l)
#     max_sum = -math.inf
#     for i in range(n-k+1):
#         curr_sum = 0
#         k1 = 0
#         while (k1 < k):
#             curr_sum += l[i+k1]
#             k1 += 1
#         max_sum = max(max_sum, curr_sum)
#     return max_sum

# def Max_SubArray_Of_K_eles(l, k):
#     n = len(l)
#     curr_sum = 0
#     for i in range(k):
#         curr_sum += l[i]
#     res = curr_sum
#     prev = 0
#     next = k
#     for j in range(n-k):
#         curr_sum = curr_sum-l[prev]+l[next]
#         res = max(res, curr_sum)
#         prev += 1
#         next += 1
#     return (res)

# print(Max_SubArray_Of_K_eles([1, 8, 30, -5, 20, 7], 3))
# print(Max_SubArray_Of_K_eles([1, 2, 3, 4, 5], 2))
# print(Max_SubArray_Of_K_eles([5, -10, 6, 90, 3], 2))


# def SubArray_with_given_sum(l, s):
#     n = len(l)
#     for i in range(n):
#         l1 = []
#         curr_sum = 0
#         for j in range(i, n):
#             curr_sum += l[j]
#             if curr_sum < s:
#                 l1.append(l[j])
#             elif curr_sum == s:
#                 l1.append(l[j])
#                 print("yes")
#                 return l1
#             else:
#                 break
#     print("no")
#     return


# def SubArray_with_given_sum(l, sum):
#     n = len(l)
#     l1 = []
#     s, curr = 0, 0
#     for i in range(n):
#         curr += l[i]
#         l1.append(l[i])
#         while (curr > sum):
#             curr -= l[s]
#             l1.remove(l[s])
#             s += 1
#         if curr == sum:
#             print("yes")
#             return l1
#     print("no")
#     return l1

# print(SubArray_with_given_sum([2, 4], 4))

# def getSum(l, a, b):
#     if b < a:
#         print("invalid inputs")
#         return
#     s = 0
#     for i in range(a, b+1):
#         s = s+l[i]
#     return s

# def getSum(l, a, b):
#     if b < a:
#         print("invalid inputs")
#         return
#     l1 = []
#     n = len(l)
#     l1.append(l[0])
#     for i in range(1, n):
#         l1.append(l1[i-1]+l[i])
#     if a == 0:
#         return l1[b]
#     else:
#         return l1[b]-l1[a-1]

# def getWSum(l, a, b):
#     if b < a:
#         print("invalid inputs")
#         return
#     l1 = []
#     n = len(l)
#     l1.append(l[0])
#     for i in range(1, n):
#         l1.append(l1[i-1]+l[i])
#     if a == 0:
#         res1 = l1[b]
#     else:
#         res1 = l1[b]-l1[a-1]

#     l2 = []
#     for j in range(n):
#         l2.append(j*l[j])

#     l3 = []
#     l3.append(l2[0])
#     for k in range(1, n):
#         l3.append(l3[k-1]+l2[k])
#     if a == 0:
#         res2 = l3[b]
#     else:
#         res2 = (l3[b]-l3[a-1])

#     return (res2-((a-1)*res1))


# print(getWSum([2, 3, 5, 4, 6, 1], 0, 2))


# def Equib_Point(l):
#     n = len(l)
#     l_sum = [None]*n
#     l_sum[0] = 0
#     for i in range(1, n):
#         l_sum[i] = l_sum[i-1]+l[i-1]

#     r_sum = [None]*n
#     r_sum[n-1] = 0
#     for j in range(n-2, -1, -1):
#         r_sum[j] = r_sum[j+1]+l[j+1]

#     for m in range(n):
#         if l_sum[m] == r_sum[m]:
#             print(f"yes, at index {m}")
#             exit()
#     print("no")
#     return

# def Equib_Point(l):
#     n=len(l)
#     ls=0
#     rs=sum(l)
#     for i in range(n):
#         rs-=l[i]
#         if (ls==rs):
#             return True
#         ls+=l[i]
#     return False


# Equib_Point([4, 2, 2])

# print(sum([1, 2, 3, 4]))

# def three_partition(l):
#     ls = 0
#     n = len(l)
#     rs = sum(l)
#     for i in range(n):
#         mid = l[i]
#         rs -= l[i]
#         rs2 = rs
#         t = 1
#         while ((ls != mid or mid != rs2 or ls != rs2) and i+t != n):
#             mid += l[i+t]
#             rs2 -= l[i+t]
#             print(ls, mid, rs2)
#             t += 1
#         if (ls == mid and mid == rs2):
#             return True
#         ls += l[i]
#     return False


# print(three_partition([3, 2, 5, 1, 1, 5]))


# def max_appearing(l,r):
a = [3]
b = a
b.append(2)
print(a, b)
