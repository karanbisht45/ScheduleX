# ⚡ ScheduleX — CPU Scheduling Visualizer  

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)  
![Made with C++](https://img.shields.io/badge/Made%20with-C++-orange?logo=c%2B%2B)  
![Streamlit](https://img.shields.io/badge/Powered%20By-Streamlit-ff4b4b?logo=streamlit)  

---

## 📌 Overview  

**ScheduleX** is an **interactive CPU Scheduling Visualizer** built with **Python (Streamlit UI)** and a **C++ backend**.  
It helps students and professionals **simulate scheduling algorithms**, view **Gantt charts**, and analyze **performance metrics** like **waiting time** and **turnaround time**.  

This project bridges **theory and practical implementation** by combining C++’s efficiency with Streamlit’s visualization power.  

---

## ✨ Features  

- 🎛 **Interactive UI** using Streamlit  
- 🖥️ Backend **C++ simulator** for scheduling logic  
- 📊 **Visualize Gantt Charts** dynamically  
- 📈 **Performance Metrics** (Avg. Waiting & Turnaround Time)  
- ⚙️ Supports multiple algorithms:  
  - **FCFS** (First Come First Serve)  
  - **SJF** (Shortest Job First - Preemptive/Non-Preemptive)  
  - **Priority Scheduling**  
  - **Round Robin**  

---

## 🏗️ Tech Stack  

- **Frontend/UI** → [Streamlit](https://streamlit.io/)  
- **Backend Logic** → C++ (compiled to `scheduler.exe`)  
- **Visualization** → Matplotlib, Pandas  
- **Language** → Python 3.10+  

---

## 📂 Project Structure  

ScheduleX/
│── gantt_chart.py # Streamlit frontend for UI & visualization
│── scheduler.cpp # C++ backend for CPU scheduling
│── scheduler.exe # Compiled C++ executable (Windows)
│── requirements.txt # Python dependencies
│── README.md # Documentation

---


---

## 🚀 Installation & Setup  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/your-username/ScheduleX.git
cd ScheduleX
```

### 2️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Compile C++ Backend
For Windows :
```bash
g++ scheduler.cpp -o scheduler.exe
```

For Linux / MacOS:
```bash
g++ scheduler.cpp -o scheduler
```

### 4️⃣ Run the Application
```bash
streamlit run gantt_chart.py
```
