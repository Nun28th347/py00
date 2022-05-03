#def myfunc():
#  global x                   #การกำหนดว่าXตัวนี้เท่ากับค่าที่กำหนด  xเท่ากับ
#x = "fantastic"

#myfunc()

#print("Python is " + x)





x = "awesome"

def myfunc():
  global x                 #globalเป็นการดึงค่าxตัวข้าง โดนประกาศในนี้
  x = "fantastic" + x

myfunc()

print("Python is " + x)




