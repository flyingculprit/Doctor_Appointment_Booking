from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure API key for Google Gemini (PaLM 2)
genai.configure(api_key="AIzaSyABi2JxvIjYdkiS0es6Uu_jBT_H1mRAB5Q")

# Expanded food recommendations for vitamins
VITAMIN_FOOD_MAP = {
    "Vitamin A": ["Carrots", "Spinach", "Sweet potatoes", "Egg yolks", "Liver", "Dairy products"],
    "Vitamin B1 (Thiamine)": ["Whole grains", "Pork", "Nuts", "Seeds", "Legumes"],
    "Vitamin B2 (Riboflavin)": ["Milk", "Eggs", "Green leafy vegetables", "Almonds"],
    "Vitamin B3 (Niacin)": ["Chicken", "Turkey", "Fish", "Peanuts", "Mushrooms"],
    "Vitamin B5 (Pantothenic Acid)": ["Avocados", "Sunflower seeds", "Eggs", "Dairy products"],
    "Vitamin B6 (Pyridoxine)": ["Bananas", "Potatoes", "Chicken", "Fish", "Nuts"],
    "Vitamin B7 (Biotin)": ["Eggs", "Almonds", "Whole grains", "Spinach"],
    "Vitamin B9 (Folate/Folic Acid)": ["Leafy greens", "Lentils", "Citrus fruits", "Beets"],
    "Vitamin B12": ["Meat", "Fish", "Dairy products", "Eggs", "Fortified cereals"],
    "Vitamin C": ["Oranges", "Strawberries", "Bell peppers", "Broccoli", "Kiwi"],
    "Vitamin D": ["Salmon", "Egg yolks", "Mushrooms", "Fortified milk"],
    "Vitamin E": ["Almonds", "Sunflower seeds", "Spinach", "Avocado"],
    "Vitamin K": ["Kale", "Spinach", "Broccoli", "Brussels sprouts"],
    "Iron": ["Red meat", "Lentils", "Spinach", "Tofu", "Pumpkin seeds"]
}

app = Flask(__name__)

def get_medical_info(disease_name):
    """Fetches medical information about a disease and recommends foods."""
    prompt = f"Provide information on {disease_name}. Include causes, symptoms, treatments, and dietary recommendations. each topic i need in 1 line so totally 4 lines. in neat format easily understandable not in capital letter segrigate in -,:,; etc. and also include vitamin deficiency if any. and include 1) \n 2)\n  3)\n like i need "
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    result = response.text

    # Check if any vitamin is mentioned in the treatment and suggest foods
    food_suggestions = ""
    for vitamin, foods in VITAMIN_FOOD_MAP.items():
        if vitamin.lower() in result.lower():  # Case-insensitive check
            food_suggestions += f"\n**Recommended Foods for {vitamin}:** " + ", ".join(foods)

    # Append food recommendations if found
    if food_suggestions:
        result += "\n\n**Dietary Recommendations:**" + food_suggestions

    return result

@app.route("/get_disease_info", methods=["GET"])
def get_disease_info():
    disease_name = request.args.get("disease", "").strip()
    if not disease_name:
        return jsonify({"error": "No disease name provided"}), 400

    try:
        disease_info = get_medical_info(disease_name)
        return jsonify({"result": disease_info})
    except Exception as e:
        return jsonify({"error": f"Failed to fetch disease info: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)