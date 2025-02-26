# AI_StockInsights_Agent

## Overview

This project is a **multi-agent AI system** that fetches stock data using the **yfinance API**, processes it, and generates insights using **Google Gemini AI**. It provides both a **command-line agent** and a **Flask API** to interact with the stock data.

---

## Features

- Uses **Google Gemini** as the AI model.
- Fetches **real-time stock data** using `yfinance`.
- Generates **stock trend insights**.
- Provides a **Flask API** for fetching stock data.
- Saves stock trend graphs as images (`stock_trend.png`).

---

## Installation

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/J2A9-11/AI_StockInsights_Agent.git
```

### **Step 2: Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Set Up Gemini API Key**

Get your API key from [Google AI Studio](https://aistudio.google.com/).

**Replace** `your-api-key` with your actual API key in agent.py file.
```bash
genai.configure(api_key="your-api-key")
```

---

## Running the Project

### **1. Start the Flask API**

```bash
python app.py
```

- API is available at: `http://127.0.0.1:5000/get_stock?ticker=AAPL`

### **2. Run the AI Agent**

```bash
python agent.py
```

- Enter a stock ticker (e.g., `AAPL`, `GOOGL`,`TSLA`).
- The AI will **fetch stock data** and **generate insights**.
- A graph will be saved as **`stock_trend.png`**.

---

## API Usage

### **1. Fetch Stock Data (GET Request)**

```
GET http://127.0.0.1:5000/get_stock?ticker=AAPL
```

#### **Response Example:**

```json
{
    "message": "Stock data fetched for AAPL. See 'stock_trend.png'."
}
```

---

## Dependencies

- `google-generativeai`
- `yfinance`
- `flask`
- `matplotlib`

To install manually:

```bash
pip install google-generativeai yfinance flask matplotlib
```

---

## Notes

- Ensure you have **Python 3.8+** installed.
- If you face an error with Gemini, ensure your API key is correct.

---


### **Author**

Jai Anand

