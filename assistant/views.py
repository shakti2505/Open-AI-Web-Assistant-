from django.shortcuts import render, redirect
import openai
from dotenv import load_dotenv
import os   
from pathlib import Path
dotenv_path = Path('webassistant/.env')

load_dotenv(dotenv_path=dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")


# Create your views here.
 

def home(request):
    try:
        if request.method == "POST":
            prompt = request.POST.get('prompt')
            res = openai.Completion.create(model='text-davinci-003', prompt=prompt, temperature=1, max_tokens= 1000 )
            formatted_response= res['choices'][0]['text']
            return render(request, 'assistant/home.html', {'prompt':prompt, 'formatted_response':formatted_response})
        else:
            return render(request, 'assistant/home.html')
    except:
        return redirect('error_handler')




    
def error_handler(request):
 return render(request, 'assistant/404.html')