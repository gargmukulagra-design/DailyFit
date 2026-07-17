# 🏋️ Daily Fit

Daily Fit is a fitness tracking web application built with **Python**, **Streamlit**, **SQLite**, and **Machine Learning**. It helps users monitor their daily calorie intake, calories burned, BMI, weight history, and predicts future weight changes based on their lifestyle.

---

## ✨ Features

### 👤 User Profile
- Store personal information
- Calculate and display BMI
- Automatic BMI category detection
- Edit profile anytime

### 🍽️ Meal Tracking
- Add meals with calorie values
- View daily calorie intake
- Maintain meal history

### 🏃 Activity Tracking
- Log daily physical activities
- Record calories burned
- Track workout history

### ⚖️ Weight Tracking
- Store weekly weight updates
- Visualize weight history
- Monitor fitness progress

### 📊 Dashboard
- Daily calorie intake
- Calories burned
- Net calorie surplus/deficit
- BMI summary
- Activity overview

### 🤖 Machine Learning Prediction
Predict future weight based on:
- Age
- Gender
- Height
- Current Weight
- BMI
- Average Calorie Surplus
- Number of Days

The prediction model is trained using **Random Forest Regression** on a realistic synthetic fitness dataset.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Frontend |
| SQLite | Database |
| Pandas | Data Processing |
| Scikit-Learn | Machine Learning |
| Matplotlib | Data Visualization |

---

# 📂 Project Structure

```
DailyFit/
│
├── app.py
├── database.py
├── Database.db
├── weight_model.pkl
├── dailyfit_realistic_synthetic_dataset_5000_rows.csv
├── assets/
├── pages/
├── requirements.txt
└── README.md
```

---

# 📈 Machine Learning

The application uses a **Random Forest Regressor** to estimate future weight changes.

### Input Features

- Age
- Sex
- Height (cm)
- Weight (kg)
- BMI
- Average Daily Calorie Surplus
- Prediction Days

### Output

Predicted Weight Change

---

# 🗄️ Database

SQLite stores:

- User Profile
- Meals
- Activities
- Weight History
- Daily Summary

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DailyFit.git
```

Move into the project

```bash
cd DailyFit
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📷 Screenshots

> Add screenshots of your dashboard here.

Examples:

- Dashboard
- Meal Tracker
- Activity Tracker
- Weight Prediction
- BMI Dashboard

---

# 🎯 Future Improvements

- Food Image Recognition using AI
- Barcode Scanner
- Personalized Diet Recommendations
- Workout Recommendation System
- User Authentication
- Cloud Database Support
- Mobile Responsive UI
- Smart Notifications
- Fitness Goal Tracking

---

# 📚 Learning Outcomes

This project helped in understanding:

- Streamlit Application Development
- SQLite Database Management
- CRUD Operations
- Machine Learning Integration
- Data Visualization
- Model Deployment
- Python Project Structure

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Mukul Garg**

Electronics & Communication Engineering  
Motilal Nehru National Institute of Technology Allahabad

Interested in:
- Artificial Intelligence
- Machine Learning
- Python
- C++
- RAG Systems
- Full Stack Development

---

⭐ If you found this project useful, consider giving it a star!
