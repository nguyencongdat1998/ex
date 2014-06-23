from math import fabs

def run3(t,a): #chon ra 3 so co tong gan bang t nhat
	#Giai: thu chon voi tat ca cac tong cua cac bo ba so thuoc a:
	i = 0 
	j = 1  #i,j,h la cac vi tri
	h = 2
	sums = a[i] + a[j] + a[h] # chon sums = a[1] + a[2] + a[3] lam moc
	for  x in range (len(a) - 2):
		for  y in range (x+1,len(a) - 1):
			for  z in range (y+1,len(a)):
				if ( fabs(a[i] + a[j] + a[h] - t) < fabs(t - sums) ) : # neu tong moi gan t hon
					i = x
					j = y
					h = z
					sums = a[i] + a[j] + a[h]

	print (a[i] ," + ",a[j]," + ",a[h]," = ",sums,' = ',t," + ",sums - t)	



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

	run3(t,a)
