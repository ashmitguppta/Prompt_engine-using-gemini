#library
import google.generativeai as genai

gemini_api_key = "AIzaSyBxlgIbAB4HzZfuZr-u202H_eEjjnY1Kpk"
genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash-001")

def run_prompt(prompt_type,user_input):
    if prompt_type ==  "Zero-Shot":
        prompt = f"{user_input}"

    elif prompt_type == "Few-Shot":
        prompt = (
            "Q : Who is the president of india\n\n"
            "A : Ms. Draupadi Murmu"
            "Q : WHo is the President of United States\n\n"
            "A : Mr. Donald Trump"

            f"Q{user_input}\n"
            "A : "

        )
    elif prompt_type == "Instruction-Based":
        prompt = (
            "Instruction: Summarize my article in 3 bullet points"
            f"Text : {user_input}"
        )
    elif prompt_type == "Chain-of-Thought":
        prompt =(

            "Solve the neural backpropagation equation step by step"
            f"Text:{user_input}"
        )
    elif prompt_type == "Role-Based":
        prompt = (
            "You are a real estate consultant, pls tell me where and why should i purchase a property in Gurgaon"
            f"Text:{user_input}"
        )
    else :
        prompt = user_input

    response = model.generate_content(prompt)
    return response.text.strip()