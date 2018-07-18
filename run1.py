sum = 0
startNum = 1
endNum = 1000
for i in range(startNum, endNum):
  sum = sum + i
print sum

# I can only get log output of sum ,
# but can't find foo.txt file in persistence volume
# claimed in polyaxon-config.yaml file
fo = open("foo.txt", "w")
fo.write(str(sum))
fo.close