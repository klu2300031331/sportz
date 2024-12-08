from django.http import JsonResponse
from django.shortcuts import render
import random

# Realistic teams and players
teams = ['India', 'Australia', 'England', 'South Africa', 'New Zealand', 'Pakistan', 'Sri Lanka', 'Bangladesh']
players = ['PV Sindhu', 'Saina Nehwal', 'Carolina Marin', 'Kento Momota', 'Lee Chong Wei', 'Roger Federer', 'Rafael Nadal', 'Novak Djokovic']

# Simulate increasing scores over time
def live_scores(request):
    # Initialize session scores
    if 'scores' not in request.session:
        request.session['scores'] = {
            'football': {'A': random.randint(0, 1), 'B': random.randint(0, 1)},
            'badminton': {'A': random.randint(0, 15), 'B': random.randint(0, 15)},
            'volleyball': {'A': random.randint(0, 10), 'B': random.randint(0, 10)},
            'kho_kho': {'A': random.randint(0, 5), 'B': random.randint(0, 5)},
            'tennis': {'A': random.randint(0, 3), 'B': random.randint(0, 3)}
        }
        request.session['names'] = {
            'football': random.sample(teams, 2),
            'badminton': random.sample(players, 2),
            'volleyball': random.sample(teams, 2),
            'kho_kho': random.sample(teams, 2),
            'tennis': random.sample(players, 2)
        }

    # Randomly increment one score per match
    for event in request.session['scores']:
        team_to_update = random.choice(['A', 'B'])
        increment = random.randint(0, 2 if event == 'badminton' else 1)
        request.session['scores'][event][team_to_update] += increment

    # Check for AJAX request using 'X-Requested-With' header
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        scores = {
            event: {
                'name_A': request.session['names'][event][0],
                'name_B': request.session['names'][event][1],
                'score': f"{request.session['scores'][event]['A']} - {request.session['scores'][event]['B']}"
            }
            for event in request.session['scores']
        }
        return JsonResponse(scores)

    # Prepare context for the initial page load
    context = {
        event: {
            'name_A': request.session['names'][event][0],
            'name_B': request.session['names'][event][1],
            'score': f"{request.session['scores'][event]['A']} - {request.session['scores'][event]['B']}"
        }
        for event in request.session['scores']
    }

    return render(request, 'live_score.html', context)
