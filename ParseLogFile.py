# /Users/jeetendave259/Documents/System_Log_2026_03_13.log

import collections

def get_top_error_ips(filename):
    # Use a dictionary to store counts: { "IP": count }
    ip_counts = collections.defaultdict(int)
    
    try:
        # Open file as an iterator (one line at a time)
        with open(filename, 'r') as f:
            for line in f:
                # 1. Split the line into parts
                parts = line.split()
                if len(parts) < 9: # Basic malformed check
                    continue
                
                ip = parts[0]
                status_code = parts[-2] # Status code is usually second to last
                
                # 2. Filter for 500 errors
                if status_code == "500":
                    ip_counts[ip] += 1
                    
    except FileNotFoundError:
        print("File not found.")
        return

    # 3. Get top 5 using sorted() or Counter.most_common()
    top_5 = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    
    for ip, count in top_5:
        print(f"{ip}: {count}")

# To run: get_top_error_ips('production_access.log')
get_top_error_ips('/Users/jeetendave259/Documents/System_Log_2026_03_13.log')