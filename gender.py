from sklearn import tree

#[height, weight, shoes size]
x = [[181, 80, 44], [177,70,43],[160, 60, 38], [154, 54, 37], [166, 65, 40],[190, 90, 47],[177,70,40], [171, 75, 42], [181,85, 43]]
y = ['male', 'female', 'female', 'female', 'female', 'male', 'female', 'female', 'male']

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(x,y)

predicition = classifier.predict([[177,78,43]])

print(predicition)
