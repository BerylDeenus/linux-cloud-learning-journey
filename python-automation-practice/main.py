from checks import check
usage = float(input("enter the disk usage in percentage: "))
status = check(usage)
print(f"usage: {usage}%")
print(f"status: {status}")
