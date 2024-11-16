from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from icmplib import ping as icmp_ping

def ping():
    host_ip = host.get()
    host_ping = int(number_ping.get())
    host_count = int(packets.get())
    host_interval = int(interval.get())
    host_timeout = int(timeout.get())

    p = icmp_ping(host_ip, count=host_count, interval=host_interval/1000, timeout=host_timeout)
    host_address = p.address
    packets_received = p.packets_received
    packets_sent = p.packets_sent
    packet_loss = (packets_sent - packets_received) / packets_sent * 100
    min_rtt = p.min_rtt
    max_rtt = p.max_rtt
    avg_rtt = p.avg_rtt

    respf = f"IP da URL: {host_address}\n"
    respf += f"Número de pacotes enviados: {packets_sent}\n"
    respf += f"Número de pacotes recebidos: {packets_received}\n"
    respf += f"Porcentagem de pacotes perdidos: {packet_loss:.2f}%\n"
    respf += f"Tempo mínimo de round-trip: {min_rtt:.2f} ms\n"
    respf += f"Tempo máximo de round-trip: {max_rtt:.2f} ms\n"
    respf += f"Tempo médio de round-trip: {avg_rtt:.2f} ms"

    resp.config(text=respf)

root = Tk()
root.title("Ping com Interface gráfica")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

host = StringVar()
packets = StringVar()
interval = StringVar()
timeout = StringVar()

ttk.Label(mainframe, text="Insira o IP ou Host").grid(column=1, row=1, sticky=W)
host_entry = ttk.Entry(mainframe, width=20, textvariable=host)
host_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Número de Envios").grid(column=1, row=2, sticky=W)
number_ping = ttk.Combobox(mainframe, width=20, textvariable=packets)
number_ping.grid(column=2, row=2, sticky=(W, E))
number_ping['values'] = tuple(str(i) for i in range(1, 101))
number_ping.current(0)

ttk.Label(mainframe, text="Intervalo de Envio (ms)").grid(column=1, row=3, sticky=W)
interval_entry = ttk.Entry(mainframe, width=20, textvariable=interval)
interval_entry.grid(column=2, row=3, sticky=(W, E))
interval_entry.insert(0, "1000")

ttk.Label(mainframe, text="Timeout (s)").grid(column=1, row=4, sticky=W)
timeout_entry = ttk.Entry(mainframe, width=20, textvariable=timeout)
timeout_entry.grid(column=2, row=4, sticky=(W, E))
timeout_entry.insert(0, "1")

pingButton = ttk.Button(mainframe, text="Executar", command=ping, padding="10 10 10 10")
pingButton.grid(column=2, row=5, sticky=(S))

resp = ttk.Label(mainframe, text="", foreground="red")
resp.grid(column=2, row=6, sticky=(W, E))

root.geometry("800x400")
root.mainloop()
