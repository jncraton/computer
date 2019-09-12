all: test

test:
	python3 -m doctest intents/arithmetic.py
	python3 -m doctest intents/networking.py
	python3 -m doctest intents/handler.py

clean:
	rm -rf __pycache__
	rm -rf intents/__pycache__