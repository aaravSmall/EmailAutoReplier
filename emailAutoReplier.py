import openai

def generate_reply(email_subject, email_body):
    prompt = f"""
    You are an AI assistant that generates professional email replies. Given the following email:
    
    Subject: {email_subject}
    
    Body:
    {email_body}
    
    Provide a polite, concise, and relevant reply.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful email assistant."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"].strip()

# Get user input
email_subject = input("Enter the email subject: ")
email_body = input("Enter the email body: ")

reply = generate_reply(email_subject, email_body)
print("\nGenerated Reply:\n", reply)
