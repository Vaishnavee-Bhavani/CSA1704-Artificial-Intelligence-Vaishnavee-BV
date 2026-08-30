# Simple rule-based Decision Tree implementation
def decision_tree_classifier(outlook, humidity):
    if outlook == 'Overcast':
        return 'Play'
    elif outlook == 'Sunny':
        if humidity == 'High':
            return 'Do Not Play'
        else:
            return 'Play'
    elif outlook == 'Rain':
        return 'Play'

print("Decision for Sunny & High Humidity:", decision_tree_classifier('Sunny', 'High'))
print("Decision for Overcast:", decision_tree_classifier('Overcast', 'High'))
