# Hybrid Image of Multiple Fantastical Characters

## Overview

**Author:** Juhapekka Ollikainen  
**Keywords:** creative coding, computational creativity, creative writing, roleplaying games, Python, scripting

This project builds on the research paper *“Hybrid Image of Multiple Fantastical Characters”*  
(published in the *Conference Proceedings, Paris, France, September 20–21, 2022*, p. 262).  
The goal is to design an open data API and Blender add-on that generate **hybrid mythological characters** — blending story archetypes, creatures, and public-domain sources into 3D assets and narrative metadata.

The system develops in **two phases**:

1. **Phase 1 — Open Data API:**  
   Provide access to story fragments, character schemas, and hybrid design metadata.

2. **Phase 2 — Blender Add-on:**  
   Allow artists, writers, and game developers to generate 3D character prototypes directly in Blender, using the open narrative data.

---

## Phase 1 — Open Data API Specification

### Base URL
https://api.hybridimage.org/v1/

pgsql
Kopioi koodi

### Authentication
Currently **no authentication** is required (public beta).  
Future versions may use API keys.

---

### Endpoints

#### 1. `GET /characters/random`
Returns a randomly generated hybrid character.



Features:

Fetch random or specific hybrid characters from the API

Offline sample mode for demoing without a network connection

Creates metadata fields (name, description) on imported objects

Installation:

Save storychar_importer.py

In Blender, open Edit → Preferences → Add-ons → Install

Select the file and enable the add-on

In 3D View → Sidebar (N) → StoryChar tab → click Import Hybrid Character

Collaboration Plan
Phase	Focus	Partners
I	Open API for public-domain hybrid character data	Developers, librarians, data curators
II	Blender integration and visual prototyping	Game artists, creative coders
III	AI-assisted storytelling extensions	Research collaborators

References
Juhapekka Ollikainen, Hybrid Image of Multiple Fantastical Characters,
Conference Proceedings, Paris, France, September 20–21 2022, p. 262

Joel Lehman, Sebastian Risi, and Jeff Clune. “Creative generation of 3D objects with deep learning and innovation engines.”
Proceedings of the 7th International Conference on Computational Creativity, 2016.

Margaret Boden, The Creative Mind: Myths and Mechanisms, 2nd ed., Routledge (2004).

License
This project is distributed under the MIT License.
All hybrid character content derived from public domain materials is open for educational and creative use.

Hybrid Image Platform © 2025 — Research-driven collaboration between open-source developers and digital creatives.
