import sys

if len(sys.argv)  != 3:
    print("Podałes zła liczbe argumentów")
    exit()

_, file_in, file_out = sys.argv

good_emails = set()

with open(file_in) as f:

    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            good_emails.add(line)


final_email = sorted(good_emails)

with open(file_out, "w") as f:
    for email in final_email:
        f.write(email + "\n")

        #lub:
        # out = "\n".join(emails)
        #