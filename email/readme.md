# Python SMTP Email with HTML Body

This guide explains how to send emails using Python's built-in `smtplib` library with an HTML message body. You can also dynamically inject arguments into the HTML content to personalize your emails.

## Requirements

- Python 3.x
- Gmail account (or another email provider with SMTP support)

## Libraries Used

- **smtplib**: A Python library for sending emails using SMTP (Simple Mail Transfer Protocol).
- **email.mime**: Classes for constructing email messages.
- **Jinja2** (Optional): For advanced HTML templating.

## Installation

The `smtplib` and `email.mime` libraries are part of Python's standard library, so no additional installation is required.

If you plan to use **Jinja2** for HTML templating, install it via pip:

```bash
pip install Jinja2
