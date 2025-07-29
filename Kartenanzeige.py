import requests
import tkinter as tk
from tkinter import messagebox, ttk
import math
# Globale Variablen
card_details_dict = {}
entry = None
main_frame = None
# Edition-Namen
EDITION_NAMES = {
    0: "Alpha", 1: "Beta", 2: "Promo", 3: "Chaos Reward", 4: "Untamed", 5: "Dice",
    6: "Gladius", 7: "Chaos Legion", 8: "Riftwatchers", 10: "Chaos Soulbound",
    12: "Rebellion", 13: "Rebellion Soulbound", 14: "Conclave", 15: "Foundation"
}
RARITY_COLORS = {1: "#d0d0d0", 2: "#87ceeb", 3: "#dda0dd", 4: "#ffd700"}
RARITY_NAMES = {1: "C", 2: "R", 3: "E", 4: "L"}  # Common, Rare, Epic, Legendary
LEVEL_ONLY_CARDS = {
    "Archmage Arius", "Armorsmith", "Corrupted Pegasus", "Delwyn Dragonscale", "Dragonling Bowman",
    "Dwarven Wizard", "Dragon Whelp", "Electric Eels", "Enchanted Defender", "Fiendish Harpy", "Goblin Chef",
    "Lord of Fire", "Mermaid Healer", "Minotaur Warlord", "Molten Ogre", "Prince Julian",
    "Red Dragon", "Silvershield Bard", "Shin-Lo", "Undead Archer",
    "Beetle Queen", "Battle Orca", "Boogeyman", "Baby Unicorn", "Brownie", "Black Dragon",
    "Creeping Ooze", "Crystal Werewolf", "Daria Dragonscale", "Divine Sorceress", "Ettin Spearman",
    "Exploding Dwarf", "Furious Chicken", "Fallen Specter", "Fire Spitter", "Flame Imp",
    "Gelatinous Cube", "Goblin Mech", "Gremlin Blaster", "Hobgoblin", "Highland Archer",
    "Imp Bowman", "Javelin Thrower", "Kobold Miner", "Lord Arianthus", "Manticore",
    "Mushroom Seer", "Naga Fire Wizard", "Naga Windmaster", "Octopider", "Pirate Archer",
    "Phantom Soldier", "Prismatic Energy", "Rusty Android", "Ruler of the Seas",
    "Serpentine Mystic", "Sea Genie", "Screeching Vulture", "Sacred Unicorn", "Sea Monster",
    "Silvershield Assassin", "Silvershield Archers", "Skeletal Warrior", "Spirit Shaman",
    "Spirit Miner", "The Kraken", "Undead Minotaur", "Vampire", "Wood Nymph", "Zalran Efreet",
    "Mighty Dricken", "Halfling Alchemist", "Chain Golem"
}
BETA_REWARD_CARDS = {
    "Baby Unicorn", "Battle Orca", "Beetle Queen", "Black Dragon", "Boogeyman", "Brownie",
    "Creeping Ooze", "Crystal Werewolf", "Daria Dragonscale", "Divine Sorceress", "Ettin Spearman",
    "Exploding Dwarf", "Fallen Specter", "Fire Spitter", "Flame Imp", "Furious Chicken",
    "Gelatinous Cube", "Goblin Mech", "Gremlin Blaster", "Highland Archer", "Hobgoblin",
    "Imp Bowman", "Javelin Thrower", "Korjack", "Lord Arianthus", "Manticore", "Mushroom Seer",
    "Naga Fire Wizard", "Naga Windmaster", "Octopider", "Phantom Soldier", "Pirate Archer",
    "Prismatic Energy", "Ruler of the Seas", "Rusty Android", "Sacred Unicorn", "Screeching Vulture",
    "Sea Genie", "Sea Monster", "Serpentine Mystic", "Silvershield Archers", "Silvershield Assassin",
    "Skeleton Warrior", "Skeletal Warrior", "Spirit Miner", "Spirit Shaman", "The Kraken",
    "Undead Minotaur", "Vampire", "Wood Nymph", "Zalran Efreet"
}
ALPHA_PROMO_CARDS = {"Dragon Whelp", "Neb Seni", "Royal Dragon Archer", "Shin-Lo"}
BETA_PROMO_CARDS = {
    "Archmage Arius", "Armorsmith", "Corrupted Pegasus", "Delwyn Dragonscale", "Dragon Whelp",
    "Dragonling Bowman", "Dwarven Wizard", "Electric Eels", "Enchanted Defender", "Fiendish Harpy",
    "Goblin Chef", "Lord of Fire", "Mermaid Healer", "Minotaur Warlord", "Molten Ogre",
    "Prince Julian", "Red Dragon", "Shin-Lo", "Silvershield Bard", "Undead Archer"
}
UNTAMED_PROMO_CARDS = {"Chain Golem", "Halfling Alchemist", "Mighty Dricken"}
CHAOS_PROMO_CARDS = {
    "Arkemis the Bear", "Doctor Blight", "Lux Vega", "Oshuur Constantia", "Runi",
    "Vruz", "Waka Spiritblade", "Zyriel"
}
REBELLION_PROMO_CARDS = {
    "Baron Fyatt", "Delya", "Elanor Bravefoot", "Fizbo the Fabulous", "Grimbardun Smith",
    "Henchling Enforcer", "Heloise the Hollow", "Kelan Gaines", "Mana Warden", "Mantaroth",
    "Meriput Mossmender", "Nephket", "Night Stalker", "Riklauniman", "Rune Arcanist",
    "Sanctus Vicar", "Ulfga the Blighted", "Warborn Shaman"
}
CONCLAVE_PROMO_CARDS = {"Arcane Skinwalker", "Archmage Yabanius", "Gramel the Hunger", "Tasoshi Drakamoto",
                        "Yaba's Pickle"}
UNTAMED_REWARD_CARDS = {
    "Almo Cambio", "Ancient Lich", "Ant Miners", "Axemaster", "Barking Spider", "Bila The Radiant",
    "Bila the Radiant", "Captain's Ghost", "Centaur Mage", "Centauri Mage", "Chain Spinner",
    "Charlok Minotaur", "Dark Ferryman", "Demented Shark", "Efreet Elder", "Evangelist",
    "Fineas Rage", "Flame Monkey", "Gloridax Soldier", "Grim Reaper", "Harvester",
    "Kelp Initiate", "Kretch Tallevor", "Nectar Queen", "Nightmare", "Onyx Sentinel",
    "Phantasm", "Pyromancer", "Robo-Dragon Knight", "Sand Worm", "Shadowy Presence",
    "Silvershield Sheriff", "Spirit Druid Grog", "Temple Priest", "Torhilo the Frozen",
    "Tortis The Frozen", "Undead Rexx", "Warrior Of Peace", "Warrior of Peace", "Wave Runner"
}
IGNORE_BCX_EDITIONS = {"Alpha", "Beta", "Alpha Promo", "Beta Reward", "Beta Promo", "Untamed Promo", "Foundation"}
def get_max_bcx(rarity, gold):
    return {1: 38, 2: 22, 3: 10, 4: 4} if gold else {1: 400, 2: 115, 3: 46, 4: 11}
def get_progress_color(percentage):
    if percentage < 30:
        return "#ffeeee"
    elif percentage < 70:
        return "#fff4e0"
    elif percentage < 100:
        return "#eaffea"
    else:
        return "#ccffcc"
def load_card_details():
    global card_details_dict
    try:
        resp = requests.get("https://api2.splinterlands.com/cards/get_details", timeout=10)
        for card in resp.json():
            cid = int(card["id"])
            name = card.get("name", "Unbekannt")
            ed = card.get("edition", card.get("editions", 0))
            rarity = int(card.get("rarity", 1))
            if isinstance(ed, list):
                ed = ed[0]
            elif isinstance(ed, str) and ',' in ed:
                ed = int(ed.split(',')[0])
            else:
                ed = int(ed)
            card_details_dict[cid] = {"name": name, "edition": ed, "rarity": rarity}
    except Exception as e:
        messagebox.showerror("Fehler", f"Kartendetails konnten nicht geladen werden: {e}")
def classify_card_edition(name, original_edition):
    edition = EDITION_NAMES.get(original_edition, f"Edition {original_edition}")
    if original_edition == 2 or original_edition == 3:
        if name in BETA_REWARD_CARDS:
            return "Beta Reward"
        elif name in UNTAMED_REWARD_CARDS:
            return "Untamed Reward"
        elif name in ALPHA_PROMO_CARDS:
            return "Alpha Promo"
        elif name in BETA_PROMO_CARDS:
            return "Beta Promo"
        elif name in UNTAMED_PROMO_CARDS:
            return "Untamed Promo"
        elif name in CHAOS_PROMO_CARDS:
            return "Chaos Promo"
        elif name in REBELLION_PROMO_CARDS:
            return "Rebellion Promo"
        elif name in CONCLAVE_PROMO_CARDS:
            return "Conclave Promo"
    return edition
def process_cards_data(cards):
    card_bcx_totals = {}
    for c in cards:
        cid = int(c["card_detail_id"])
        lvl = int(c.get("level", 1))
        bcx = int(c.get("xp", 0))
        gold = int(c.get("gold", 0))
        key = (cid, gold)
        if key not in card_bcx_totals:
            card_bcx_totals[key] = {"total_bcx": 0, "highest_level": 0, "gold": gold}
        card_bcx_totals[key]["total_bcx"] += bcx
        if lvl > card_bcx_totals[key]["highest_level"]:
            card_bcx_totals[key]["highest_level"] = lvl
    final_cards = {}
    for (cid, gold), data in card_bcx_totals.items():
        if cid not in final_cards or data["highest_level"] > final_cards[cid]["level"]:
            final_cards[cid] = {"level": data["highest_level"], "bcx": data["total_bcx"], "gold": gold}
    return final_cards
def create_combined_columns(parent, owned_cards, missing_cards, bg_color, max_cards_per_column=27):
    """Erstellt kombinierte Spalten mit besitzenden und fehlenden Karten"""
    all_cards = []
    # Füge besitzende Karten hinzu
    for label_text, rarity, is_max in sorted(owned_cards, key=lambda x: x[1]):
        all_cards.append(("owned", label_text, rarity, is_max))
    # Füge fehlende Karten hinzu (mit Rarität)
    for name, rarity in sorted(missing_cards, key=lambda x: x[1]):
        all_cards.append(("missing", name, rarity, None))
    if not all_cards:
        return
    num_columns = math.ceil(len(all_cards) / max_cards_per_column)
    for col in range(num_columns):
        start_idx = col * max_cards_per_column
        end_idx = min((col + 1) * max_cards_per_column, len(all_cards))
        column_cards = all_cards[start_idx:end_idx]
        column_frame = tk.Frame(parent, bg=bg_color)
        column_frame.grid(row=0, column=col, sticky="nw", padx=2)
        for card_type, label_text, rarity, is_max in column_cards:
            if card_type == "owned":
                card_bg = RARITY_COLORS.get(rarity, "#ffffff")
                font_style = ("Arial", 9, "bold" if is_max else "normal")
                card_label = tk.Label(column_frame, text=label_text, bg=card_bg, font=font_style,
                                      relief="solid", bd=0.5, anchor="w", wraplength=260)
                card_label.pack(fill="x", pady=1)
            else:  # missing
                rarity_text = RARITY_NAMES.get(rarity, "?")
                missing_text = f"{label_text} ({rarity_text})"
                missing_card = tk.Label(column_frame, text=missing_text, bg="#ffcccc", anchor="w",
                                        font=("Arial", 9), wraplength=200)
                missing_card.pack(fill="x", pady=1)
def create_edition_frame(parent, edition_name, owned_cards, missing_cards, stats):
    total_owned = stats.get("owned", 0)
    total_maxed = stats.get("maxed", 0)
    total_missing_bcx = stats.get("missing_bcx", 0)
    total_cards = total_owned + len(missing_cards)
    owned_pct = (total_owned / total_cards * 100) if total_cards > 0 else 0
    maxed_pct = (total_maxed / total_cards * 100) if total_cards > 0 else 0
    bg_color = get_progress_color(owned_pct)
    if total_cards > 0 and total_maxed == total_cards:
        bg_color = "#88cc88"
    frame = tk.Frame(parent, bg=bg_color, relief="raised", bd=1, padx=5, pady=5)
    # Header
    header = tk.Label(frame, text=edition_name, font=("Arial", 11, "bold"), bg="#d9edf7")
    header.pack(fill="x", pady=(0, 5))
    # Statistiken
    show_bcx = edition_name not in IGNORE_BCX_EDITIONS
    stats_text = ""
    # Für Total-Spalte: Verwende die korrekte Gesamtanzahl
    if "Total" in edition_name:
        total_missing_display = stats.get("total_missing_count", len(missing_cards))
        total_cards = total_owned + total_missing_display  # Korrekte Gesamtanzahl
        owned_pct = (total_owned / total_cards * 100) if total_cards > 0 else 0
        maxed_pct = (total_maxed / total_cards * 100) if total_cards > 0 else 0
        if show_bcx and total_missing_bcx > 0:
            stats_text += f"Total Missing BCX: {total_missing_bcx}\n"
        stats_text += f"Total Maxed Cards: {total_maxed} ({maxed_pct:.1f}%)\n"
        stats_text += f"Total Owned Cards: {total_owned} ({owned_pct:.1f}%)\n"
        stats_text += f"Total Missing Cards: {total_missing_display}"
    else:
        if show_bcx and total_missing_bcx > 0:
            stats_text += f"Missing BCX: {total_missing_bcx}\n"
        stats_text += f"Maxed out Cards: {total_maxed} ({maxed_pct:.1f}%)\n"
        stats_text += f"Owned Cards: {total_owned} ({owned_pct:.1f}%)\n"
        stats_text += f"Missing Cards: {len(missing_cards)}"
    stats_label = tk.Label(frame, text=stats_text, font=("Arial", 8), justify="left", bg=bg_color, fg="#333")
    stats_label.pack(fill="x", pady=(0, 5))
    # Fortschrittsbalken
    if total_cards > 0:
        progress = ttk.Progressbar(frame, length=200, mode='determinate')
        progress['value'] = owned_pct
        progress.pack(fill="x", pady=(0, 5))
    # Kombinierte Karten in Spalten (besitzende + fehlende)
    # Nur anzeigen wenn Karten vorhanden sind (für Total-Spalte werden leere Listen übergeben)
    if owned_cards or missing_cards:
        cards_frame = tk.Frame(frame, bg=bg_color)
        cards_frame.pack(fill="x", pady=2)
        create_combined_columns(cards_frame, owned_cards, missing_cards, bg_color)
    else:
        # Für die Total-Spalte: Nur ein kleiner Hinweis, dass keine Kartenliste angezeigt wird
        if "Total" in edition_name:
            hint_label = tk.Label(frame, text="(Summary only - no card list)",
                                  font=("Arial", 7, "italic"), bg=bg_color, fg="#666")
            hint_label.pack(pady=2)
    return frame
def fetch_cards():
    global entry, main_frame
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Fehler", "Bitte gib einen Benutzernamen ein.")
        return
    # Clear and show loading
    for widget in main_frame.winfo_children():
        widget.destroy()
    loading = tk.Label(main_frame, text="⏳ Lade Kartendaten...", font=("Arial", 12))
    loading.pack(expand=True)
    main_frame.update()
    try:
        resp = requests.get(f"https://api2.splinterlands.com/cards/collection/{username}", timeout=15)
        cards = resp.json().get("cards", [])
        if not cards:
            loading.config(text="❌ Keine Karten gefunden.")
            return
        final_cards = process_cards_data(cards)
        edition_groups = {}
        missing_cards_by_edition = {}
        stats_by_edition = {}
        # Process all cards
        for cid, details in card_details_dict.items():
            ed = details["edition"]
            if ed == 9 or ed == 11: continue
            name, rarity = details["name"], details["rarity"]
            edition = classify_card_edition(name, ed)
            if cid in final_cards:
                info = final_cards[cid]
                level, bcx, gold = info["level"], info["bcx"], info["gold"]
                foil_icon = "✨" if gold else ""
                if edition in ["Alpha", "Beta"] or name in LEVEL_ONLY_CARDS:
                    label_text = f"{foil_icon}{name} - Level {level}"
                    is_max = False
                else:
                    max_bcx = get_max_bcx(rarity, gold).get(rarity, 0)
                    is_max = bcx >= max_bcx
                    max_icon = " ⭐" if is_max else ""
                    label_text = f"{foil_icon}{name} - Level {level} (BCX {bcx}){max_icon}"
                stats_by_edition.setdefault(edition, {"missing_bcx": 0, "maxed": 0, "owned": 0})
                if not (edition in IGNORE_BCX_EDITIONS):
                    stats_by_edition[edition]["missing_bcx"] += 0 if is_max else max_bcx - bcx
                    if is_max: stats_by_edition[edition]["maxed"] += 1
                stats_by_edition[edition]["owned"] += 1
                edition_groups.setdefault(edition, []).append((label_text, rarity, is_max))
            else:
                # Fehlende Karte - BCX zur Statistik hinzufügen
                missing_cards_by_edition.setdefault(edition, []).append((name, rarity))
                stats_by_edition.setdefault(edition, {"missing_bcx": 0, "maxed": 0, "owned": 0})
                # BCX für fehlende Karten hinzufügen (nur wenn BCX relevant ist)
                if not (edition in IGNORE_BCX_EDITIONS):
                    # Normale Karten: max BCX für Regular (nicht Gold)
                    max_bcx = get_max_bcx(rarity, False).get(rarity, 0)
                    stats_by_edition[edition]["missing_bcx"] += max_bcx
        # Clear loading
        loading.destroy()
        # Create scrollable area
        canvas = tk.Canvas(main_frame, bg="#ffffff")
        v_scroll = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        h_scroll = tk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
        scrollable_frame = tk.Frame(canvas, bg="#ffffff")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        # Edition ordering
        custom_order = [
            ("Alpha", "Beta"), "Alpha Promo", "Beta Promo", "Beta Reward", "Untamed Promo",
            "Untamed", "Untamed Reward", "Dice", "Chaos Legion", "Chaos Promo", "Chaos Reward",
            "Chaos Soulbound", "Riftwatchers", "Rebellion", "Rebellion Promo", "Rebellion Soulbound",
            "Conclave", "Conclave Promo", "Gladius", "Foundation"
        ]
        all_editions = set(edition_groups) | set(missing_cards_by_edition)
        used = set()
        ordered_groups = []
        # Erste durchlauf: Alle normalen Editionen
        for entry in custom_order:
            if isinstance(entry, tuple):
                group_keys = [k for k in entry if k in all_editions]
                if group_keys:
                    ordered_groups.append((("/".join(entry), group_keys)))
                    used.update(group_keys)
            elif entry in all_editions:
                ordered_groups.append(((entry, [entry])))
                used.add(entry)
        # Alle verbleibenden Editionen (nicht in custom_order)
        for ed in sorted(all_editions - used):
            ordered_groups.append(((ed, [ed])))
        # Create edition frames (normale Editionen)
        col = 0
        for display_name, keys in ordered_groups:
            all_owned_cards = []
            all_missing_cards = []
            for k in keys:
                all_owned_cards.extend(edition_groups.get(k, []))
                all_missing_cards.extend(missing_cards_by_edition.get(k, []))
            total_missing_bcx = sum(stats_by_edition.get(k, {}).get("missing_bcx", 0) for k in keys)
            total_maxed = sum(stats_by_edition.get(k, {}).get("maxed", 0) for k in keys)
            total_owned = sum(stats_by_edition.get(k, {}).get("owned", 0) for k in keys)
            stats = {"missing_bcx": total_missing_bcx, "maxed": total_maxed, "owned": total_owned}
            frame = create_edition_frame(scrollable_frame, display_name, all_owned_cards, all_missing_cards, stats)
            frame.grid(row=0, column=col, sticky="n", padx=2, pady=2)
            col += 1
        # AM ENDE: Total-Spalte erstellen
        display_name_total = "Total (All Editions)"
        # Berechne Gesamtstatistiken über alle Editionen
        total_missing_bcx_all = sum(stats_by_edition[edition_key].get("missing_bcx", 0)
                                    for edition_key in stats_by_edition)
        total_maxed_all = sum(stats_by_edition[edition_key].get("maxed", 0)
                              for edition_key in stats_by_edition)
        total_owned_all = sum(stats_by_edition[edition_key].get("owned", 0)
                              for edition_key in stats_by_edition)
        # Zähle alle fehlenden Karten
        total_missing_count_all = sum(len(missing_cards_by_edition.get(edition_key, []))
                                      for edition_key in missing_cards_by_edition)
        stats_total = {
            "missing_bcx": total_missing_bcx_all,
            "maxed": total_maxed_all,
            "owned": total_owned_all,
            "total_missing_count": total_missing_count_all
        }
        # Total-Spalte OHNE Kartenliste (leere Listen übergeben) - als letztes
        frame_total = create_edition_frame(scrollable_frame, display_name_total,
                                           [], [], stats_total)  # Leere Kartenlisten!
        frame_total.grid(row=0, column=col, sticky="n", padx=2, pady=2)
        # Pack scrollbars and canvas
        h_scroll.pack(side="bottom", fill="x")
        v_scroll.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        # Mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    except Exception as e:
        loading.config(text=f"❌ Fehler: {str(e)}")
# GUI Setup
root = tk.Tk()
root.title("? Splinterlands Kartensammlung")
root.geometry("1600x900")
root.configure(bg="#f7f7f7")
# Header
header_frame = tk.Frame(root, bg="#1976d2", height=60)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)
tk.Label(header_frame, text="Splinterlands Kartensammlung", font=("Arial", 14, "bold"),
         bg="#1976d2", fg="white").pack(expand=True)
# Input area
input_frame = tk.Frame(root, bg="#f7f7f7")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Benutzername:", bg="#f7f7f7", font=("Arial", 10)).grid(row=0, column=0, padx=5)
entry = tk.Entry(input_frame, font=("Arial", 10))
entry.grid(row=0, column=1, padx=5)
entry.bind('<Return>', lambda e: fetch_cards())
tk.Button(input_frame, text="Karten abrufen", command=fetch_cards, font=("Arial", 9, "bold"),
          bg="#4caf50", fg="white").grid(row=0, column=2, padx=5)
# Main area
main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)
load_card_details()
root.mainloop()
