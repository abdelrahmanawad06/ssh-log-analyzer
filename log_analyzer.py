with open("OpenSSH_2k.log") as f:
    logs = f.readlines()
logs.append("Dec 10 09:00:00 LabSZ sshd[99999]: Accepted password for root from 183.62.140.253 port 22 ssh2")

print(len(logs))

counts = {}

for line in logs:
    if "Failed password" in line:
        words = line.split()
        ip = words[words.index("from") + 1]
        counts[ip] = counts.get(ip, 0) + 1

for ip in counts:
    print(ip, counts[ip])


sorted_ips = sorted(counts, key=counts.get, reverse=True)

alerts = 0

for ip in sorted_ips:
    if counts[ip] >= 5:
        print("ALERT:", ip, "failed", counts[ip], "times")
        alerts = alerts + 1

print("Total suspicious IPs:", alerts)

for line in logs:
    if "Accepted password" in line:
        words = line.split()
        ip = words[words.index("from") + 1]
        if counts.get(ip, 0) >= 5:
            print("BREAK-IN WARNING:", ip, "logged in after", counts[ip], "failed attempts")