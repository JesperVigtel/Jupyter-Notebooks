from pylab import *



fil =  open("./assets/poeng.txt","w")

fil.write("10")
fil.close()

fil =  open("./assets/poeng.txt","r")
print(fil.read())



"""
high_score_fil = loadtxt("./assets/poeng.txt")
high_score = int(high_score_fil)

poeng = 7
print(high_score)

#savetxt("./assets/poeng.txt",0,7)

print(loadtxt("./assets/poeng.txt"))

#loadtxt("./assets/poeng.txt", in)
"""