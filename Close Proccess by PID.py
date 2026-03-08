import psutil     # Removed line 3-10, because it crashes the whole thing.

# def list_all_processes():
#     print("Listing all running processes:")
#     for proc in psutil.process_iter(['pid', 'name', 'username']):
#         try:
#             process_info = proc.info
#             print(f"Process name: {process_info['name']} (PID: {process_info['pid']}) User: {process_info['username']}")
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
#             print(f"Could not access process: {e}")

def close_application_by_pid(pid):
    try:
        proc = psutil.Process(pid)
        proc_name = proc.name()
        print(f"Attempting to close application: {proc_name} (PID: {pid})")
        proc.terminate()  # Terminate the process
        proc.wait(timeout=5)  # Wait for the process to terminate with a timeout
        print(f"Closed application: {proc_name} (PID: {pid})")
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        print(f"Could not terminate process PID: {pid}: {e}")
        return False

#Ask which PID you want to close

pid = int(input("Enter the PID of the application you want to close: "))
close_application_by_pid(pid)
