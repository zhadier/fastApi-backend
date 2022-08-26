import os
from typing import Dict
import requests
from dataclasses import dataclass

@dataclass()
class Airtable:
  base_id: str
  api_key: str
  table_name: str

  def get_companies(self):
    headers = {
      "Authorization": f"Bearer {self.api_key}",
      "Content-Type": "application/json"
    }
    endpoint = f'https://api.airtable.com/v0/{self.base_id}/{self.table_name}'
    response = requests.get(endpoint, headers=headers)
    airtable_response = response.json()

    return [d['fields'] for d in airtable_response['records']]
