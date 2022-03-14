import numpy as np

filename="data 1.npy"
nodes = np.load(filename)
#+D,-G | +A +C
#[3]=T,[6]=F| [0]=T [2]=T
totalNum=len(nodes[0])

p={}
p.update({"a":sum(nodes[0])/totalNum})
p.update({"na":1-p["a"]})
p.update({"b":sum(nodes[1])/totalNum})
p.update({"nb":1-p["b"]})
p.update({"c":sum(nodes[2])/totalNum})
p.update({"nc":1-p["c"]})
p.update({"d":sum(nodes[3])/totalNum})
p.update({"nd":1-p["d"]})
ac,nac,ab,anb,abd,nab,nanb,ec,enc,fc,fnc,gd,gnd,nabd,anbd,nanbd=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
for i in zip(*nodes):#i=(nodes[0][x],nodes[1][x]...nodes[7][x])
   if(i[0]):#+a
       if(i[1]):#+a,+b
           ab+=1
           if(i[3]):#+a,+b,+d
               abd+=1
       if(not(i[1])):#+a,-b
           anb+=1
           if(i[3]):#+a,-b,+d
               anbd+=1
       if(i[2]):#+a,+c
           ac+=1
   if(not(i[0])):#-a
       if(not(i[1])):#-a,-b
           nanb+=1
           if(i[3]):#-a,-b,+d
               nanbd+=1
       if(i[1]):#-a,+b
           nab+=1
           if(i[3]):#-a,+b+d
               nabd+=1
       if(i[2]):#-a,+c
           nac+=1
   if(i[5]):#+f
       if(i[2]):#+f,+c
           fc+=1
       if(not(i[2])):#+f,-c
           fnc+=1
   if(i[6]):#+g
       if(i[3]):#+g,+d
           gd+=1
       if(not(i[3])):#+g,-d
           gnd+=1
   if(i[4]):#+e
       if(i[2]):#+e,+c
           ec+=1
       if(not(i[2])):#+e,-c
           enc+=1
ac,nac,ab,anb,abd,nab,nanb,ec,enc,fc,fnc,gd,gnd,nabd,anbd,nanbd=ac/totalNum,nac/totalNum,ab/totalNum,anb/totalNum,abd/totalNum,nab/totalNum,nanb/totalNum,ec/totalNum,enc/totalNum,fc/totalNum,fnc/totalNum,gd/totalNum,gnd/totalNum,nabd/totalNum,anbd/totalNum,nanbd/totalNum
p.update({"c_a":ac/p["a"]})
p.update({"c_na":nac/p["na"]})
p.update({"d_ab":abd/ab})
p.update({"d_nab":nabd/nab})
p.update({"d_anb":anbd/anb})
p.update({"d_nanb":nanbd/nanb})
p.update({"e_c":ec/p["c"]})
p.update({"e_nc":enc/p["nc"]})
p.update({"f_c":fc/p["c"]})
p.update({"f_nc":fnc/p["nc"]})
p.update({"g_d":gd/p["d"]})
p.update({"g_nd":gd/p["nd"]})


m= p["a"]*p["b"]*p["c_a"]*p["d_ab"]*p["e_c"]*p["f_c"]*(1-p["g_d"])
m1=p["a"]*p["b"]*p["c_a"]*p["d_ab"]*p["e_c"]*(1-p["f_c"])*(1-p["g_d"])
m2=p["a"]*p["b"]*p["c_a"]*p["d_ab"]*(1-p["e_c"])*p["f_c"]*(1-p["g_d"])
m3=p["a"]*p["b"]*p["c_a"]*p["d_ab"]*(1-p["e_c"])*(1-p["f_c"])*(1-p["g_d"])
m4=p["a"]*(1-p["b"])*p["c_a"]*p["d_ab"]*p["e_c"]*p["f_c"]*(1-p["g_d"])
m5=p["a"]*(1-p["b"])*p["c_a"]*p["d_ab"]*p["e_c"]*(1-p["f_c"])*(1-p["g_d"])
m6=p["a"]*(1-p["b"])*p["c_a"]*p["d_ab"]*(1-p["e_c"])*p["f_c"]*(1-p["g_d"])
m7=p["a"]*(1-p["b"])*p["c_a"]*p["d_ab"]*(1-p["e_c"])*(1-p["f_c"])*(1-p["g_d"])
print(m+m1+m2+m3+m4+m5+m6+m7)
