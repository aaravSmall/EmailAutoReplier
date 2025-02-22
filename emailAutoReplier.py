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

# Example usage
email_subject = "Meeting Request for Next Week"
email_body = "Hi, I hope you're doing well. I wanted to check if you're available for a meeting next week to discuss our project updates. Let me know your availability."

reply = generate_reply(email_subject, email_body)
print(reply)
