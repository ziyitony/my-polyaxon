sum = 0
startNum = 1
endNum = 1000
for i in range(startNum, endNum):
  sum = sum + i
print sum

fo = open("foo.txt", "w")
fo.write(str(sum))
fo.close