with open("chembl_train.smi") as srcTrain, open(
    "chembl_train_short.smi", "w"
) as targetTrain:
    for i in range(3000):
        targetTrain.write("CCCC\n")
