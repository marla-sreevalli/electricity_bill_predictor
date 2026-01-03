import matplotlib.pyplot as plt

def generate_chart(predicted_bill):
    average_bill = 1800  # average Indian household bill

    labels = ["Average Bill", "Your Predicted Bill"]
    values = [average_bill, predicted_bill]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Electricity Bill Comparison")
    plt.ylabel("Amount (₹)")

    plt.savefig("static/chart.png")
    plt.close()