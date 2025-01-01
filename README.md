# Mental Health Bot

## Introduction
The Mental Health Bot is a Python-based chatbot designed to provide emotional support, resources, and activities to promote mental well-being. It can analyze user sentiment, suggest activities, share mental health tips, provide affirmations, and even guide breathing exercises. This bot can serve as a friendly companion to help users navigate mental health challenges.

---

## Features

- **Time and Date Retrieval**: Get the current time and date in a friendly format.
- **Activity Suggestions**: Suggests activities based on user mood.
- **Music and Videos**: Opens relaxing music or motivational video playlists on YouTube.
- **Mental Health Resources**: Links to reputable mental health resources.
- **Sentiment Analysis**: Analyzes user input to determine sentiment (positive, negative, or neutral).
- **Affirmations**: Provides positive affirmations to uplift the user.
- **Mental Health Tips**: Shares actionable mental health tips.
- **Jokes**: Shares light-hearted jokes to brighten the user's mood.
- **Quiz**: Offers a mental health awareness quiz.
- **Breathing Exercises**: Guides simple breathing exercises to reduce stress.
- **Gratitude List**: Encourages users to create a gratitude list to stay positive.
- **Emergency Contact Encouragement**: Prompts users to contact a trusted person or helpline during a crisis.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mental-health-bot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd mental-health-bot
   ```

3. Install the required dependencies:
   ```bash
   pip install textblob
   ```

---

## Usage

Run the bot using Python:
```bash
python mental_health_bot.py
```

Interact with the bot by typing messages, such as:
- "What time is it?"
- "Can you suggest an activity?"
- "Tell me a joke."
- "I feel stressed."

---

## Functionality Overview

### Key Functions

1. **`get_time()`**: Returns the current time.
2. **`get_date()`**: Returns the current date.
3. **`suggest_activities()`**: Suggests activities to improve mental well-being.
4. **`play_music()`**: Opens a YouTube search for relaxing music.
5. **`open_resources()`**: Opens a mental health resource website.
6. **`analyze_sentiment(user_input)`**: Analyzes the sentiment of user input.
7. **`provide_affirmation()`**: Shares a positive affirmation.
8. **`mental_health_tips()`**: Provides actionable mental health tips.
9. **`recommend_videos()`**: Opens motivational videos on YouTube.
10. **`share_joke()`**: Shares a joke to lighten the mood.

### Additional Functions

- **`quiz()`**: Starts a mental health awareness quiz.
- **`handle_quiz_response()`**: Validates user responses to the quiz.
- **`breathing_exercise()`**: Guides a simple breathing exercise.
- **`gratitude_list()`**: Encourages creating a gratitude list.
- **`emergency_contact()`**: Prompts users to seek help in a crisis.

---

## Extending the Bot

You can add more features by defining new functions and integrating them into the `check_all_messages()` or `get_response()` functions.

For example, to add a "weather forecast" feature:

1. Define a new function:
   ```python
   def weather_forecast():
       return "I'm not connected to real-time data, but you can check the weather online!"
   ```
2. Update `check_all_messages()`:
   ```python
   response('The weather forecast feature is under development.', ['weather', 'forecast'], required_words=['weather'])
   ```

---

## Contribution

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

