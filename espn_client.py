from espn_api.football import League
from credentials import login
import math

league = League(league_id=login['league_id'], year=2020)

def parse_local_draft_file():
  draft_file = open('draft.txt', 'r')
  draft_dict = {}
  for line in draft_file:
    player, team = line.strip().rsplit(',')
    draft_dict[player.strip().lower()] = team.strip()

  draft_file.close()
  return draft_dict


__local_draft = parse_local_draft_file()


def get_online_draft():
  draft = league.draft


def get_local_draft_info(player):
  if player in __local_draft:
    draft_position = list(__local_draft).index(player) + 1
    draft_round = 1 if (draft_position < 11) else (math.trunc(draft_position / 10) + 1)
    return {
      "player": player.title(),
      "round": draft_round,
      "position": draft_position
    }

  return "Undrafted"
