"""
Created by Deena Nath Srivastava on 28/11/18
"""

import re

email_count = 0
ip_count = 0
total_lines = 0
unique_email = []
unique_ip = []
unique_call = []
# open('emails.txt', 'w').close()
# open('ip.txt', 'w').close()

with open('regex.txt', 'r', encoding='utf8', errors='ignore') as f:
    with (open('emails.txt', 'w')) as email:
        with (open('ip.txt', 'w')) as ip:
            with (open('calls.txt', 'w')) as call:

                for line in f:
                    # print(line)
                    a = re.findall(r'[\w-]+@[\w-]+', line)
                    b = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)
                    c = re.findall(r'[\d+%]\d+\-[\d+\w+]\w+.\d+\-[\d+\w+]\w+\d+', line)
                    if len(a) > 0:
                        # print(a[0])
                        for i in a:
                            if i in unique_email:
                                pass
                            else:
                                email_count += 1
                                email.write(i + "\n")
                                unique_email.append(i)

                    if len(b) > 0:
                        # print(b[0])
                        for i in b:
                            if i in unique_ip:
                                pass
                            else:
                                ip_count += 1
                                ip.write(i + "\n")
                                unique_ip.append(i)

                    total_lines += 1

                    if len(c) > 0:
                        # print(a[0])
                        for i in c:
                            if i in unique_call:
                                pass
                            else:
                                call.write(i + "\n")
                                unique_call.append(i)




print("Number of email addresses found are: " + str(email_count) + " in " + str(total_lines))
print("Number of ip addresses found are: " + str(ip_count) + " in " + str(total_lines))
