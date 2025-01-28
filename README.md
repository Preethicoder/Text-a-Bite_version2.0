# Text-a-Bite API

This project is a text-based API for tracking and displaying nutritional information of food items using SMS. It leverages a generative AI model (`Gemini`) to provide calorie and macronutrient estimations.

This project was developed as part of the **Masterschool 2nd Hackathon**. Special thanks to Masterschool for organizing this opportunity.

![Alt Text](assets/presentation_img/1.png)


### Presented by Team: Text-a-Bite

- **Preethi Sivakumar**
- **Nikola Brajkovic**
- **Gabo Oscar**

## About the Project

Text-a-Bite is your personal nutrition assistant, available one text away. It simplifies nutrition tracking through an SMS-based interface, making it accessible to everyone, including older adults and individuals in remote areas without access to mobile apps.

![Alt Text](assets/presentation_img/3.png)

### Why Use Text-a-Bite?

- **Convenience**: No downloads, no sign-ups, no hassle—just send a text.
- **Real-Time Insights**: Get accurate nutritional breakdowns instantly.
- **Personalized Tracking**: Save and review tracked calories for better dietary awareness.
- **Accessibility**: Works on any phone with SMS capabilities.

### Key Features

- **Instant Nutritional Breakdown**: Simply text your food items for calorie, protein, carbohydrate, and fat content.
- **Cumulative Tracking**: Use "Track" and "Display" commands to log and review your daily intake.
- **SMS-Based Simplicity**: No need for internet or apps—just text and receive reliable responses.

![Alt Text](assets/presentation_img/2.png)
![Alt Text](assets/presentation_img/4.png)
![Alt Text](assets/presentation_img/5.png)


## Requirements

- Python 3.8+
- `gemini` (Generative AI library)
- `.env` file for storing the Gemini API key (`APP_KEY`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-a-bite-api.git
   cd text-a-bite-api
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file:
   - Add your Gemini API key to the `.env` file:
     ```
     APP_KEY=your_gemini_api_key
     ```

5. Run the application:
   ```bash
   python text_a_bite_api.py
   ```

## SMS Commands

- **Track**: Log food nutrition data.
  ```
  Example: Track 1 cup rice
  ```
- **Display**: Retrieve cumulative nutritional data.
  ```
  Example: Display
  ```
- **Subscribe**: Register for the service.
  ```
  Example: SUBSCRIBE
  ```

### Future Enhancements

- Gamification and rewards for consistent tracking.
- Personalized insights and recipe recommendations.
- Multi-language support and custom alerts/reminders.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Reflections

![Alt Text](assets/presentation_img/6.png)

**Preethi Sivakumar**: “The process was stressful, but the final product made it all worthwhile. It’s always rewarding to collaborate with a group of people who bring diverse ideas and perspectives to the table.”

**Nikola Brajkovic**: “Hackathons are a great way to build skills and tackle real-world challenges. They always leave me with a taste of what it’s like to work in the industry.”

**Gabo Oscar**: “This Hackathon revealed areas for growth and inspired future project ideas. I’m grateful for the chance to learn from more experienced teammates.”

---

Thank you for supporting Text-a-Bite!

![Alt Text](assets/presentation_img/7.png)

[Download Gift Pack](downloads/gift_pack.zip)

[Download Project Documentation](docs/UserGuide.pdf)
