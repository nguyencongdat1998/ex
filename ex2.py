def run1(t,a): #chon ra 2 so trong a co tong bang n
	i = -1 # i, j la bien chi vi tri cua 2 so
	j = -1
	for x in range (len(a)-1):
		for y in range (x+1,len(a)):
			if a[x]+a[y] == t :
				i = x
				j = y
	return (i,j)

def run2(t,a): #chon ra 3 so trong a co tong bang n
	i = -1 # i, j ,h la bien chi vi tri cua 3 so
	j = -1
	h = -1
	for x in range (len(a)-2):
		for y in range (x+1,len(a)-1):
			for z in range (y+1,len(a)):
				if a[x]+a[y]+a[z] == t :
					i = x
					j = y
					h = z
	return (i,j,h)
	
def run3(t,a): #chon ra 3 so co tong gan bang t nhat
	#Giai: thu chay lan luot voi t, t-1 , t+1, .... , t-w, t+w
	done = False
	w = -1 
	i = -1 #i,j,h la vi tri
	while (done == False):
		w = w + 1
		i,j,h = run2(t-w,a)
		if i != -1:
			break
		i,j,h = run2(t+w,a)
		if i != -1:
			break
	return(i,j,h)	



def inputArray(): # nhap vao mang
    # nhap lan luot: nhap mot phan tu roi Enter
    # nhap "." -> Enter de danh dau het manng
	print (" Input array :")
	a = [0] * -1
	i = -1
	s = 1 
	t = "   "
	while (t !=  "."):
		t = input ()
		if t != ".":
			s = int (t)
			i = i + 1
			a = a + [0]
			a[i] = s
	return a

if __name__ == '__main__':
	t = int(input("Tong = "))   #nhap vao tong
	a = inputArray()			#nhap vao day
	print ("Array = " ,a)		#in ra day vua nhap

	# Bai 1: 
	m,n = run1(t,a)
	if m != -1: #neu tim duoc so thoa man
		print (a[m] ," + ", a[n] ," = ",t)
	else:		#neu khong tim duoc so thoa man
		print ("Bai toan 1 khong co dap an thoa man.")

	# Bai 2:
	m,n,p = run2(t,a)
	if m != -1:
		print (a[m] ," + ", a[n] ," + ", a[p] ," = ",t)
	else:
		print ("Bai toan 2 khong co dap an thoa man.")

	# Bai 3:
	m,n,p = run3(t,a)
	print (a[m] ," + ", a[n] ," + ", a[p] ," = ",a[m]+a[n]+a[p]," = ",t," + ",a[m]+a[n]+a[p]-t)

