with open("chembl_train.smi") as srcTrain:
    with open("chembl_test.smi") as srcTest:
        with open("chembl_train_short.smi", "w") as targetTrain:
            with open("chembl_train_short.smi", "w") as targetTest:
                targetTrain.writelines(srcTrain.readlines[:200000])
                targetTest.writelines(srcTest.readlines[:200000])

