#!/usr/bin/python

import sys,math

prev_line_context = ""
entropy_dict={}

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if len(ll) == 2:
       line=ll[0]
       value=int(ll[1])
       l_list=line.split()
       if " ".join(l_list[0:2]) == prev_line_context:
           entropy_dict[l_list[2]]=value
       else:
           #first 2 words in current line does not equal prev_line_context 
           if prev_line_context != "":
               #print prev_line_context
               #--step1, calculate the previous entropy
               v_sum=sum(entropy_dict.itervalues())
               v_list=[]
               entropy=0.0000
               for v in entropy_dict.itervalues():
                    v_list.append(float(v)/v_sum)
               for i in v_list:
                    entropy = entropy + (-i*math.log(i,2))
               print("{0}\t{1}".format(prev_line_context, entropy)) 
           
  
           #--step2, configure new context
           prev_line_context = " ".join(l_list[0:2])
           entropy_dict={}
           entropy_dict[prev_line_context] = value
          

if prev_line_context != "" and entropy_dict:
     v_sum=sum(entropy_dict.itervalues())
     v_list=[]
     entropy=0.0000
     for v in entropy_dict.itervalues():
         v_list.append(float(v)/v_sum)
     for i in v_list:
         entropy = entropy + (-i*math.log(i,2))
     print("{0}\t{1}".format(prev_line_context, entropy)) 
 
