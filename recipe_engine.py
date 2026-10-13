# ==========================================
# STEP 2 PORTFOLIO: PYTHON SMART-KITCHEN ENGINE
# Schema-matching engine for culinary data optimization
# ==========================================

# Mock database dictionary storing recipes and required ingredient arrays
RECIPE_DATABASE = [
    {
        "name": "Classic Tomato Basil Pasta",
        "category": "Italian",
        "ingredients": {"pasta", "tomato", "garlic", "basil", "olive oil"}
    },
    {
        "name": "Quick Paneer Stir-Fry",
        "category": "North Indian",
        "ingredients": {"paneer", "capsicum", "onion", "ginger", "soy sauce", "oil"}
    },
    {
        "name": "Fluffy Banana Pancakes",
        "category": "Breakfast",
        "ingredients": {"banana", "flour", "milk", "sugar", "butter"}
    },
    {
        "name": "Garlic Butter Mushrooms",
        "category": "Continental",
        "ingredients": {"mushroom", "garlic", "butter", "pepper", "parsley"}
    },
    {
        "name": "Street-Style Masala Maggi",
        "category": "Snacks",
        "ingredients": {"maggi", "onion", "tomato", "chilli", "masala"}
    }
]

def find_matching_recipes(available_ingredients):
    """
    Core algorithmic matcher logic block.
    Compares user sets against recipe database subsets.
    """
    # Standardize input strings: lowercase and strip extra whitespaces
    user_ingredients = {ing.strip().lower() for ing in available_ingredients if ing.strip()}
    
    print(f"\nSearching database for items you can cook with: {list(user_ingredients)}")
    print("-" * 50)
    
    matches_found = 0
    
    for recipe in RECIPE_DATABASE:
        recipe_ingredients = recipe["ingredients"]
        
        # Core logic check: Is the required recipe ingredients a subset of user items?
        if recipe_ingredients.issubset(user_ingredients):
            print(f"✅ MATCH FOUND: {recipe['name']} [{recipe['category']}]")
            print(f"   -> Required items: {', '.join(recipe_ingredients)}")
            matches_found += 1
        else:
            # Check for partial availability to offer helpful context
            missing_items = recipe_ingredients - user_ingredients
            # If the user has more than 50% of the ingredients, display as close match
            if len(missing_items) <= 2:
                print(f"⚠️  ALMOST MATCH: {recipe['name']} (Missing: {', '.join(missing_items)})")

    if matches_found == 0:
        print("\n❌ No exact matches found. Try updating your fridge inventory parameters!")

# --- Execution sequence simulation on runtime setup ---
if __name__ == "__main__":
    print("==================================================")
    print("         AURA SMART-KITCHEN BOT (BACKEND DETECTOR) ")
    print("==================================================")
    
    # Simulating a user typing what ingredients they have inside their fridge
    print("Enter the ingredients you have available (separated by commas).")
    print("Example: tomato, pasta, garlic, basil, olive oil, onion\n")
    
    user_input = input("Your Fridge Inventory: ")
    
    # Split the raw string by comma separator parameters into a list array
    fridge_items = user_input.split(",")
    
    # Trigger matching engine function logic
    find_matching_recipes(fridge_items)
