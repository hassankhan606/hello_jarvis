"""modules/system_info.py — Live CPU, RAM, Disk, Network stats."""

import psutil, datetime, platform
from rich.table import Table
from rich       import box

def sys_stats():
    t = Table(title="System Status", box=box.SIMPLE_HEAD,
              border_style="cyan", expand=False)
    t.add_column("Metric",  style="bold yellow", no_wrap=True)
    t.add_column("Value",   style="white")

    # CPU
    cpu  = psutil.cpu_percent(interval=0.5)
    freq = psutil.cpu_freq()
    t.add_row("CPU Usage",     f"{cpu}%")
    t.add_row("CPU Freq",      f"{freq.current:.0f} MHz" if freq else "N/A")
    t.add_row("CPU Cores",     str(psutil.cpu_count()))

    # RAM
    ram = psutil.virtual_memory()
    t.add_row("RAM Used",      f"{ram.used/1e9:.2f} GB / {ram.total/1e9:.2f} GB  ({ram.percent}%)")

    # Disk
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            t.add_row(f"Disk {part.device}",
                      f"{usage.used/1e9:.1f} GB / {usage.total/1e9:.1f} GB  ({usage.percent}%)")
        except Exception:
            pass

    # Network
    net = psutil.net_io_counters()
    t.add_row("Net Sent",      f"{net.bytes_sent/1e6:.1f} MB")
    t.add_row("Net Recv",      f"{net.bytes_recv/1e6:.1f} MB")

    # OS / uptime
    boot = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = str(datetime.datetime.now() - boot).split(".")[0]
    t.add_row("OS",            platform.platform())
    t.add_row("Uptime",        uptime)
    t.add_row("Python",        platform.python_version())

    return t
