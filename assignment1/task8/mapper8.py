#!/usr/bin/python

import sys,math


if __name__ == "__main__":

    
    for line in sys.stdin:
        line=line.rstrip()
        ll=line.split('\t')
        if len(ll) == 2:
            course_list=ll[1].split()
            if len(course_list) > 3:
                name=ll[0].split()[0]
                sum=0
                for c in course_list:
                   raw_mark=c.split()[0].split(',')
                   mark=raw_mark[1][0:-1]
                   sum = sum+int(mark)
                print "{}\t{}".format(name,sum/len(course_list))
 
