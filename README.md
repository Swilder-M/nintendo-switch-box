<p align="center">
  <a href="https://gist.github.com/Swilder-M/4aa566c004d4baac8561a36ae02bc2ea"><img width="400" src="https://raw.githubusercontent.com/Swilder-M/nintendo-switch-box/master/assets/pinned.png"></a>
  <h3 align="center">🎮 nintendo-switch-box</h3>
  <p align="center">Update a pinned gist to contain your Nintendo Switch Game stats</p>
</p>

## Setup
1. Fork [this repository](https://github.com/Swilder-M/nintendo-switch-box).

2. Create a new **public** GitHub Gist at <https://gist.github.com/>.

3. Go to the <https://github.com/settings/tokens/new> page to create a token, just grant the **gist** permission.

4. Run `python src/get_session.py` to get session token.

5. Go to the repository **Settings > Secrets**, Add the following environment variables:
   - NINTENDO_SESSION_TOKEN: The session token you got from the previous step.
   - GH_TOKEN: The token you created in the previous step.
   - GIST_ID: The ID portion from your gist URL: `https://gist.github.com/your_name/<GIST_ID>`.
