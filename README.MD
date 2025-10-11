# Hybrid Image Platform — README

## Overview

This repository documents the **Hybrid Image Platform**, (HIP) a two-phase research and development initiative based on the paper *Hybrid Image of Multiple Fantastical Characters* (Juhapekka Ollikainen, 2022, International Conference on Computational Creativity, Paris).

The project combines artistic research and technical prototyping to explore new ways of generating hybrid story characters from open public-domain materials. It bridges cultural archives and computational creativity, producing:

1. An **Open Data API** for story and character data.
2. A **Blender Add-on** for 3D visualization and prototyping.

HIP follws A Java MVC framework is a software framework  Model-View-Controller design pattern, where the Model (Open Data API)), the View (Blender Add-on), and the Controller (StoryChar Importer). 

---

## 🧩 Phase 1 — Open Data API

### Base URL
```
https://api.hybridimage.org/v1/
```

### Endpoints

#### `GET /characters/random`
Returns a randomly generated hybrid character.

**Example Response:**
```json
{
  "id": "suomuhauki_001",
  "name": "Suomuhauki – The Scale Pike",
  "description": "A mythic hero merging human intellect and fish spirit strength.",
  "origin": "Kalevala",
  "traits": ["bravery", "transformation", "elemental-water"],
  "model_url": "https://api.hybridimage.org/assets/suomuhauki.blend"
}
```

#### `GET /characters/{id}`
Fetch a specific character by ID.

**Example Response:**
```json
{
  "id": "lynx_oracle_002",
  "name": "Lynx Oracle",
  "description": "A seer whose hybrid essence merges feline stealth and human intuition.",
  "tags": ["prophecy", "animal-spirit", "wisdom"],
  "3d_model": "https://api.hybridimage.org/assets/lynx_oracle.glb"
}
```

#### `POST /characters/generate`
Generate a new hybrid character using user-defined parameters.

**Example Request:**
```json
{
  "base_sources": ["Kalevala", "Norse mythology"],
  "elements": ["human", "spirit", "animal"],
  "style": "heroic",
  "random_seed": 42
}
```

---

## 🧠 Data Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique character identifier |
| `name` | string | Generated hybrid character name |
| `description` | string | Narrative metadata |
| `origin` | string | Source mythos or archive |
| `traits` | array | Narrative or symbolic traits |
| `model_url` | string | Link to `.blend` or `.glb` 3D model |

---

## 🧪 Example Usage

### Fetch a Random Character (Python)
```python
import requests
r = requests.get("https://api.hybridimage.org/v1/characters/random")
data = r.json()
print(data["name"], "-", data["description"])
```

### Blender Integration Example
```python
import bpy, requests
response = requests.get("https://api.hybridimage.org/v1/characters/random")
char = response.json()

bpy.ops.mesh.primitive_uv_sphere_add()
obj = bpy.context.active_object
obj.name = char["name"]
obj["description"] = char["description"]
```

---

## 🎨 Phase 2 — Blender Add-on: *StoryChar Importer*

The **StoryChar Importer** connects Blender to the Hybrid Image API and can operate in both online and offline demo modes.

### Features
- Fetch and import hybrid characters via API
- Offline sample mode for demonstrations
- Adds metadata fields (`name`, `description`) to Blender objects
- Extensible for character rigging or texture fusion

### Installation
1. Save `storychar_importer.py` locally
2. In Blender → **Edit → Preferences → Add-ons → Install...**
3. Select the file and enable the add-on
4. Open the *Sidebar → StoryChar* tab and click **Import Hybrid Character**

---

## 🤝 Collaboration Plan

| Phase | Focus | Partners |
|-------|--------|----------|
| **I** | Open API for hybrid character data | Developers, librarians, data curators |
| **II** | Blender integration and visualization | Game artists, creative coders |


---

## 📚 References

- Ollikainen, J. (2022). *Hybrid Image of Multiple Fantastical Characters.* Conference Proceedings, Paris, France, September 20–21.  
- Lehman, J., Risi, S., & Clune, J. (2016). *Creative generation of 3D objects with deep learning and innovation engines.* ICCC.  
- Boden, M. (2004). *The Creative Mind: Myths and Mechanisms.* Routledge.


---

**Author:** Juhapekka Ollikainen  
**Contact:** pekollik@gmail.com  
**Keywords:** creative coding, computational creativity, creative writing, Python, Blender, hybrid characters





