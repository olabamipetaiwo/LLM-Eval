
# eval.py

dataset = [
    {
        "input": "What does RAG stand for?",
        "expected": "Retrieval-Augmented Generation",
    },
    {
        "input": "What does LLM stand for?",
        "expected": "Large Language Model",
    },
    {
        "input": "What does NLP stand for?",
        "expected": "Natural Language Processing",
    },
]


def model(question: str) -> str:
    responses = {
        "What does RAG stand for?": "Retrieval-Augmented Generation",
        "What does LLM stand for?": "Large Language Model",
        "What does NLP stand for?": "Natural Language Processing",
    }

    return responses.get(question, "I don't know")


correct = 0

for example in dataset:
    prediction = model(example["input"])
    expected = example["expected"]

    passed = prediction == expected

    correct += int(passed)

    print({
        "input": example["input"],
        "prediction": prediction,
        "passed": passed,
    })


accuracy = correct / len(dataset)

print(f"Accuracy: {accuracy:.2%}")
