def sendmail(subject, tolist, content ):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    mail_content = content

    # The mail addresses and password
    from_address = 'bitsassignment111@gmail.com'
    from_pass = 'BitsPassword$1'
    to_address = tolist # from input parameter

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = ", ".join(to_address)
    message['Subject'] = subject  # from input parameter

    # The body and the attachments for the mail (if any - as of now, it is a plain mail)
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    # use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)
    # enable security
    session.starttls()
    # login with mail_id and password
    session.login(from_address, from_pass)

    text = message.as_string()
    session.sendmail(from_address, to_address, text)
    session.quit()
    print('Mail Sent')
    return
