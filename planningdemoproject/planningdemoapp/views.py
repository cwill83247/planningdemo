
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
API_KEY = os.environ.get ("OPENAI_API_KEY", "API Key error")
openai.api_key = API_KEY      # this needs ot pull from environment variable or .env file !!!

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = request.POST.dict()
        question = data.get('question', '')
        response = ask_question(question)
        return JsonResponse({'answer': response})

    return render(request, 'planningchatgpt.html')

def ask_question(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=(f"I have a question: {question}\n"
                "Answer:"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer
