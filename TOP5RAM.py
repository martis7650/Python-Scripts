import subprocess


def top_memory_processes():
  print("--- TOP 5 proces on Lubuntu ( RAM ) ---")
  cmd = "ps -eo pid,%mem,%cpu,comm --sort=-%mem | head -n 6"
  result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  print(result.stdout)


top_memory_processes()
