# main.py

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QVBoxLayout, QWidget, QPushButton, QTextEdit, QScrollArea, QSizePolicy)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

# Sample backend logic to generate a list of meal names for each day
def generate_meal_plan(preferences, ingredients):
    # Sample meal names for demonstration
    return {
        'Monday': {'Breakfast': 'Omelette', 'Lunch': 'Chicken Salad', 'Dinner': 'Spaghetti Carbonara'},
        'Tuesday': {'Breakfast': 'Smoothie', 'Lunch': 'Quinoa Salad', 'Dinner': 'Vegetarian Stir-Fry'},
        'Wednesday': {'Breakfast': 'Pancakes', 'Lunch': 'Turkey Sandwich', 'Dinner': 'Grilled Chicken Salad'},
        'Thursday': {'Breakfast': 'Yogurt with Berries', 'Lunch': 'Beef Tacos', 'Dinner': 'Quinoa and Black Bean Bowl'},
        'Friday': {'Breakfast': 'Avocado Toast', 'Lunch': 'Chicken Caesar Salad', 'Dinner': 'Pasta Primavera'},
        'Saturday': {'Breakfast': 'French Toast', 'Lunch': 'Veggie Wrap', 'Dinner': 'Baked Salmon'},
        'Sunday': {'Breakfast': 'Bagels with Cream Cheese', 'Lunch': 'Vegetable Soup', 'Dinner': 'Chicken Tacos'}
    }

class MealPlannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Meal Planner App')
        self.setGeometry(100, 100, 360, 640)  # Adjusted size for a phone-like view

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Create a scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to contain the main layout
        self.content_widget = QWidget()
        self.content_widget.setLayout(main_layout)

        # Set the content widget to the scroll area
        self.scroll_area.setWidget(self.content_widget)

        # Set the scroll area as the central widget
        self.setCentralWidget(self.scroll_area)

        self.createWelcomePage()

    def createWelcomePage(self):
        layout = self.content_widget.layout()
        self.clear_layout(layout)  # Clear any existing widgets from the layout

        self.label = QLabel('Welcome to Meal Planner App', self)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        layout.addWidget(self.label)

        self.pref_label = QLabel('Enter your dietary preferences (e.g., vegetarian, vegan, gluten-free):', self)
        self.pref_label.setStyleSheet("font-size: 14px; color: #666;")
        self.pref_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        layout.addWidget(self.pref_label)

        self.pref_input = QLineEdit(self)
        self.pref_input.setStyleSheet("padding: 10px; font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.pref_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        layout.addWidget(self.pref_input)

        self.ingr_label = QLabel('Enter the ingredients you have available:', self)
        self.ingr_label.setStyleSheet("font-size: 14px; color: #666;")
        self.ingr_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        layout.addWidget(self.ingr_label)

        self.ingr_input = QTextEdit(self)
        self.ingr_input.setStyleSheet("padding: 10px; font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.ingr_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.ingr_input)

        self.submit_btn = QPushButton('Submit', self)
        self.submit_btn.setStyleSheet("padding: 10px; font-size: 14px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        self.submit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.submit_btn.clicked.connect(self.showMealPlan)
        layout.addWidget(self.submit_btn)

    def showMealPlan(self):
        preferences = self.pref_input.text()
        ingredients = self.ingr_input.toPlainText()
        self.meal_plan_page(preferences, ingredients)

    def meal_plan_page(self, preferences, ingredients):
        layout = self.content_widget.layout()
        self.clear_layout(layout)  # Clear any existing widgets from the layout

        self.meal_plan_label = QLabel('Your Weekly Meal Plan:', self)
        self.meal_plan_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        self.meal_plan_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        layout.addWidget(self.meal_plan_label)

        meal_plan = generate_meal_plan(preferences, ingredients)
        self.meals = meal_plan  # Store the meal plan for later use

        for day, meals in meal_plan.items():
            day_label = QLabel(f'{day}:', self)
            day_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #444; margin-top: 10px;")
            layout.addWidget(day_label)

            for meal_time, meal in meals.items():
                meal_btn = QPushButton(f'{meal_time}: {meal}', self)
                meal_btn.setStyleSheet("padding: 10px; font-size: 14px; background-color: #2196F3; color: white; border: none; border-radius: 5px; margin-bottom: 5px;")
                # Use lambda to pass the meal name to the view_recipe method
                meal_btn.clicked.connect(lambda checked, m=meal: self.view_recipe(m))
                layout.addWidget(meal_btn)

        self.back_btn = QPushButton('Back', self)
        self.back_btn.setStyleSheet("padding: 10px; font-size: 14px; background-color: #f44336; color: white; border: none; border-radius: 5px; margin-top: 10px;")
        self.back_btn.clicked.connect(self.createWelcomePage)
        layout.addWidget(self.back_btn)

    def view_recipe(self, meal):
        layout = self.content_widget.layout()
        self.clear_layout(layout)  # Clear any existing widgets from the layout

        self.recipe_label = QLabel(f'Recipe for {meal}:', self)
        self.recipe_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        self.recipe_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        layout.addWidget(self.recipe_label)

        # Sample recipe details
        recipes = {
            'Omelette': 'Ingredients:\n- Eggs\n- Milk\n- Cheese\n- Vegetables\n\nInstructions: Whisk eggs, pour into a hot pan, and add fillings.',
            'Chicken Salad': 'Ingredients:\n- Chicken\n- Lettuce\n- Tomatoes\n- Cucumber\n\nInstructions: Grill chicken, mix with vegetables, and serve.',
            'Spaghetti Carbonara': 'Ingredients:\n- Spaghetti\n- Eggs\n- Parmesan Cheese\n- Bacon\n\nInstructions: Cook spaghetti, mix with eggs and cheese, add bacon.',
            'Smoothie': 'Ingredients:\n- Banana\n- Berries\n- Yogurt\n- Honey\n\nInstructions: Blend all ingredients until smooth.',
            'Quinoa Salad': 'Ingredients:\n- Quinoa\n- Bell Peppers\n- Black Beans\n- Avocado\n\nInstructions: Cook quinoa, mix with vegetables and beans.',
            'Grilled Chicken Salad': 'Ingredients:\n- Chicken\n- Lettuce\n- Tomatoes\n- Cucumber\n\nInstructions: Grill chicken, mix with vegetables, and serve.',
            'Pancakes': 'Ingredients:\n- Flour\n- Eggs\n- Milk\n- Sugar\n\nInstructions: Mix ingredients, cook on a griddle, and serve with syrup.',
            'Turkey Sandwich': 'Ingredients:\n- Turkey\n- Bread\n- Lettuce\n- Tomato\n- Mayonnaise\n\nInstructions: Assemble ingredients between slices of bread.',
            'Baked Salmon': 'Ingredients:\n- Salmon\n- Lemon\n- Herbs\n\nInstructions: Bake salmon with lemon and herbs.',
            'Pasta Primavera': 'Ingredients:\n- Pasta\n- Mixed Vegetables\n- Parmesan Cheese\n\nInstructions: Cook pasta and vegetables, mix with cheese.',
            'Avocado Toast': 'Ingredients:\n- Avocado\n- Bread\n- Salt\n- Pepper\n\nInstructions: Mash avocado, spread on toast, and season.',
            'Vegetable Soup': 'Ingredients:\n- Mixed Vegetables\n- Broth\n- Herbs\n\nInstructions: Cook vegetables in broth with herbs.',
            'Bagels with Cream Cheese': 'Ingredients:\n- Bagels\n- Cream Cheese\n\nInstructions: Spread cream cheese on toasted bagels.'
        }

        recipe_details = recipes.get(meal, 'Recipe not found.')
        self.recipe_details = QLabel(recipe_details, self)
        self.recipe_details.setStyleSheet("font-size: 14px; color: #555; white-space: pre-wrap;")  # Preserve line breaks
        self.recipe_details.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.recipe_details)

        self.back_btn = QPushButton('Back', self)
        self.back_btn.setStyleSheet("padding: 10px; font-size: 14px; background-color: #f44336; color: white; border: none; border-radius: 5px; margin-top: 10px;")
        self.back_btn.clicked.connect(self.showMealPlan)
        layout.addWidget(self.back_btn)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MealPlannerApp()
    ex.show()
    sys.exit(app.exec_())
