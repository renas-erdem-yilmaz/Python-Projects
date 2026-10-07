import os
import torch
import matplotlib.pyplot as plt

from torch import nn
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader


train_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)


train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)


class DigitClassifier(nn.Module):

    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()

        self.network = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        x = self.network(x)
        return x


model = DigitClassifier()

model_path = "digit_classifier.pth"


if os.path.exists(model_path):

    model.load_state_dict(
        torch.load(model_path)
    )

    print("Saved model loaded!")

else:

    loss_fn = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )

    epochs = 5

    for epoch in range(epochs):

        model.train()

        total_loss = 0

        for images, labels in train_loader:

            optimizer.zero_grad()

            outputs = model(images)

            loss = loss_fn(outputs, labels)

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

        average_loss = total_loss / len(train_loader)

        print(
            f"Epoch {epoch + 1}/{epochs}, "
            f"Loss: {average_loss:.4f}"
        )

    torch.save(
        model.state_dict(),
        model_path
    )

    print("Training complete!")
    print("Model saved!")


model.eval()

correct = 0
total = 0


with torch.no_grad():

    for images, labels in test_loader:

        outputs = model(images)

        predictions = outputs.argmax(dim=1)

        correct += (
            predictions == labels
        ).sum().item()

        total += labels.size(0)


accuracy = correct / total * 100

print(
    f"Test Accuracy: {accuracy:.2f}%"
)


images, labels = next(iter(test_loader))


with torch.no_grad():

    outputs = model(images)

    predictions = outputs.argmax(dim=1)


for i in range(6):

    plt.imshow(
        images[i].squeeze(),
        cmap="gray"
    )

    plt.title(
        f"Predicted: {predictions[i].item()} | "
        f"Actual: {labels[i].item()}"
    )

    plt.show()