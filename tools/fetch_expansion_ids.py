import requests
from enum import Enum
import re


def get_one_card(
    exp: Enum = None, lan: str = "fr", card_number: int = 1
) -> requests.models.Response:
    url = "https://admin.starwarsunlimited.com/api/card-list"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip",
        "Origin": "https://starwarsunlimited.com",
        "Referer": "https://starwarsunlimited.com/",
    }

    # One param per line
    params = [
        ("locale", lan),
        ("orderBy[expansion][id]", "asc"),
        ("sort[0]", "type.sortValue:asc,expansion.sortValue:desc,cardNumber:asc"),
        ("filters[$and][0][variantOf][id][$null]", "true"),
        ("filters[$and][1][cardNumber][$eq]", card_number),
    ]
    if exp is not None:
        params.append(("filters[$and][2][expansion][id][$eq]", exp.value))

    resp = requests.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()  # raises if HTTP status is 4xx/5xx
    return resp


def fetch_expansion_ID() -> list:
    def iter_objects(o):
        # Génère tous les dicts rencontrés dans l'arbre JSON
        if isinstance(o, dict):
            yield o
            for v in o.values():
                yield from iter_objects(v)
        elif isinstance(o, list):
            for v in o:
                yield from iter_objects(v)

    result = []
    for lan in ["en", "fr", "de", "es", "it"]:
        resp = get_one_card(None, lan, 1)

        result += [
            f"{obj['expansion']['data']['attributes']['code']}_{lan.upper()} = {obj['expansion']['data']['id']}"
            for obj in iter_objects(resp.json())
            if isinstance(obj, dict)
            and "expansion" in obj
            and isinstance(obj["expansion"].get("data"), dict)
            and isinstance(obj["expansion"]["data"].get("attributes"), dict)
            and "code" in obj["expansion"]["data"]["attributes"]
            and "id" in obj["expansion"]["data"]
        ]
    return result


def sort_and_display_expansion_ID(lst: list) -> None:
    def key_num(s: str) -> int:
        # extrait le nombre après "=" (tolère espaces)
        m = re.search(r"=\s*(\d+)\s*$", s)
        return int(m.group(1)) if m else float("inf")

    unique_sorted = sorted(set(lst), key=key_num)
    print("\n".join(unique_sorted))


lst = fetch_expansion_ID()
sort_and_display_expansion_ID(lst)
