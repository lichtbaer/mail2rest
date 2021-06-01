from typing import Optional

from fastapi import FastAPI
from imap_tools import MailBox, AND


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/mails/{inbox}/{item_id}")
def read_mails(inbox: str, item_id: str, q: Optional[str] = None):
    mailbox = MailBox(q)
    mailbox.login('mailadresse', item_id , initial_folder=inbox)
    subjects = [{"text": msg.text} for msg in mailbox.fetch(AND(all=True))]
    return subjects



@app.get("/mails")
def read_mail():
    mailbox = MailBox('imap.mailbox.org')
    mailbox.login('mailadresse', 'passwort', initial_folder='INBOX')
    subjects = [{"text": msg.text} for msg in mailbox.fetch(AND(all=True))]
    return subjects