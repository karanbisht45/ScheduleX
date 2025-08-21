import streamlit as st
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def generate_cpp_input(n, processes, algo_choice, quantum):
    """Generate formatted input for the C++ scheduling program."""
    cpp_input = f"{n}\n"
    for p in processes:
        cpp_input += f"{p[0]} {p[1]} {p[2]}\n"
    cpp_input += f"{algo_choice}\n"
    if algo_choice == 3:  # Round Robin needs quantum
        cpp_input += f"{quantum}\n"
    return cpp_input

def get_process_data(n, processes, algo_choice, quantum):
    """Run the C++ scheduler, parse its output, and return process data."""
    cpp_input = generate_cpp_input(n, processes, algo_choice, quantum)

    # Execute C++ program
    result = subprocess.run(["./a.out"], input=cpp_input, text=True, capture_output=True)

    # Debugging: Show raw output from C++
    st.text("Raw C++ Output:\n" + result.stdout)

    lines = result.stdout.strip().split("\n")
    data = []

    for line in lines:
        parts = line.split()
        if len(parts) == 3 and parts[0].isdigit():
            try:
                data.append({
                    "Process": f"P{parts[0]}",
                    "Start": int(parts[1]),
                    "End": int(parts[2])
                })
            except ValueError:
                continue
    
    return pd.DataFrame(data)

def calculate_times(df, processes):
    """Compute Waiting Time (WT) and Turnaround Time (TAT) based on the Gantt chart."""
    completion_times = {row["Process"]: row["End"] for _, row in df.iterrows()}
    
    process_times = []
    total_wt = 0
    total_tat = 0
    
    for i, p in enumerate(processes):
        process_id = f"P{i+1}"
        if process_id in completion_times:
            completion_time = completion_times[process_id]
            turnaround_time = completion_time - p[0]  # TAT = Completion - Arrival
            waiting_time = turnaround_time - p[1]  # WT = TAT - Burst
            
            total_tat += turnaround_time
            total_wt += waiting_time

            process_times.append({
                "Process": process_id,
                "Arrival Time": p[0],
                "Burst Time": p[1],
                "Completion Time": completion_time,
                "Turnaround Time": turnaround_time,
                "Waiting Time": waiting_time
            })
    
    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)
    
    return pd.DataFrame(process_times), avg_wt, avg_tat

def plot_gantt_chart(df):
    """Visualize the Gantt chart based on process execution times."""
    fig, ax = plt.subplots(figsize=(10, 5))

    for i, row in df.iterrows():
        ax.barh(row["Process"], row["End"] - row["Start"], left=row["Start"], color="skyblue")

    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title("Process Scheduling Gantt Chart")
    st.pyplot(fig)

# Streamlit UI
st.title("ScheduleX : The CPU Scheduler")

# Number of processes input
n = st.number_input("Enter number of processes:", min_value=1, step=1)

# Process details input
processes = []
for i in range(n):
    arrival = st.number_input(f"Arrival Time for Process {i+1}:", min_value=0, step=1)
    burst = st.number_input(f"Burst Time for Process {i+1}:", min_value=1, step=1)
    priority = st.number_input(f"Priority for Process {i+1} (Lower = Higher Priority):", min_value=1, step=1)
    processes.append((arrival, burst, priority))

# Algorithm selection
algo_map = {"FCFS": 1, "SJF": 2, "Round Robin": 3, "Priority": 4}
algo_choice = st.selectbox("Select Scheduling Algorithm", list(algo_map.keys()))

# Time quantum input for Round Robin
quantum = st.number_input("Enter Time Quantum:", min_value=1, step=1) if algo_choice == "Round Robin" else 1

if st.button("Generate Gantt Chart"):
    df = get_process_data(n, processes, algo_map[algo_choice], quantum)
    
    if not df.empty:
        plot_gantt_chart(df)
        
        # Calculate and display times
        process_df, avg_wt, avg_tat = calculate_times(df, processes)
        
        st.subheader("Process Details with Turnaround and Waiting Times")
        st.dataframe(process_df)

        st.success(f"**Average Waiting Time (AWT):** {avg_wt:.2f} units")
        st.success(f"**Average Turnaround Time (ATAT):** {avg_tat:.2f} units")
