# Assignment #8: Programming Practice

## 723A. The New Year: Meeting Friends

implementation, math, sorting, 800, https://codeforces.com/problemset/problem/723/A

### Methods

最小距离一定是最边上的两个人向中间走，即列表的最大值减最小值

### Codes

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:09:26 2020

@author: zuoxichen
"""
l1=list(int(i) for i in input().split())  # get a list that contains coordinates of the houses
print(max(l1)-min(l1))    # the minimum distance
```

## 705A. Hulk

implementation, 800, https://codeforces.com/problemset/problem/705/A

### Methods

模拟即可，当n为偶时输出‘I hate’，当n为奇时输出‘I love’

### Codes

```python
"""
Created on Tue Nov 17 13:12:45 2020
 
@author: zuoxichen
"""
 
n=int(input()) # get number
i=0 # create a timer
list1=[] # create an empty list
while i<n:
    list1.append('I hate' if i%2==0 else 'I love')
    list1.append('that' if i<n-1 else 'it')
    i+=1
for i in list1:
   	print(i,end=' ')             # print as a string
```

## 200B. Drinks

implementation, math, 800, https://codeforces.com/problemset/problem/200/B

### Methods

水题，把给出的列表求和除以n即可

### Codes

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:07:13 2020

@author: zuoxichen
"""

n=int(input())
print(sum(list(int(i) for i in input().split(' ')))/n)      # print final results
```

## 492B. Vanya and Lanterns

binary search/implementation/math/sortings, 1200, https://codeforces.com/problemset/problem/492/B

### Codes

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:22:17 2020

@author: zuoxichen
"""
l1=list(int(i) for i in input().split())
l2=sorted(list(int(i) for i in input().split()))
l3=list()
i=0
l4=[l2[0]]
if l1[0]>=2:
    while i<=l1[0]-2:
        l3.append(l2[i+1]-l2[i])
        i+=1
else:
    l3.append(l2[0])
l4.append(l1[1]-l2[l1[0]-1])
print(round(max(l3)/2 if max(l3)/2>max(l4) else max(l4),10))
```

