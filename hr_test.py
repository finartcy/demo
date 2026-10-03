import os
from openai import OpenAI

# Initialize the client. 
# It will automatically look for an environment variable named "OPENAI_API_KEY"
client = OpenAI()

def generate_fevs_analysis_prompt(fevs_comment, occupational_series, target_competencies):
    """
    Constructs a custom prompt by injecting local variables into a template.
    """
    prompt_template = """
    You are an expert federal organizational psychologist and data scientist. 
    Review the following qualitative, anonymized employee comment from the annual FEVS survey:
    
    "{fevs_comment}"
    
    The employee belongs to the {occupational_series} job series. 
    
    Your task:
    1. Extract the core theme (e.g., leadership communication, resource constraints, burnout).
    2. Map this theme against the following OPM competencies: {target_competencies}.
    3. Provide a brief, actionable recommendation for a federal branch chief to address this feedback.
    """
    
    formatted_prompt = prompt_template.format(
        fevs_comment=fevs_comment,
        occupational_series=occupational_series,
        target_competencies=target_competencies
    )
    
    return formatted_prompt

def run_fevs_theme_extraction():
    # 1. Define local variables (representing a row in a federal dataset)
    comment = "We are constantly bogged down by manual data entry. We have the budget for new software, but the ATO approval process takes so long that the tools are outdated by the time we get them."
    series = "GS-1560 Data Scientist"
    competencies = "Technology Management, Strategic Thinking, Flexibility"
    
    # 2. Build the final prompt string
    final_prompt = generate_fevs_analysis_prompt(
        fevs_comment=comment, 
        occupational_series=series, 
        target_competencies=competencies
    )
    
    # 3. Pass the formatted prompt to the FedRAMP-aligned API (OpenAI placeholder)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a qualitative analytics AI aligned with OPM psychometric standards."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.3 # Lowered temperature for analytical consistency rather than creative variance
    )
    
    return response.choices[0].message.content

# Example execution
if __name__ == "__main__":
    analysis_report = run_fevs_theme_extraction()
    print(analysis_report)
