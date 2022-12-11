# import string
f=open("taksohinnad.txt",encoding="UTF-8")
tee_pikkus_koju = float(input("Sisesta tee pikkus kilomeetrites: "))
# takso_firma=""
# komad=""
# while True:
#     rida=f.readline()
#     if rida=="":
#         break
#     for el in rida:
#         if el.isalpha():
#             takso_firma=takso_firma+el
#         elif el in string.punctuation:
#             komad=komad+el     
#for rida in f:
rida=f.readline()
a=rida.strip("\n").split(",")
if rida=="":
    taksosse_sisisenemise_hind=0
    kilomeetri_hind=0
else:    
    taksosse_sisisenemise_hind=float(a[1])
    kilomeetri_hind=float(a[2])
taksosõit_koju= taksosse_sisisenemise_hind+(tee_pikkus_koju*kilomeetri_hind)
miinimum=taksosõit_koju
f.close()
f=open("taksohinnad.txt",encoding="UTF-8")
# while True:
#     rida=f.readline()
#     if rida=="":
#         break
if rida=="":
    print("Kahjuks taksod puuduvad.")
else:
    for rida in f:
    
        a=rida.strip("\n").split(",")
        takso_firma=a[0]
        taksosse_sisisenemise_hind=float(a[1])
        kilomeetri_hind=float(a[2])
        taksosõit_koju= taksosse_sisisenemise_hind+(tee_pikkus_koju*kilomeetri_hind)
        
        if taksosõit_koju<=miinimum:
            miinimum=taksosõit_koju
            vastav_firma=takso_firma
    print("Kõige odavam on "+vastav_firma+".")#Alati vaata üle, kas otsitavat järjendit ei ole juba väljaspool tsükklit juba mainitud.
#Muidu tsükkel väljastab nii ühe kui ka teise. Imelik küll, aga järjenditega nii ongi.
f.close()# print(miinimum)