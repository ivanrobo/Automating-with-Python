#!/usr/bin/env python 3
import reports
import emails
import os
import datetime


def process_data(path):
    content = ""
    for file in filter(lambda x: x.endswith(".txt"), os.listdir(path)):
        with open(os.path.join(path, file)) as f:
            content += "name: {}<br/>weight: {}<br/><br/>".format(f.readline().strip(), f.readline().strip())
    return content


if __name__ == '__main__':
    path = "supplier_data/descriptions"
    now = datetime.datetime.now()
    reports.generate_report(attachment="/tmp/processed.pdf",
                            title="Processed Update on {}".format(now.strftime("%m/%d/%Y")),
                            paragraph=process_data(path))
    message = emails.generate_email(sender="automation@example.com",
                                    recipient="@example.com",
                                    subject="Upload Completed - Online Fruit Store",
                                    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                                    attachment_path="/tmp/processed.pdf")
    emails.send_email(message)
