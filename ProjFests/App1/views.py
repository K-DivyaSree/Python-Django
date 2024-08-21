from django.shortcuts import render
from datetime import datetime
# Create your views here.

FESTIVALS = {
    'AndhraPradesh': {
        'f1': 'Happy Ugadi! 🌸 May this Telugu New Year bring joy and prosperity!',
        'f2': 'Happy Tirupati Brahmotsavam! 🌺 Celebrate the grand festival of Lord Venkateswara!',
        'f3': 'Happy Rottela Panduga! 🍞 A unique festival celebrated at the Bara Shaheed Dargah!',
    },
    'Karnataka': {
        'f1': 'Happy Dasara! 🐘 Celebrate the victory of good over evil in Mysuru!',
        'f2': 'Happy Varamahalakshmi Vrata! 🌸 Worship the goddess of wealth and prosperity!',
        'f3': 'Happy Eid-ul-Fitr! 🕌 Celebrate the end of Ramadan with joy and blessings!',
    },
    'TamilNadu': {
        'f1': 'Happy Pongal! 🌾 May your harvest be abundant and your home filled with joy!',
        'f2': 'Happy Mahamagam! 🕉️ A sacred festival celebrated once in 12 years in Kumbakonam!',
        'f3': 'Happy Christmas! 🎄 Celebrate the birth of Jesus Christ with love and joy!',
    },
    'Maharashtra': {
        'f1': 'Happy Ganesh Chaturthi! 🐘 May Lord Ganesha remove all obstacles in your path!',
        'f2': 'Happy Mount Mary Fair! 🌹 A Christian pilgrimage in Bandra, Mumbai!',
        'f3': 'Happy Eid-e-Milad! 🌙 Celebrate the birth of Prophet Muhammad with peace and prayers!',
    },
    'Gujarat': {
        'f1': 'Happy Navratri! 🕺 Dance to the beats of Garba during these nine nights!',
        'f2': 'Happy Shamlaji Fair! 🎉 A grand festival celebrated at the Shamlaji Temple!',
        'f3': 'Happy Paryushan Parva! 🕉️ Jain festival of fasting and forgiveness!',
    },
    'WestBengal': {
        'f1': 'Happy Durga Puja! 🕉️ Celebrate the triumph of good over evil in Kolkata!',
        'f2': 'Happy Dol Jatra! 🟣 A colorful festival similar to Holi but unique to Bengal!',
        'f3': 'Happy Eid-ul-Adha! 🕌 Celebrate the festival of sacrifice with devotion!',
    },
    'Punjab': {
        'f1': 'Happy Baisakhi! 🌾 Celebrate the harvest festival and the formation of Khalsa!',
        'f2': 'Happy Gurpurab! 🕯️ Celebrate the birth of Guru Nanak with devotion!',
        'f3': 'Happy Hola Mohalla! 🏇 Witness the martial arts and religious processions of Sikhs!',
    },
    'Kerala': {
        'f1': 'Happy Onam! 🌸 Celebrate the homecoming of King Mahabali with grand feasts!',
        'f2': 'Happy Vishu! 🌾 May the new year bring prosperity and happiness!',
        'f3': 'Happy Eid-ul-Fitr! 🌙 Celebrate the end of Ramadan with prayers and joy!',
    },
    'Rajasthan': {
        'f1': 'Happy Teej! 🌸 Celebrate the monsoon festival with songs and swings!',
        'f2': 'Happy Pushkar Fair! 🐪 Experience the largest camel fair in India!',
        'f3': 'Happy Christmas! 🎄 Celebrate the birth of Christ in the royal palaces of Rajasthan!',
    },
    'UttarPradesh': {
        'f1': 'Happy Ram Navami! 🏹 Celebrate the birth of Lord Rama with devotion!',
        'f2': 'Happy Buddh Purnima! 🌸 Celebrate the birth of Lord Buddha in Sarnath!',
        'f3': 'Happy Muharram! 🕌 Commemorate the martyrdom of Imam Hussain with reverence!',
    },
}

def festival_wishes(request, state, festival):
    state_festivals = FESTIVALS.get(state)
    wish = state_festivals.get(festival) if state_festivals else ""
    current_time = datetime.now().strftime("%H:%M %p")
    context = {
        'wish': wish,
        'time': current_time,
        'state': state,
        'festival': festival,
    }
    return render(request, '../templates/index.html', context)