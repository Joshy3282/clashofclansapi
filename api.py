import requests


class COCApi:
    def __init__(self, token):
        self.token = token
        self.endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 30

    def get(self, uri, params=None):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        url = self.endpoint + uri

        try:
            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def post(self, uri, data):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        url = self.endpoint + uri

        try:
            response = requests.post(url, json=data, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def clans(self, params):
        return self.get("/clans", params)

    def clans_by_name(self, name, params=None):
        return self.get("/clans", {"name": name}.update(params))

    def clans_by_war_frequency(self, frequency, params=None):
        return self.get("/clans", {"warFrequency": frequency}.update(params))

    def clans_by_location_id(self, locationId, params=None):
        return self.get("/clans", {"locationId": locationId}.update(params))

    def clans_by_min_members(self, minMembers, params=None):
        return self.get("/clans", {"minMembers": minMembers}.update(params))

    def clans_by_max_members(self, maxMembers, params=None):
        return self.get("/clans", {"maxMembers": maxMembers}.update(params))

    def clans_by_min_clan_points(self, minClanPoints, params=None):
        return self.get("/clans", {"minClanPoints": minClanPoints}.update(params))

    def clans_by_min_clan_level(self, minClanLevel, params=None):
        return self.get("/clans", {"minClanLevel": minClanLevel}.update(params))

    def get_clan(self, tag):
        return self.get(f"/clans/%23{tag}")

    def get_clan_capital_raid_seasons(self, tag, params=None):
        return self.get(f"/clans/%23{tag}/capitalraidseasons", params)

    def get_clan_members(self, tag, params=None):
        return self.get(f"/clans/%23{tag}/members", params)

    def get_clan_current_war(self, tag):
        return self.get(f"/clans/%23{tag}/currentwar")

    def get_clan_warlog(self, tag, params=None):
        return self.get(f"/clans/%23{tag}/warlog", params)

    def get_clan_league_war(self, tag):
        return self.get(f"/clanwarleagues/wars/{tag}")

    def get_clan_current_war_league_group(self, tag):
        return self.get(f"/clans/%23{tag}/currentwar/leaguegroup")

    def get_player(self, tag):
        return self.get(f"players/%23{tag}")

    def verify_player_token(self, tag, token):
        return self.post(f"/players/%23{tag}/verifytoken", {"token": token})

    def get_capital_leagues(self, params=None):
        return self.get("f/capitalleagues", params)

    def get_leagues(self, params=None):
        return self.get(f"/leagues", params)

    def get_league_season_rankings(self, leagueId, seasonid, params=None):
        return self.get(f"/leagues/{leagueId}/seasons/{seasonid}", params)

    def get_capital_league(self, leagueId):
        return self.get(f"/capitalleagues/{leagueId}")

    def get_builder_base_league(self, leagueId):
        return self.get(f"/builderbaseleagues/{leagueId}")

    def get_builder_base_leagues(self, params=None):
        return self.get(f"/builderbaseleagues", params)

    def get_league(self, leagueId):
        return self.get(f"/leagues/{leagueId}")

    def get_league_seasons(self, leagueId, params=None):
        return self.get(f"/leagues/{leagueId}/seasons", params)

    def get_war_league_information(self, leagueId):
        return self.get(f"/warleagues/{leagueId}")

    def get_war_leagues(self, params=None):
        return self.get(f"/warleagues", params)

    def get_location_clan_rankings(self, locationId, params=None):
        return self.get(f"/locations/{locationId}/rankings/clans", params)

    def get_location_player_rankings(self, locationId, params=None):
        return self.get(f"/locations/{locationId}/rankings/players", params)

    def get_location_player_builder_base_rankings(self, locationId, params=None):
        return self.get(f"/locations/{locationId}/rankings/players-builder-base", params)

    def get_location_clan_builder_base_rankings(self, locationId, params=None):
        return self.get(f"/locations/{locationId}/rankings/clans-builder-base", params)

    def get_locations(self, params=None):
        return self.get(f"/locations", params)

    def get_locations_capital_rankings(self, locationId, params=None):
        return self.get(f"/locations/{locationId}/rankings/capitals", params)

    def get_location(self, locationId):
        return self.get(f"/locations/{locationId}")

    def get_goldpass_season(self):
        return self.get("/goldpass/seasons/current")

    def get_player_labels(self, params=None):
        return self.get("/labels/players", params)

    def get_clan_labels(self, params=None):
        return self.get('/labels/clans', params)