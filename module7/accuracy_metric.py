from sklearn.metrics import accuracy_score


def simple_binary():
    # Simple binary classification example
    prediction = [1, 1, 1]
    actual_results = [1, 0, 1]

    correct = 0
    for index in range(len(prediction)):
        if prediction[index] == actual_results[index]:
            correct += 1
    print(f'For loop accuracy = {(correct/len(prediction))*100:.2f}')
    print(f'For Sklearn accuracy = {
          (accuracy_score(actual_results, prediction)):.2f}')


def main():
    simple_binary()


if __name__ == '__main__':
    main()
