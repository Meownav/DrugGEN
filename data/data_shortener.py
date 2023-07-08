with open("chembl_train.smi") as srcTrain, open(
    "chembl_train_short.smi", "w"
) as targetTrain:
    targetTrain.writelines(srcTrain.readlines()[:1500])

with open("chembl_test.smi") as srcTest, open(
    "chembl_test_short.smi", "w"
) as targetTest:
    targetTest.writelines(srcTest.readlines()[:1500])
