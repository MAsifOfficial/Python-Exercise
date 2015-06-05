# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def recursiveInc(c, A):
  if A[c] <  A[c+1]:
	return c
  else:
	return  recursiveInc(c+1, A)

def recursiveDec(c, A):
  l = len(A)
  if(c < (l-1)):
    if A[c] >  A[c+1]:
	    return c
    else:
        return  recursiveDec(c+1, A)
  else:
     return c

def solution(A):
    n = len(A)
    pitlist = []

    #---------------------------------------#
    # Loop through a given list			    #
    # Use recursive functions to figure out	#
    # Q and R values				        #
    #---------------------------------------#
    for p in xrange(0, n-1):
        q = recursiveInc(p, A)
        if(p < q):
            r = recursiveDec(q, A)
            print"p: "+str(p)+" q: "+str(q) + "r: " + str(r) 
            if(q < r):
		        print "("+str(A[p])+","+str(A[q])+","+str(A[r])+")"
		        aa = A[p] - A[q]
		        bb = A[r] - A[q]
		        pitlist.append(min(aa, bb))
        
    if len(pitlist) > 0:
      pitlist.sort()
      return(pitlist.pop())
    else:
      print pitlist
      return -1

def main():
  eList = [0, 1, 3, -2, 0, 1, 0, -3, 2, 3]
  print "max pit value: " + str(solution(eList))

main()

