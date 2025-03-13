from opik import Opik, track
from opik.evaluation import evaluate
from opik.evaluation.metrics import Equals, Hallucination
from opik.integrations.openai import track_openai
import openai
from dotenv import load_dotenv

import os

load_dotenv()

print(os.getenv("X_OPENAI_API_KEY"))


# Define the task to evaluate
openai_client = track_openai(openai.OpenAI(api_key=os.getenv("X_OPENAI_API_KEY")))
MODEL = "gpt-3.5-turbo"
@track
def your_llm_application(input: str) -> str:
    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": input}],
    )
    return response.choices[0].message.content
# Define the evaluation task
def evaluation_task(x):
    return {
        "output": your_llm_application(x['input'])
    }
# Create a simple dataset
client = Opik()
dataset = client.get_or_create_dataset(name="Example dataset")
dataset.insert([
    {"input": "What is the capital of France?"},
    {"input": "What is the capital of Germany?"},
])
# Define the metrics
hallucination_metric = Hallucination()
evaluation = evaluate(
    dataset=dataset,
    task=evaluation_task,
    scoring_metrics=[hallucination_metric],
    experiment_config={
        "model": MODEL
    }
)
