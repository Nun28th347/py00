class myclass():
  def __len__(self):                #_len_ ส่งคืนค่าFalse or 0
    return 0

myobj = myclass()
print(bool(myobj))  