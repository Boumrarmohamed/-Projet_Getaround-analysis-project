# GetAround Analysis Project

Analyse des delais optimaux entre locations GetAround pour reduire les annulations.

## Resultats cles

- 358 locations affectees par un threshold de 60min (1.98%)
- 270 retards observes (1.5% des locations)  
- 176 problemes evites (63 CONNECT + 113 MOBILE)
- RandomForest R2 = 0.734 pour la prediction de prix

## Utilisation

Dashboard: cd streamlit_dashboard && streamlit run dashboard.py
API: cd api && python app.py

## Recommandation

Implementer un threshold de 60 minutes pour CONNECT et MOBILE.