
import os
from dotenv import load_dotenv
import google.generativeai as genai



load_dotenv()
APP_KEY = os.getenv("APP_KEY")
def get_nutrition(text,display= False):
    refined_query = ""
    genai.configure(api_key=APP_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
   # response = model.generate_content(f"calorieee vlue of {qty} {text} with percentage of content with out explaination")

    if display:
       refined_query =refined_query=(f"Calculate the approximate total calories and macronutrient composition for the following list of food items: {text}. "
                                      f"Provide a general estimate, even if specific details about preparation or type are missing . Dont include any extra text. Present the results as: Total calories till now: [value] kcal, protein: [value] g, carbohydrates: [value] g, fats: [value] g format the answer in SMS format for every new line")
    else:
       refined_query=(f"Provide the calorie value and percentage composition of {text}. "
                     f"if no  quantity or measure provided given average calories value"
                     f"Include only numerical values with the units. Dont include any extra text.Present the results as: calories of given food name also give default measure as [Food Name] (Default Measure): [calories] kcal, protein: [protein] g, carbs: [carbs] g, fats: [fats] g format the answer in SMS format for every new line")
    response = model.generate_content(refined_query)
    text = response.text
    print(text)
    return response.text

def main():
    get_nutrition('Track rice',True )

if __name__ == "__main__":
    main()








