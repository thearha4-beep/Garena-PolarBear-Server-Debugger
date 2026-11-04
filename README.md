
Garena & PolarBear Server Debugging Toolkit (PK Region)

This diagnostic and traffic interception toolkit is built for auditing and debugging regional authentication flows (specifically for Garena Connect and PolarBear custom game endpoints tailored to the Pakistan region).
The tool includes a standalone Python application bundled via a custom PyInstaller .spec configuration, enabling straightforward CLI testing across both desktop environments and Android setups using Termux.

Core Components & Functional Layout

• app.py & config.json: Serves as the primary entry point providing a interactive CLI interface. It handles setup configuration mapping to identify targeted Unique Identifiers (target_uid), client security details, and server endpoints configured for regional routing (region: PK).
• majorlogin.py: Standardizes token request tests aiming toward OAuth validation endpoints (/oauth/guest/token/grant), spoofing headers specifically for standard mobile platforms.
• majorlogin_pd2.py: Initiates custom JSON payloads targeting secondary backend application APIs (api/v1/login) using dedicated server URL routing configurations.
• mitm_script.py: An automation script engineered for mitmproxy that actively monitors traffic sent through designated domains. It explicitly flags unexpected responses (such as 400, 401, or 405 error statuses) and instantly manipulates them into clean 200 OK success bodies containing mock session tokens. This structure isolates frontend interface behavior away from active or disrupted backend connections during local environment testing.
