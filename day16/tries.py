#TRIES DATA STRUCTURE
class node:
  def __init__(self):
    self.d={}
    self.flag=0
class tries:
  def __init__(self):
    self.root=node()
  def insert(self,str):
    t=self.root
    for i in str:
      if i not in t.d:
        t.d[i]=node()
      t = t.d[i] 
    t.flag=1 
    return self.root
  def search(self,str):
    t=self.root
    for i in str:
      if i not in t.d:
        return False
      t=t.d[i]
    if t.flag==1:
      return True
    else:
      return False
  def prefix(self,str):
    t=self.root
    for i in str:
      if i not in t.d:
        return False
      t=t.d[i]
    return True
  def all_prefix(self,str):
    def auto(t,s):
      if t.flag==1:
        print(s)
      for i in t.d:
        auto(t.d[i],s+i)
    t=self.root
    s=''
    for i in str:
      if i in t.d:
        s=s+i
        t=t.d[i]
      else:
        return
    auto(t,s)
  def longest_prefix(self, str):
    t = self.root
    s = ''
    longest = ''
    for i in str:
        if i in t.d:
            s = s + i
            t = t.d[i]
            longest = s  
        else:
            return longest
    return longest
n=int(input())
t1=tries()
for i in range(n):
  a,s=input().split()
  if a=='1':
    t1.insert(s)
  elif a=='2':
    print(t1.search(s))
  elif a=='3':
    print(t1.prefix(s))
  elif a=='4':
    t1.all_prefix(s)
  elif a=='5':
    t1.longest_prefix(s)
