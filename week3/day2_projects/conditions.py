disk_usage = 85

if disk_usage > 90:
    print("CRITICAL")
elif disk_usage >= 70:
    print("WARNING")
else:
    print("OK")
