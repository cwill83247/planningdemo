
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = 

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
