import csv
import os


def save_leads(leads):

    file_exists = os.path.exists("leads.csv")

    seen = set()

    with open(
        "leads.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Website",
                "Company",
                "Email",
                "Phone",
                "Facebook",
                "Instagram",
                "LinkedIn",
                "X"
            ])

        for lead in leads:

            email = ", ".join(lead["emails"])

            if email in seen:
                continue

            seen.add(email)

            writer.writerow([
                lead["website"],
                lead["company"],
                email,
                ", ".join(lead["phones"]),
                ", ".join(lead["facebook"]),
                ", ".join(lead["instagram"]),
                ", ".join(lead["linkedin"]),
                ", ".join(lead["x"])
            ])