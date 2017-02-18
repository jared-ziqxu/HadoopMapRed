#!/usr/bin/python

import sys

name=""
course={}

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if ll[0] == "student":
       if len(course) > 0:
           #a new student record section, print out the last section
           mark_list=""
           for k,v in course.iteritems():
              mark_list=mark_list+' ('+k+','+v+')'
           print '{} ------->\t{}'.format(name,mark_list)
           name = ll[2]
           course = {} 
       else :
           name = ll[2]
    else:
       #ll[0] == "mark"
       course[ll[2]]=ll[3]

#last line process
if name and len(course)>0:
       mark_list=""
       for k,v in course.iteritems():
          mark_list=mark_list+' ('+k+','+v+')'
       print '{} ------->\t{}'.format(name,mark_list)
   
