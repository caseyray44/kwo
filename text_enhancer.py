def enhance_text(text, text_type):
    if not text.strip():
        return text
    text = text.strip()
    
    if text_type == "title":
        return text.title()
    
    elif text_type == "description":
        text = text.replace("must", "should").replace("required", "recommended")
        if not text.startswith(("Welcome", "This", "At KW")):
            text = f"Welcome to our guide on {text.lower()}" if "intro" in text.lower() else f"This section covers {text.lower()}"
        return text.capitalize()
    
    elif text_type == "list":
        lines = []
        for line in text.split("\n"):
            line = line.strip()
            if not line:
                continue
            line = line.lower()
            if line.startswith(("do ", "ensure ", "complete ")):
                line = line.replace("do ", "").replace("ensure ", "").replace("complete ", "")
                line = f"Please {line}"
            elif not line.startswith("please"):
                line = f"Please {line}"
            line = line.replace("immediately", "promptly").replace("must", "should")
            lines.append(line.capitalize())
        return "\n".join(lines)
    
    return text
