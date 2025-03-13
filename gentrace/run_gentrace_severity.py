import gentrace
import os
from dotenv import load_dotenv
# from email_creation import create_email_with_ai # TODO: REPLACE WITH YOUR PIPELINE
import openai
import tqdm

load_dotenv()

gentrace.init(os.getenv("GENTRACE_API_KEY"))

PIPELINE_SLUG = "mini-apache-error"


openai_client = openai.OpenAI(api_key=os.getenv("X_OPENAI_API_KEY"))

def run_eval(log_input):
    prompt = f"""
    Given the following log, determine whether it is:
    - notice
    - warn
    - error

    {log_input}
    """
    resp = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role":"user", "content":prompt}]
            )
    return resp.choices[0].message.content

    

def main():
    DATASET_ID="a86f513f-a9d7-4bde-b03a-1792d37276a4"
    test_cases = gentrace.get_test_cases(dataset_id=DATASET_ID)

    # Using get_test_cases() with a pipeline slug  pulls test cases for 
    # the golden dataset in the pipeline
    # test_cases = gentrace.get_test_cases(pipeline_slug=PIPELINE_SLUG)

    eval_inputs = []
    outputs = []
    print(len(test_cases))
    counter = 0
    for test_case in tqdm.tqdm(test_cases):
        # print(test_case.keys())
        
        # print(test_case["inputs"]["Expected"])
        # print(test_case["inputs"]["Log"])

        # eval_inputs.append(test_case["inputs"]["Log"])
        # outputs.append(test_case["inputs"]["Expected"])

        eval_inputs.append(test_case)

        outputs.append({
            "value": run_eval(test_case["inputs"]["Log"])
        })
        # print(outputs)
        # print(counter)
        counter += 1

    print(len(test_cases))
    print(len(outputs))

    response = gentrace.submit_test_result(PIPELINE_SLUG, eval_inputs, outputs)

    print(response)

main()
