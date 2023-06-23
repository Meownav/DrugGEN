src = open("./chembl_train.smi", "r")
p = src.readlines()[:1200]
target = open("./chembl_train_short.smi", "w")
target.writelines(p)

src.close()
target.close()

s = open("./chembl_test.smi", "r")
p = s.readlines()[:1200]
target = open("./chembl_test_short.smi", "w")
target.writelines(p)

s.close()
target.close()
