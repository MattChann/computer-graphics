# Work 09: Providing Illumination

Due: Monday 04/27 10:00am

GitHub link: https://github.com/mks66/lighting.git

Implement the Phong Reflection model with flat shading. (Note: if you look up information online, do not confuse this with Phong Shading).
- You should be calculating I once per polygon.
- Remember to limit I to be in the range [0, 255]. You may not want to do this all at once at the end.
- There are a lot of user-defined values in lighting calculation, eventually, we will to be able to set them in our scripts. For now, pass them around to the necessary functions, and set them in either your main/parser functions. This is modeled in the provided source code.
