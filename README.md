# Anti-Modlishka PoC

Proposed mitigation for MITM proxy phishing techniques such as [Modlishka](https://github.com/drk1wi/Modlishka) or [evilginx2](https://github.com/kgretzky/evilginx2).
Basically, it's doing some obfuscated JavaScript sanity checks in order to detect if the current domain is correct.
It's important to mention that this technique is always bypassable with some effort of the attacker. However, it brings problem to a higher level, so it's no longer possible to setup a MITM phishing proxy using one command.


## Usage

1. Copy `app.env.example` to `app.env`.
2. Set `LEGITIMATE_HOST` to the actual domain you are going to host this application on.
3. Set `SECRET_KEY` to some random value.
4. Run `docker-compose up --build`
5. Setup Modlishka/evilginx2 instance pointing to the original site and check if fraud will be detected.