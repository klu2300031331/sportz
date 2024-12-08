from django.shortcuts import render

# Predefined responses based on user input related to sports management
def get_response(user_input):
    responses = {
        'hi': "Hi! How can I assist you with sports management today?",
        'hello': "Hi! How can I assist you with sports management today?",
        'what is sports management': "Sports management involves the business and organizational aspects of sports, including managing teams, events, and facilities.",
        'how to manage a sports team': "Managing a sports team involves planning, organizing practices, fostering team spirit, and handling logistics for games and events.",
        'what are the benefits of sports management': "Sports management offers career opportunities in event management, marketing, and team coordination. It also contributes to promoting sports and engaging communities.",
        'how to organize a sports event': "To organize a sports event, plan the logistics, secure a venue, arrange necessary equipment, manage registrations, and promote the event to attract participants and spectators.",
        'what is team coordination in sports': "Team coordination in sports refers to how players and coaches work together to achieve common goals, improving teamwork, communication, and performance.",
        'how to increase fan engagement': "Increase fan engagement by creating interactive content, organizing fan events, and using social media to keep fans updated and involved with the team.",
        'what is sports marketing': "Sports marketing is the promotion of sports teams, events, and related products to increase visibility, attract sponsorships, and engage audiences.",
        'how to analyze player performance': "Analyzing player performance involves tracking statistics, reviewing game footage, and using data analytics to assess strengths and areas for improvement.",
        'what are the roles in sports management': "Roles in sports management include team managers, event coordinators, marketing professionals, and facility managers.",
        'how to manage sports finances': "Managing sports finances includes budgeting, securing sponsorships, controlling expenses, and ensuring profitability for teams, events, or facilities.",
        'how to improve athlete fitness': "Improving athlete fitness involves creating personalized training plans, focusing on strength, conditioning, flexibility, and recovery techniques.",
        'what is sports law': "Sports law involves legal issues related to sports, such as contracts, sponsorships, intellectual property, and liability for injuries.",
        'how to secure sponsorship for a sports event': "To secure sponsorship for a sports event, create attractive sponsorship packages, showcase the event's potential audience, and approach brands that align with the event's audience."
    }

    # Convert the input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Return the response if it exists, otherwise default response
    return responses.get(user_input, "Sorry, I couldn't understand that. Please try again.")


# Chatbot view to handle user input
def chatbot_view(request):
    bot_response = ''
    user_input = ''

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()  # Ensure no leading/trailing spaces
        if user_input:  # If user input is provided
            bot_response = get_response(user_input)
        else:  # If input is empty
            bot_response = "Please type a message."

    return render(request, 'chatbot/chat.html', {'bot_response': bot_response, 'user_input': user_input})
