# 🎬 IMDB Movie Review Sentiment Analysis

A simple yet powerful **Sentiment Analysis Web App** built using **TensorFlow / Keras** and deployed with **Streamlit**. This project classifies IMDB movie reviews into **Positive** or **Negative** sentiments using a trained Recurrent Neural Network (RNN).

---

## 📌 Features

* ✅ Uses IMDB dataset word index
* ✅ Pre‑trained RNN model for fast predictions
* ✅ Clean text preprocessing & padding
* ✅ Interactive Streamlit UI
* ✅ Displays prediction confidence score

---

## 🧠 Model Overview

The project loads a pre‑trained model `simple_rnn_imdb.h5` which predicts sentiment probability. Reviews with prediction > 0.5 are classified as **Positive**, otherwise **Negative**.

---

## 🗂️ Project Structure

```
📁 Project
│-- main.py              # Streamlit application
│-- simple_rnn.ipynb     # Model training notebook
│-- prediction.ipynb     # Prediction testing notebook
│-- requirements.txt     # Dependencies
│-- simple_rnn_imdb.h5   # Pre-trained model (required)
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd project-folder
```

### 2️⃣ Install Dependencies

Make sure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Streamlit app with:

```bash
streamlit run main.py
```

Then open the link provided in the terminal.

---

## 🧾 How It Works

1️⃣ Enter a movie review text in the input box

2️⃣ Click **Classify**

3️⃣ The app preprocesses the text:

* Converts words to lowercase
* Maps words to IMDB dictionary indices
* Pads sequence to length 500

4️⃣ Model predicts sentiment

5️⃣ Result & Probability displayed 🎉

---

## 🧪 Example Reviews

```
This movie was really good, I loved the acting.
→ Positive

I didn't like this movie. It was boring and slow.
→ Negative
```

---


## 📦 Requirements

Ensure the following key libraries are installed:

* TensorFlow
* NumPy
* Pandas
* Scikit‑Learn
* Matplotlib
* Streamlit

*(Already included in requirements.txt)*

---

## ❤️ Contributing

Pull requests are welcome! If you’d like to improve the model, UI, or add features, feel free to contribute.

---

## 📜 License

Open‑source — free to use and modify.

---

### 🚀 Enjoy exploring Sentiment Analysis! If you want tweaks like visuals, improved UI, or deployment help, just ask 😊
