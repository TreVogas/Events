# Heroku Deployment

1. Create app
```sh
heroku create vovaevents111
```
2. Deploy to remote instance
```sh
git push heroku master
```
3. To run on the instance:
```sh
heroku run bash
python Events.py
```
4. To run remotely:
```sh
heroku run python Events.py
```
5. To schedule: [Point 6 from this](sitehttps://medium.com/analytics-vidhya/schedule-a-python-script-on-heroku-a978b2f91ca8)


