import streamlit as st
import numpy as np

def mttf(lambd):
    return 1 / lambd

def mttr(mu):
    return 1 / mu

def utilization(lambd, mu):
    return lambd / mu

def traffic_intensity(lambd, mu):
    return lambd / (lambd + mu)

def avg_queue_length(lambd, mu):
    rho = traffic_intensity(lambd, mu)
    return rho / (1 - rho)

def avg_waiting_time(lambd, mu):
    return avg_queue_length(lambd, mu) / lambd

def server_busy_time(mu, num_customers):
    return 1 / mu * num_customers

def system_waiting_time(lambd, mu):
    rho = traffic_intensity(lambd, mu)
    return avg_waiting_time(lambd, mu) + (1 / mu)

def probability_queue_more_than_k(lambd, mu, k):
    rho = traffic_intensity(lambd, mu)
    return (rho ** (k + 1)) / (1 - rho)

def probability_server_idle(lambd, mu):
    rho = traffic_intensity(lambd, mu)
    return 1 - rho

# Main Streamlit code
st.title("Teori Antrian")

# Input parameters
lambd = st.number_input("kedatangan pelanggan (λ)", value=2.0, min_value=0.0)
mu = st.number_input("Lama waktu pelayanan (μ)", value=3.0, min_value=0.0)
num_customers = st.number_input("Jumlah pelanggan", value=5, min_value=0, step=1)

# Calculate metrics
avg_queue_len = round(avg_queue_length(lambd, mu),3)
avg_waiting = round(avg_waiting_time(lambd, mu),3)
server_busy = round(server_busy_time(mu, num_customers),3)
system_waiting = round(system_waiting_time(lambd, mu),3)
prob_server_idle = round(probability_server_idle(lambd, mu))
prob_queue_more_k2 = round(probability_queue_more_than_k(lambd, mu, 2),3)
prob_queue_more_k4 = round(probability_queue_more_than_k(lambd, mu, 4),3)
prob_queue_more_k5 = round(probability_queue_more_than_k(lambd, mu, 5),3)
prob_queue_more_k6 = round(probability_queue_more_than_k(lambd, mu, 6),3)

# Display results
st.header("Hasil")
st.write("Rata-rata Panjang Antrian:", avg_queue_len)
st.write("Rata-rata Waktu Tunggu:", avg_waiting)
st.write("Waktu Pelayan Sibuk:", server_busy)
st.write("Waktu Tunggu Sistem:", system_waiting)
st.subheader("Probabilitas")
st.write("Waktu Pelayan Menganggur:", prob_server_idle)
st.write("Pelanggan Mengantri Lebih dari 2:", prob_queue_more_k2)
st.write("Pelanggan Mengantri Lebih dari 4:", prob_queue_more_k4)
st.write("Pelanggan Mengantri Lebih dari 5:", prob_queue_more_k5)
st.write("Pelanggan Mengantri Lebih dari 6:", prob_queue_more_k6)
