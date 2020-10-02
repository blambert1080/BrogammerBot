from espn_api.football import League
from credentials import login

league = League(league_id=login['league_id'], year=2020)

def get_draft():
  draft = league.draft
