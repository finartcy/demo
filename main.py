import os
from openai import OpenAI

# Initialize the OpenAI client (requires openai >= 1.0.0)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_linkedin_article_prompt(trending_topic, target_audience, plan_type):
    """
    Constructs a custom prompt by injecting local variables into a template.
    """
    # The template uses {variable_name} placeholders for readability
    prompt_template = """
    You are an expert B2B copywriter. Write a highly engaging LinkedIn blog article about {trending_topic}.
    
    The primary goal of this article is to capture the attention of {target_audience} and seamlessly encourage them to sign up for our {plan_type} membership.
    
    Provide two different variations of the headline and the final call-to-action so we can A/B test their conversion rates.
    """
    
    # Inject the local variables into the template
    formatted_prompt = prompt_template.format(
        trending_topic=trending_topic,
        target_audience=target_audience,
        plan_type=plan_type
    )
    
    return formatted_prompt

def run_content_generation():
    # 1. Define local variables (these could be passed dynamically from a database or script)
    topic = "how automation is reducing overhead costs in 2027"
    audience = "agency founders"
    plan = "Elite 12-Month Annual"
    
    # 2. Build the final prompt string
    final_prompt = generate_linkedin_article_prompt(
        trending_topic=topic, 
        target_audience=audience, 
        plan_type=plan
    )
    
    # 3. Pass the formatted prompt to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a conversion-focused marketing AI."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

# Example execution
if __name__ == "__main__":
    draft = run_content_generation()
    print(draft)
