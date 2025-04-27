# Import necessary libraries
import json


# Define the function for generating creative writing prompts
def generate_topic_content(client, user_input, model_name, temp_info):
    # Adding static context to guide the model
    context = """ You are a creative writing assistant. 
                  Your task is to generate a creative writing prompt based on the user's input.

                Instructions:
                        1. You will be given an input string (input_content).
                        2. Your task is to generate a JSON object containing:

                        3. "Headline": exactly the same as the input string.

                        4. "Content": a short, relevant paragraph (8–10 sentences) that explains, describes, or elaborates on the Headline.

                        5. Output must be in valid JSON format only.
                        6. No extra text, titles, or explanations outside the JSON block.

                Guidelines:
                    1. Headline
                       1.1 Copy the exact input string into the "Headline" field.
                       1.2 Do not modify, rephrase, or correct the input string.

                    2. Content
                       2.1 Write a concise and clear paragraph related to the headline.
                       2.2 Ensure the paragraph is informative and contextually relevant.
                       2.3 Length should be about 8 to 10 sentences.
                       2.4 Keep the language professional, clear, and easy to understand.

                    3.Formatting
                        3.1 Response must be a single JSON object.
                        3.2 Use double quotes " for keys and string values (standard JSON).
                        3.3 Properly indent the JSON for readability.

                    4.Tone
                        4.1 Maintain a neutral, informative, and engaging tone.
                        4.2 Avoid using first-person (e.g., "I think", "we believe") unless specifically related to the headline.
 
                Example:
                    Input: "AI & ML"
                    Output :{
                                "Headline": "AI & ML",
                                "Content": "Artificial Intelligence (AI) and Machine Learning (ML) are transformative technologies reshaping industries across the globe. AI refers to machines designed to simulate human intelligence, while ML focuses on enabling systems to learn and improve from experience without being explicitly programmed. Together, they power advancements in fields like healthcare, finance, and transportation, making processes smarter and more efficient."
                            }
        """
    
    # Build the conversation with context and user input
    messages = [
        {"role": "system", "content": context},  # static context
        {"role": "user", "content": user_input}  # user input
    ]
    
    # Request the model for a completion
    response = client.chat.completions.create(
                model      = model_name, #'gpt-4o-mini','gpt-4o',"gpt-3.5-turbo-1106",
                messages   = messages,
                temp       = temp_info,  # 0.5,0.6,0.7,0.8,0.9
                web_search = False
    )
    
    # Return the generated writing prompt
    response_text = response.choices[0].message.content.replace("```json","").replace('```','')
    return json.loads(response_text)

# outcome = generate_writing_prompt(user_input='AI ML& gen AI')
# print(outcome,type(outcome))