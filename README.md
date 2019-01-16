# Anti-Modlishka

Proposed mitigation for MITM proxy phishing techniques such as Modlishka.


## How does it work?

Some client-side magic to detect if the client is on legitimate domain.


## Usage

1. Copy `app.env.example` to `app.env`.
2. Set `LEGITIMATE_HOST` to the actual domain you are going to host this application on.
3. Set `SECRET_KEY` to some random value.
4. Run `docker-compose up --build`
