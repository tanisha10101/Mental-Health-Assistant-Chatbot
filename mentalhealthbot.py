#Mental Health Bot

import random
import re
from datetime import datetime
import webbrowser


from textblob import TextBlob


def get_time():
    """Returns the current time in a friendly format."""
    return datetime.now().strftime("%I:%M %p")

def get_date():
    """Returns the current date in a friendly format."""
    return datetime.now().strftime("%A, %B %d, %Y")

def suggest_activities():
    """Suggests activities based on user mood."""
    activities = [
        "Try journaling your thoughts.",
        "Go for a walk and enjoy nature.",
        "Watch a comedy show or your favorite movie.",
        "Try a new hobby like painting or cooking.",
        "Listen to some relaxing music or a podcast.",
        "Consider doing some light stretches or yoga to relax.",
        "Connect with a friend or loved one for a chat."
    ]
    return random.choice(activities)

def play_music():
    """Suggests relaxing music from YouTube."""
    webbrowser.open("https://www.youtube.com/results?search_query=relaxing+music")
    return "Here's some relaxing music for you!"

def open_resources():
    """Opens a mental health resource website."""
    webbrowser.open("https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health")
    return "I've opened a helpful mental health resource for you."

def set_reminder(task):
    """Sets a reminder for the user."""
    return f"Reminder set for: {task}. I'll make sure you don't forget!"

def analyze_sentiment(user_input):
    """Analyzes the sentiment of user input."""
    analysis = TextBlob(user_input)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

def provide_affirmation():
    """Provides a positive affirmation."""
    affirmations = [
        "You are capable of achieving great things.",
        "Take one step at a time, and you will succeed.",
        "Your feelings are valid, and you deserve happiness.",
        "You are stronger than you think.",
        "Remember to be kind to yourself."
    ]
    return random.choice(affirmations)

def quiz():
    """Offers a quick mental health awareness quiz."""
    questions = {
        "What is one simple way to reduce stress?": ["deep breathing", "exercise", "meditation"],
        "What is a sign of good mental health?": ["emotional resilience", "positive relationships"],
        "What should you do if you feel overwhelmed?": ["seek help", "take a break", "talk to someone"]
    }
    question, answers = random.choice(list(questions.items()))
    return question, answers

def handle_quiz_response(user_input, correct_answers):
    """Handles user responses to the quiz."""
    if user_input.lower() in correct_answers:
        return "That's correct! Great job!"
    else:
        return "That's okay! Remember, it's important to keep learning."

def mental_health_tips():
    """Provides actionable mental health tips."""
    tips = [
        "Practice mindfulness meditation daily.",
        "Stay connected with friends and family.",
        "Set realistic goals and priorities.",
        "Get enough sleep and maintain a consistent routine.",
        "Engage in regular physical activity.",
        "Avoid overexposure to negative news.",
        "Seek professional help if you feel persistently overwhelmed."
    ]
    return random.choice(tips)

def recommend_videos():
    """Suggests motivational videos."""
    webbrowser.open("https://www.youtube.com/results?search_query=motivational+videos")
    return "I've opened a list of motivational videos for you!"

def share_joke():
    """Shares a light-hearted joke."""
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the math book look sad? Because it had too many problems!",
        "Why don't programmers like nature? Too many bugs!",
        "What do you call a fake noodle? An Impasta!"
    ]
    return random.choice(jokes)


unknown_responses = [
    "I'm not sure I understand. Could you clarify?",
    "Hmm, that's interesting. Could you explain more?",
    "I don't quite get that. Maybe try rephrasing?",
    "I'm here to help, but I need a bit more context.",
    "I'm sorry, I didn't catch that. Could you repeat?",
    "Could you please rephrase that?"
]

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    """Calculates the likelihood of a response based on keywords."""
    message_certainty = 0
    has_required_words = True

    # Count matching words
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculate percentage match
    percentage = float(message_certainty) / float(len(recognised_words))

    # Ensure required words are present
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    return int(percentage * 100) if has_required_words or single_response else 0

def check_all_messages(message):
    """Determine the best response based on user input."""
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'greetings'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'are', 'you'])
    response('You\'re welcome!', ['thank', 'thanks', 'thankyou'], single_response=True)
    response('Thank you!', ['i', 'love', 'you'], required_words=['love', 'you'])
    response('Great to hear!', ['fine', 'good', 'doing', 'well'], single_response=True)
    response('I am Mandy-your friendly neighbourly bot! I am here to guide you through this journey', ['who', 'are', 'you'], required_words=['who', 'are', 'you'])
    response('Mental health is a state of mental well-being that enables people to cope with stress. The need for action on mental health is indisputable and urgent.', ['mental', 'health'], required_words=['mental', 'health'])
    response('Don\'t be sad, cheer up. I am here to assist you.', ['sad'], required_words=['sad'])
    response('Practice deep breathing, exercise, prioritize tasks, set boundaries, seek support, and maintain perspective for effective stress management. This can make you feel better.', ['stress'], required_words=['stress'])
    response('Try to deviate your mind into some positive things if you feel this way.', ['family'], required_words=['family'])
    response('I\'m really sorry to hear that you\'re feeling this way, but I can\'t provide the help that you need. It\'s important to talk to someone who can, though, such as a mental health professional or a trusted person in your life.', ['suicide'], required_words=['suicide'])
    response('Yes, a doctor\'s help can be a good option. Please go ahead on our website to book your appointment with our experts.', ['doctor'], required_words=['doctor'])
    response('I know, right? It\'s really important to have a good friend circle who always support and motivate you to achieve your life goals.', ['friends'], required_words=['friends'])
    response('Im here to help! If you\'re comfortable, please share more details or specific concerns so I can provide more targeted assistance. If it\'s a serious or urgent matter, consider reaching out to a mental health professional or someone you trust.', ['help', 'me'], required_words=['help'])
    response('Good to see that you are happy today :)', ['happy'], required_words=['happy'])
    response('You can use the following resources: https://www.youtube.com/watch?v=PTAkiukJK7E.\nYou can also refer to the following videos - https://www.youtube.com/watch?v=CNkiPN_WZfA.', ['resources', 'resource', 'material'], required_words=['resources'])
    response('Why don\'t scientists trust atoms? Because they make up everything!', ['joke'], required_words=['joke'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return random.choice(unknown_responses) if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    """Generates a response based on user input."""
    user_input = user_input.lower()

    # Analyze sentiment
    sentiment = analyze_sentiment(user_input)
    if sentiment == "negative":
        return "I'm here for you. Remember, it's okay to seek support. How can I assist further?"
    elif sentiment == "positive":
        return "I'm glad to hear that! Let's keep the positivity going."

   
    if 'time' in user_input:
        return f"The current time is {get_time()}"
    if 'date' in user_input:
        return f"Today's date is {get_date()}"
    if 'activity' in user_input:
        return f"Here's a suggestion: {suggest_activities()}"
    if 'play music' in user_input:
        return play_music()
    if 'open resource' in user_input or 'resource website' in user_input:
        return open_resources()
    if 'set reminder' in user_input:
        task = user_input.replace('set reminder', '').strip()
        return set_reminder(task) if task else "What would you like to be reminded about?"
    if 'affirmation' in user_input:
        return provide_affirmation()
    if 'quiz' in user_input:
        question, answers = quiz()
        return f"{question} (Possible answers: {', '.join(answers)})"
    if 'tips' in user_input or 'mental health tip' in user_input:
        return f"Here's a tip: {mental_health_tips()}"
    if 'video' in user_input or 'motivational' in user_input:
        return recommend_videos()
    if 'joke' in user_input:
        return share_joke()

    return check_all_messages(user_input.split())
  

  def weather_forecast():
      """Provides a simple weather forecast."""
      return "I'm not connected to real-time data, but you can check the weather online!"
  
  def gratitude_list():
      """Encourages the user to create a gratitude list."""
      return "Why not list three things you're grateful for today? It's a great way to stay positive!"
  
  def breathing_exercise():
      """Guides a simple breathing exercise."""
      return "Take a deep breath in for 4 seconds, hold for 7 seconds, and exhale slowly for 8 seconds. Repeat this 4 times."
  
  def emergency_contact():
      """Encourages the user to contact someone in case of emergency."""
      return "If you're in a crisis, please reach out to a trusted friend, family member, or a local helpline. Remember, you're not alone."


