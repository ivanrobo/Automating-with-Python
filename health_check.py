#!/usr/bin/env python3
import emails
import psutil
import socket


def check_cpu():
    if psutil.cpu_percent() > 80:
        message = emails.generate_email(sender="automation@example.com",
                                        recipient="@example.com",
                                        subject="Error - CPU usage is over 80%",
                                        body="Please check your system and resolve the issue as soon as possible.")

        emails.send_email(message)


def check_disk():
    if psutil.disk_usage('/').percent > 80:
        message = emails.generate_email(sender="automation@example.com",
                                        recipient="@example.com",
                                        subject="Error - Available disk space is less than 20%",
                                        body="Please check your system and resolve the issue as soon as possible.")

        emails.send_email(message)


def check_ram():
    memory = psutil.virtual_memory()
    limit = 500 * 1024 * 1024
    if memory.available < limit:
        message = emails.generate_email(sender="automation@example.com",
                                        recipient="@example.com",
                                        subject="Error - Available memory is less than 500MB",
                                        body="Please check your system and resolve the issue as soon as possible.")
        emails.send_email(message)


def check_localhost():
    try:
        if socket.gethostbyname("localhost") != '127.0.0.1':
            message = emails.generate_email(sender="automation@example.com",
                                            recipient="@example.com",
                                            subject="Error - localhost cannot be resolved to 127.0.0.1",
                                            body="Please check your system and resolve the issue as soon as possible.")
            emails.send_email(message)
    except socket.error:
        message = emails.generate_email(sender="automation@example.com",
                                        recipient="@example.com",
                                        subject="Error - localhost cannot be resolved to 127.0.0.1",
                                        body="Please check your system and resolve the issue as soon as possible.")
        emails.send_email(message)


if __name__ == '__main__':
    check_cpu()
    check_disk()
    check_ram()
    check_localhost()