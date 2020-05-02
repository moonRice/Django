import numpy as np


class KNN:
    def __init__(self, k):
        self.K = k

    def createData(self):
        features = np.array(
            [
                [17, 6],
                [7, 2],
                [1, 5],
                [16, 7],
                [5, 10],
                [2, 8]
            ]
        )
        labels = ["男", "男", "女", "男", "女", "女"]
        return features, labels

    def Normalization(self, data):
        maxs = np.max(data, axis=0)
        mins = np.min(data, axis=0)
        new_data = (data - mins) / (maxs - mins)
        return new_data, maxs, mins

    def classify(self, one, data, labels):
        differenceData = data - one
        squareData = (differenceData ** 2).sum(axis=1)
        distance = squareData ** 0.5
        sortDistanceIndex = distance.argsort()
        labelCount = dict()
        for i in range(self.K):
            label = labels[sortDistanceIndex[i]]
            labelCount.setdefault(label, 0)
            labelCount[label] += 1
        sortLabelCount = sorted(labelCount.items(), key=lambda x: x[1], reverse=True)
        print(sortLabelCount)
        return sortLabelCount[0][0]


if __name__ == "__main__":
    knn = KNN(3)
    features, labels = knn.createData()
    new_data, maxs, mins = knn.Normalization(features)
    one = np.array([5, 10])
    new_one = (one - mins) / (maxs - mins)
    result = knn.classify(new_one, new_data, labels)
    print("两项评分为 {} 的预测性别为 : {}".format(one, result))