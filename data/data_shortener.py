with open("chembl_train.smi") as srcTrain, open(
    "chembl_train_short.smi", "w"
) as targetTrain:
    for i in range(1500):
        targetTrain.write("CC(=O)Nc1ccc(O)cc1\n")
