# SayangASD — Demo Prototaip

Flask web app simulating the SayangASD mobile platform for B40 families with autistic children in rural Johor.

## Run

```bash
pip install -r requirements.txt
python app.py
```

Then open **http://localhost:5050**

## Screens

| URL | Role | Scenario |
|-----|------|----------|
| `/` | Caregiver (Siew Hua) | Home dashboard |
| `/therapy` | Caregiver | Log therapy session |
| `/therapy/result` | Caregiver | View session results & trend |
| `/chat` | Caregiver | Async chat with Dr. Arina |
| `/milestone` | CHW (Fadzli) | Milestone assessment form |
| `/aid` | Village Head (Dato' Razak) | Financial aid directory |
| `/referral` | Village Head | Discrete referral to JKM |
| `/offline` | — | Edge case: offline mode |
| `/conflict` | — | Edge case: sync conflict |

## Structure

```
sayangasd/
├── app.py               # Flask routes
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html        # Phone shell + desktop nav
│   ├── home.html
│   ├── therapy.html
│   ├── therapy_result.html
│   ├── chat.html
│   ├── milestone.html
│   ├── milestone_result.html
│   ├── aid.html
│   ├── referral.html
│   ├── referral_confirm.html
│   ├── offline.html
│   └── conflict.html
└── static/
    ├── css/style.css    # All styles
    └── js/app.js        # Try-button & mood interactions
```
