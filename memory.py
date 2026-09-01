history=[]

def add(role,text):
    history.append({
        "role": role,
        "parts": [{"text":text}]
    })

def get():
    return history  