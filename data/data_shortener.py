with open("chembl_train.smi") as srcTrain, open(
    "chembl_train_short.smi", "w"
) as targetTrain:
    targetTrain.writelines(srcTrain.readlines()[:200000])
