import platform
import socket
import psutil
from datetime import datetime


def line():
    print("-" * 55)


def get_size(bytes_value):
    gb = bytes_value / (1024 ** 3)
    return f"{gb:.2f} GB"


def show_system_info():
    print("\n🖥️  SYSTEM INFORMATION")
    line()

    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"OS Version       : {platform.version()}")
    print(f"Computer Name    : {socket.gethostname()}")
    print(f"Architecture     : {platform.machine()}")
    print(f"Processor        : {platform.processor()}")


def show_cpu_info():
    print("\n⚙️  CPU INFORMATION")
    line()

    print(f"CPU Cores        : {psutil.cpu_count(logical=False)} Physical")
    print(f"CPU Threads      : {psutil.cpu_count(logical=True)} Logical")
    print(f"CPU Usage        : {psutil.cpu_percent(interval=1)}%")


def show_memory_info():
    print("\n🧠 MEMORY INFORMATION")
    line()

    memory = psutil.virtual_memory()

    print(f"Total RAM        : {get_size(memory.total)}")
    print(f"Used RAM         : {get_size(memory.used)}")
    print(f"Available RAM    : {get_size(memory.available)}")
    print(f"RAM Usage        : {memory.percent}%")


def show_storage_info():
    print("\n💾 STORAGE INFORMATION")
    line()

    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            print(f"\nDrive            : {partition.device}")
            print(f"Mount Point      : {partition.mountpoint}")
            print(f"Total Space      : {get_size(usage.total)}")
            print(f"Used Space       : {get_size(usage.used)}")
            print(f"Free Space       : {get_size(usage.free)}")
            print(f"Usage            : {usage.percent}%")

        except PermissionError:
            continue


def show_network_info():
    print("\n🌐 NETWORK INFORMATION")
    line()

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error:
        ip_address = "Unable to detect"

    print(f"Hostname         : {hostname}")
    print(f"Local IP         : {ip_address}")


def main():
    print("=" * 55)
    print("       PC DIAGNOSTIC TOOLKIT v1.0")
    print("=" * 55)

    print(f"Scan Time        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    show_system_info()
    show_cpu_info()
    show_memory_info()
    show_storage_info()
    show_network_info()

    print("\n")
    line()
    print("✅ System scan completed.")
    line()


if __name__ == "__main__":
    main()