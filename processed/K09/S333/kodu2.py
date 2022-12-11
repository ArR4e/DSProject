def minu_shuffle(järjend):
    from random import randint, sample
    #segame arve nii,et iga arv liigub korra (vähemalt on see teor. võimalik)
    for i in range(len(järjend)):
        #valime juhuslikult 2 arvu indexit
        juh_index0= randint(0,len(järjend)-1)
        juh_index1= randint(0,len(järjend)-1)
        #vahetame nende kahe kohad ära
        järjend[juh_index0], järjend[juh_index1]= järjend[juh_index1], järjend[juh_index0]
  